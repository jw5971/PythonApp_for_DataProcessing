import numpy as np
import pandas as pd
import sys


def main(argv):

    try:
        df = pd.DataFrame({'COL1': ['Key1', 'Key2', 'Key3'],
                           'COL2': ['A', 'B', 'C'],
                           'COL3': [10, 10, 30]})

        # Can be an object or a list.
        df_pivot1 = df.pivot('COL1', 'COL2', 'COL3')

        df_pivot2 = df.pivot(index='COL1', columns='COL2', values=['COL3', 'COL1'])

        # Add new row to deal with indexing.
        new_row = {'COL1': 'Key1', 'COL2': 'A', 'COL3': 40}

        df = df.append(new_row, ignore_index=True)

        # Raise ValueError.
        # df_pivot3 = df.pivot('COL1', 'COL2', 'COL3')

        # Usage of pivot_table() built-in function.
        df_pivot3 = df.pivot_table(index=['COL1', 'COL2'], values=['COL3'], aggfunc=np.sum)
        df_target = pd.DataFrame(df_pivot3.to_records())
        print("Exit")
    except Exception as gen_exc:
        print(gen_exc)


if __name__ == '__main__':
    # Call main process.
    sys.exit(main(sys.argv[1:]))
