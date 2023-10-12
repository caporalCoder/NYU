


from collections import OrderedDict
from functools import reduce
import itertools

sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2,7,7,9,0,0,11,-5,-3]

def print_list(lst):
    print(sorted(lst))

def remove_naive(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

def remove_conds(lst):
    new_list = []
    [new_list.append(i) for i in lst if i not in new_list]
    return new_list

def remove_set(lst):
    return list(set(lst))

def remove_enum(lst):
    return [item for index, item in enumerate(lst) if lst.index(item) == index]

def remove_coll(lst):
    return list(OrderedDict.fromkeys(lst))

def remove_dict_comprehension(lst):
    return list({i: None for i in lst}.keys())

def remove_reduce(lst):
    return reduce(lambda l, x: l.append(x) or l if x not in l else l, lst, [])

def remove_itertools_groupby(lst):
    return [key for key, group in itertools.groupby(sorted(lst))]

def remove_helper_func(lst):
    seen = set()
    def helper(x):
        if x not in seen:
            seen.add(x)
            return True
        return False
    return [i for i in lst if helper(i)]

print_list(remove_naive(sample_list))
print_list(remove_conds(sample_list))
print_list(remove_set(sample_list))
print_list(remove_enum(sample_list))
print_list(remove_coll(sample_list))
print_list(remove_dict_comprehension(sample_list))
print_list(remove_reduce(sample_list))
print_list(remove_itertools_groupby(sample_list))
print_list(remove_helper_func(sample_list))
