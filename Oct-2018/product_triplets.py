# coding=utf-8
"""
    Created by prakash on 14/12/18
"""

__author__ = 'Prakash14'


def check_condition(nums, x, y, z):
    return nums[x] == nums[y] * nums[z] or nums[y] == nums[x] * nums[z] or nums[z] == nums[y] * nums[x]


def get_product_triplets():
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        number_of_inputs = int(input())
        inputs = [int(i) for i in input().split(" ")]
        while inputs.__len__() < number_of_inputs:
            inputs.extend([int(i) for i in input().split(" ")])
        if inputs.__len__() > number_of_inputs:
            raise ValueError("More number of inputs given")
        x = 1
        counts = 0
        while x <= number_of_inputs - 2:
            y = x + 1
            while y <= number_of_inputs - 1:
                z = y + 1
                while z <= number_of_inputs:
                    if check_condition(inputs, x=x-1, y=y-1, z=z-1):
                        counts += 1
                    z += 1
                y += 1
            x += 1
        print(f"Case #{test_case+1}: {counts}")


get_product_triplets()
