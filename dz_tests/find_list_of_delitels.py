def find_list_of_delitels(n, d=2):
    if n < 0:
        n = -n
    if n == 1 or n ==0:
        return []
    if n % d== 0:
        return [d] + find_list_of_delitels(n // d, d)
    return find_list_of_delitels(n, d+1)
