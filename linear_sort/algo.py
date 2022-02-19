from typing import *

__all__ = ["insertion_sort", "bubble_sort", "selection_sort"]


def insertion_sort(arr: List, cmp=None) -> None:
    """
    Insertion sort algorithm.
    Algo: a sub-list is maintained which is always sorted. whenever new element is introduced, it has to find its
    appropriate place So that sub-list should be sorted.

    :param arr: original array or list
    :param cmp: comparison logic
    :return: None

    Example-1:
    a = [7, 5, 4, 2, 9, 1, 6, 8]
    insertion_sort(a)
    sorted a = [1, 2, 4, 5, 6, 7, 8, 9]

    Example-2:
    a = [7, 5, 4, 2, 9, 1, 6, 8]
    insertion_sort(a, cmp=lambda x: x[0] < x[1])
    sorted a = [9, 8, 7, 6, 5, 4, 2, 1]

    Example-3:
    a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    insertion_sort(a, cmp=lambda x: x[0][0] > x[1][0])  # compare using first element of each item
    sorted a = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]

    Example-4:
    a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    insertion_sort(a, cmp=lambda x: x[0][1] > x[1][1])
    sorted a = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    """
    if not cmp:
        cmp = lambda x: x[0] > x[1]

    for i in range(1, len(arr)):
        hole = i
        key = arr[i]
        while hole > 0 and cmp([arr[hole - 1], key]):
            arr[hole] = arr[hole - 1]
            hole = hole - 1
        arr[hole] = key


def bubble_sort(arr: List, cmp=None) -> None:
    """
    Bubble sort algorithm
    With each iteration element has to compare with its adjacent element, then swap if fails the comparison.

    :param arr: original array or list
    :param cmp: sorting comparison logic function
    :return: None

    Example-1: ascending order sorting
        a = [7, 5, 4, 2, 9, 1, 6, 8]
        bubble_sort(a)
        sorted a = [8, 6, 1, 9, 2, 4, 5, 7]

    Example-2: descending order sorting
        a = [7, 5, 4, 2, 9, 1, 6, 8]
        bubble_sort(a, cmp=lambda x: x[0] < x[1])
        sorted a = [9, 8, 7, 6, 5, 4, 2, 1]

    Example-3: ascending using first element of each item
        a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
        bubble_sort(a, cmp=lambda x: x[0][0] > x[1][0])
        sorted a = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]

    Example-4: ascending using second element of each item
        a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
        bubble_sort(a, cmp=lambda x: x[0][1] > x[1][1])
        sorted a = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    """
    if not cmp:
        cmp = lambda x: x[0] > x[1]

    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if cmp([arr[i],arr[i + 1]]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def selection_sort(arr: List, cmp=None) -> None:
    """
    Selection sort algorithm
    start first to end:
        find index of minimum element by iterating from current index to end
        swap if min index is not equal to current index
    :param arr: original array or list
    :param cmp: comparison logic
    :return: None

    Example-1:
    a = [7, 5, 4, 2, 9, 1, 6, 8]
    selection_sort(a)
    sorted a = [1, 2, 4, 5, 6, 7, 8, 9]

    Example-2:
    a = [7, 5, 4, 2, 9, 1, 6, 8]
    selection_sort(a, cmp=lambda x: x[0] < x[1])
    sorted a = [9, 8, 7, 6, 5, 4, 2, 1]

    Example-3:
    a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    selection_sort(a, cmp=lambda x: x[0][0] > x[1][0])  # compare using first element of each item
    sorted a = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]

    Example-4:
    a = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    selection_sort(a, cmp=lambda x: x[0][1] > x[1][1])
    sorted a = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    """
    if not cmp:
        cmp = lambda x: x[0] > x[1]

    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if cmp([arr[min_idx], arr[j]]):
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
