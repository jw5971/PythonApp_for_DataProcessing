import pandas as pd
import sys

import frelabpy.utils.misc_util as miscu


SAMPLE_ASSIGN_CONFIG = {
    "col_const": {
        "ASSIGN_CURRENCY": "USD",
        "ASSIGN_ACCOUNT": "SFELDMAN",
        "ASSIGN_COMMENTS": ""
    },
    "col_var": None,
    "plugin": None
}
SAMPLE_DATAFRAME = pd.DataFrame({'TYPE': ['PDF', 'XLS'],
                                 'ABBREV': ['NY', 'LDN']})


class EtlFeature(object):

    def __init__(self, name, config):
        self._name = name

        # There are two ways  for attribute assignment
        self._config = config
        #self.config(config)

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        if not isinstance(value, dict):
            raise ValueError("Provided config argument is of incorrect type")
        self_config = value

    @property
    def name(self):
        return self._name

    def identify(self):
        print(f'The name of this ETL feature instance is: {self._name}')

    def run(self):
        print("Nothing to do by calling base")
        #pass


class AssignEtlFeatureSimple(EtlFeature):
    pass


class AssignEtlFeatureOverrideMethod(EtlFeature):

    def identify(self):
        print(f'The name of this Assign ETL feature instance is: {self._name}')


class AssignEtlFeature(EtlFeature):

    def __init__(self, name, config, df):
        super().__init__(name, config)
        self._df = df

    def run(self):
        """
        ETL feature to assign new columns to a given dataframe
        :return: df_target: pd.DataFrame; Resulted dataframe
        """
        df_target = self._df
        length = len(df_target.index)
        config_assign = dict()

        # Assign new columns, using static values.
        config_assign_const = miscu.eval_elem_mapping(self._config, 'col_const')
        if config_assign_const and isinstance(config_assign_const, dict):
            config_assign.update(config_assign_const)

        # Assign new columns, using variable values.
        config_assign_var = miscu.eval_elem_mapping(self._config, 'col_var')
        if config_assign_var and isinstance(config_assign_var, dict):
            config_assign.update(config_assign_var)

        for col_name, col_value in config_assign.items():
            df_target[col_name] = [col_value] * length

        return df_target


class PlugableFeature(object):

    def __init__(self, config):
        self._plugin = miscu.eval_func(config, "plugin")

    @property
    def plugin(self):
        return self._plugin

    def run(self, df):
        df_target = df
        if self._plugin:
            df_target = self._plugin(df)
        return df_target


class PlugableAssignEtlFeature(EtlFeature, PlugableFeature):

    def __init__(self, name, config, df):
        EtlFeature.__init__(self, name, config)
        PlugableFeature.__init__(self, config)
        self._df = df

    def run(self):
        """
        ETL feature to assign new columns to a given dataframe
        :return: df_target: pd.DataFrame; Resulted dataframe
        """
        df_target = self._df
        length = len(df_target.index)
        config_assign = dict()

        # Assign new columns, using static values.
        config_assign_const = miscu.eval_elem_mapping(self._config, 'col_const')
        if config_assign_const and isinstance(config_assign_const, dict):
            config_assign.update(config_assign_const)

        # Assign new columns, using variable values.
        config_assign_var = miscu.eval_elem_mapping(self._config, 'col_var')
        if config_assign_var and isinstance(config_assign_var, dict):
            config_assign.update(config_assign_var)

        for col_name, col_value in config_assign.items():
            df_target[col_name] = [col_value] * length

        df_target = PlugableFeature.run(df_target)
        return df_target


class EtlFeatureWithId(object):

    next_id = 10

    def __init__(self, name, config):
        self._name = name
        self._config = config
        self._id = EtlFeatureWithId.next_id
        EtlFeatureWithId.next_id += 1

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        if not isinstance(value, dict):
            raise ValueError("Provided config argument is of incorrect type")
        self_config = value

    @property
    def name(self):
        return self._name

    def identify(self):
        print(f'{self._name} ETL feature instance with id {self._id}')

    def run(self):
        print("Nothing to do by calling base")
        #pass

class EtlFeatureWithStaticId(object):

    next_id = 10

    @staticmethod
    def _get_next_id():
        target = EtlFeatureWithStaticId.next_id
        EtlFeatureWithStaticId.next_id += 1
        return target

    @classmethod
    def _get_next_id2(cls):
        target = cls.next_id
        cls.next_id += 1
        return target

    def __init__(self, name, config):
        self._name = name
        self._config = config
        self._id = EtlFeatureWithStaticId._get_next_id()

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        if not isinstance(value, dict):
            raise ValueError("Provided config argument is of incorrect type")
        self_config = value

    @property
    def name(self):
        return self._name

    def identify(self):
        print(f'{self._name} ETL feature instance with id {self._id}')

    def run(self):
        print("Nothing to do by calling base")
        #pass

def main(argv):

    try:

        etl_feature = EtlFeature("EtlFeature", SAMPLE_ASSIGN_CONFIG)
        etl_feature.identify()
        etl_feature.run()

        etl_feature_simple = AssignEtlFeatureSimple("AssignEtlFeatureSimple", SAMPLE_ASSIGN_CONFIG)
        etl_feature_simple.identify()
        etl_feature_simple.run()

        etl_feature_override = AssignEtlFeatureOverrideMethod("AssignEtlFeatureOverride", SAMPLE_ASSIGN_CONFIG)
        etl_feature_override.identify()
        etl_feature_override.run()

        etl_feature_assign = AssignEtlFeature("AssignEtlFeatureOverride", SAMPLE_ASSIGN_CONFIG, SAMPLE_DATAFRAME)
        etl_feature_assign.identify()
        df_target = etl_feature_assign.run()

        etl_feature_assign_plugable = PlugableAssignEtlFeature("PlugableAssignEtlFeature", SAMPLE_ASSIGN_CONFIG,
                                                               SAMPLE_DATAFRAME)
        etl_feature_assign_plugable.identify()
        #df_target = etl_feature_assign_plugable.run()

        etl_feature = EtlFeatureWithId("EtlFeatyreWithId", SAMPLE_ASSIGN_CONFIG)
        etl_feature.identify()


        print("Exit")
    except Exception as gen_exc:
        print(gen_exc)


if __name__ == '__main__':
    # Call main process.
    main(sys.argv[1:])
