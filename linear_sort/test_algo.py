from algo import insertion_sort, bubble_sort, selection_sort


def test_insertion_sort():
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [1, 2, 4, 5, 6, 7, 8, 9]
    insertion_sort(original)
    assert original == expected, "failed test case 1"
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [9, 8, 7, 6, 5, 4, 2, 1]
    insertion_sort(original, cmp=lambda x: x[0] < x[1])
    assert original == expected, "failed test case 2"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]
    insertion_sort(original, cmp=lambda x: x[0][0] > x[1][0])
    assert original == expected, "failed test case 3"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    insertion_sort(original, cmp=lambda x: x[0][1] > x[1][1])
    assert original == expected, "failed test case 4"


def test_bubble_sort():
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [1, 2, 4, 5, 6, 7, 8, 9]
    bubble_sort(original)
    assert original == expected, "failed test case 1"
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [9, 8, 7, 6, 5, 4, 2, 1]
    bubble_sort(original, cmp=lambda x: x[0] < x[1])
    assert original == expected, "failed test case 2"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]
    bubble_sort(original, cmp=lambda x: x[0][0] > x[1][0])
    assert original == expected, "failed test case 3"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    bubble_sort(original, cmp=lambda x: x[0][1] > x[1][1])
    assert original == expected, "failed test case 4"


def test_selection_sort():
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [1, 2, 4, 5, 6, 7, 8, 9]
    selection_sort(original)
    assert original == expected, "failed test case 1"
    original = [7, 5, 4, 2, 9, 1, 6, 8]
    expected = [9, 8, 7, 6, 5, 4, 2, 1]
    selection_sort(original, cmp=lambda x: x[0] < x[1])
    assert original == expected, "failed test case 2"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[4, 2], [6, 8], [7, 5], [7, 1], [8, 3], [9, 1]]
    selection_sort(original, cmp=lambda x: x[0][0] > x[1][0])
    assert original == expected, "failed test case 3"
    original = [[7, 5], [4, 2], [9, 1], [6, 8], [8, 3], [7, 1]]
    expected = [[9, 1], [7, 1], [4, 2], [8, 3], [7, 5], [6, 8]]
    selection_sort(original, cmp=lambda x: x[0][1] > x[1][1])
    assert original == expected, "failed test case 4"
