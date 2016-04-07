# There is a single regression build failure that we need to find as efficiently as possible using a binary search/divide and conquer
# 
# for a given numbers of builds (i.e. 20), create a script that will run the least amount of iterations to return back the first occurrence of the failure 
# 
# 
# Enjoy your interview!
# Julio

import os,sys

build_results = [
    {"build": 1, "result": True}, 
    {"build": 2, "result": True}, 
    {"build": 3, "result": True}, 
    {"build": 4, "result": True}, 
    {"build": 5, "result": True}, 
    {"build": 6, "result": True}, 
    {"build": 7, "result": True}, 
    {"build": 8, "result": True}, 
    {"build": 9, "result": False}, 
    {"build": 10, "result": False}, 
    {"build": 11, "result": False}, 
    {"build": 12, "result": False}, 
    {"build": 13, "result": False}, 
    {"build": 14, "result": False}, 
    {"build": 15, "result": False}, 
    {"build": 16, "result": False}, 
    {"build": 17, "result": False}, 
    {"build": 18, "result": False}, 
    {"build": 19, "result": False}, 
    {"build": 20, "result": False}]


def find_first_fail(build_data):
    build = len(build_data)
    for data in build_data:
        if not data.get('result'):
            b = data.get('build')
            if b < build:
                build = b
    return build

def find_first_fail_bs(build_data, i, j):
    if i <= j:
        return build_data[i].get('build')
    m = (i + j) / 2
    if build_data[m].get('result'):
        return find_first_fail_bs(build_data, m + 1, j)
    else:
        return find_first_fail_bs(build_data, i, m)
    

if __name__ == '__main__':
    print find_first_fail_bs(build_results, 0, len(build_results) - 1)

