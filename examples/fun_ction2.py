# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:20:59 2020

@author: JIWU5
"""

import copy


def tuple_types(input_tuple):
    """
    tuple_types:
        checks every element of given tuple and reports back on its type
    parameters: 
        input_tuple
    return: 
        resulted tuple of types
    """
    med = [type(i) for i in list(input_tuple)]

    return tuple(med)


def remove_element(input_tuple, element):
    """
    remove_element:
        removes an element from given tuple
    parameters:
        input_tuple
        element: element to be removed (not index)
    return: 
        resulted tuple
    """
    med = list(input_tuple)
    med.remove(element)

    return tuple(med)


def check_containment(input_string, lookup_string):
    """
    check_containment:
        checks for substring availability in given string
    parameters:
        input_string: full string
        param lookup_string: target substring
    return: 
        True/False
    """
    if lookup_string in input_string:
        return True
    return False

def reverse(input_string):
    """
    reverse: 
        reverses given string using slicing
    parameters:
        input_string: given string
    return: 
        resulted reversed string
    """
    return input_string[::-1]

def concatenate(list1, list2):
    """
    concatenate:
        concatenates two lists index-wise, two lists can have different length
    parameters:
        list1, list2
    :return: 
        resulted list
    """
    if len(list1) > len(list2):
        return[str(i) + str(j) for i, j in zip(list1, list2)] + list1[len(list2):]
    if len(list1) == len(list2):
        return [str(i) + str(j) for i, j in zip(list1, list2)]
    if len(list1) < len(list2):
        return[str(i) + str(j) for i, j in zip(list1, list2)] + list2[len(list1):]

def concatenate_list_of_lists(input_list):
    """
    concatenate_list_of_lists:
        concatenate all list elements index-wise
    parameters:
        input_list:ist of lists
    return: 
        resulted list
    """

    output_list = []

    for i in range(len(input_list)):
        element = ""
        for lst in input_list:
            element += str(lst[i])
        output_list.append(element)
    return output_list



def deep_copy(input_list):
    """
    deep_copy:
        create a deep copy of the given list
    parameters:
        input_list
    return: 
        deep copy of input_list
    """
    return copy.deepcopy(input_list)

def find(input_dict, lookup_key):
    """
    find:
        find all elements with specified key, 
        accounting for the case where given dictionary 
        is a dict of dicts and traversing all elements of inner dict elements
    parameters:
        input_dict: dictionary, or dict of dict
        lookup_key: key of element(s)
    return: 
        resulted tuple of key, value pairs or such elements
    """
    
    result = list()
    for key, value in input_dict.items():

        try:
            if key == lookup_key:
                result.append(value)
                
        except:pass

        try:
            for skey, svalue in value.items():
                if skey == lookup_key:
                    result.append(svalue)
                    
        except:pass
    
    return result

def min_value(input_dict):
    """
    min_value: 
        find the key corresponding to the minimum value from the given dictionary
    parameters:
        input_dict: dictionary
    return: 
        key of the minimum value
    """
    return min(input_dict,key = lambda x:input_dict[x])



t_uple = ('123',123)
lis_t = list(t_uple)
lis_t2 = [1,2,3]
lis_t3 = ['a', 'b', 'c']

substring = "12"
s_tring = "123"
di_ct1 = {
        'a': {'b': 1,  'c': 2},
        'c': {'c': 2, 'b': 3}
                 }
di_ct2 = {"NY": 10, "BST": 20, "TYU": 5}

def main():

    print("tuple_types:",tuple_types(t_uple))
    
    print("remove_element:",remove_element(t_uple,t_uple[0]))
    
    print("check_containment:",check_containment(s_tring,substring))
    
    print("reverse:",reverse(s_tring))
    
    print("concatenate:",concatenate(lis_t2, lis_t3))
    
    print("concatenate_list_of_lists:",concatenate_list_of_lists([lis_t2,lis_t3]))
    
    print("deep_copy:",deep_copy(lis_t))
    
    print("find:",find(di_ct1, 'c'))
    
    print("min_value:",min_value(di_ct2))


if __name__ == "__main__":
    main()