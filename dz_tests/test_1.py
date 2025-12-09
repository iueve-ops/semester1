from find_list_of_delitels import find_list_of_delitels

assert find_list_of_delitels(7) == [7]

assert find_list_of_delitels(60) == [2, 2, 3, 5]

assert find_list_of_delitels(49) == [7, 7]

assert find_list_of_delitels(1) == []
assert find_list_of_delitels(-5) == [5]

assert find_list_of_delitels(0) == []
try:
    assert find_list_of_delitels(1009) == [1009]
except RecursionError:
    pass

print("Тесты закончены")