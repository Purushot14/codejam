# coding=utf-8
"""
    Created by prakash on 17/12/18
"""

# from threading import Thread as cls
from multiprocessing import Process as cls

__author__ = 'Prakash14'


def _run(test_case, number_of_inputs, forbidden_sequences):
    possible_sequences = pow(2, number_of_inputs)
    number_of_forbidden = 0
    _forbidden_sequences = []
    forbidden_sequences.sort()
    forbidden_sequences = list(set(forbidden_sequences))
    _duplicate = []
    for forbidden in forbidden_sequences:
        for _forbidden in forbidden_sequences:
            if forbidden == _forbidden:
                continue
            elif _forbidden.startswith(forbidden):
                _duplicate.append(_forbidden)
    for _ in set(_duplicate):
        forbidden_sequences.remove(_)
    for forbidden in forbidden_sequences:
        if forbidden.__len__() == number_of_inputs:
            number_of_forbidden += 1
        else:
            number_of_forbidden = number_of_forbidden + pow(2, number_of_inputs-forbidden.__len__())
    _ = possible_sequences - number_of_forbidden or 0
    print(f"Case #{test_case+1}: { 0 if _< 0 else _ }")


def get_big_buttons():
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        number_of_inputs, forbidden = [int(i) for i in input().split(" ")]
        if 1 <= forbidden <= min(pow(2, number_of_inputs), 100):
            forbidden_sequences = []
            for i in range(forbidden):
                forbidden_sequences.append(input())
            # cls(target=_run, kwargs={"test_case": test_case,
            #                          "number_of_inputs": number_of_inputs,
            #                          "forbidden_sequences": forbidden_sequences}).start()
            _run(test_case, number_of_inputs, forbidden_sequences)


get_big_buttons()
