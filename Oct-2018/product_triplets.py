# coding=utf-8
"""
    Created by prakash on 14/12/18
"""

# from threading import Thread as cls
from multiprocessing import Process as cls

__author__ = 'Prakash14'


def check_condition(nums, x, y, z):
    return nums[x] == nums[y] * nums[z] or nums[y] == nums[x] * nums[z] or nums[z] == nums[y] * nums[x]


def _run(test_case, number_of_inputs, inputs):
    x = 1
    counts = 0
    unique = set(inputs)
    is_run = True
    if unique.__len__() == 1 and inputs[0] != 0 and inputs[0] != 1:
        is_run = False

    while is_run and x <= number_of_inputs - 2:
        y = x + 1
        while y <= number_of_inputs - 1:
            z = y + 1
            while z <= number_of_inputs:
                if x != y != z and check_condition(inputs, x=x - 1, y=y - 1, z=z - 1):
                    counts += 1
                z += 1
            y += 1
        x += 1
    print(f"Case #{test_case+1}: {counts}")


def get_product_triplets():
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        number_of_inputs = int(input())
        inputs = [int(i) for i in input().split(" ")]
        while inputs.__len__() < number_of_inputs:
            inputs.extend([int(i) for i in input().split(" ")])
        if inputs.__len__() > number_of_inputs:
            raise ValueError("More number of inputs given")

        cls(target=_run, kwargs={"test_case": test_case,
                                 "number_of_inputs": number_of_inputs,
                                 "inputs": inputs}).start()

get_product_triplets()
