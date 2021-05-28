"""
Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:

Przykład użycia:
> przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    )

[4, 5, 6]

"""

def przytnij (data, start, stop)->list:
    """

    :param data:
    :param start:
    :param stop:
    :return:
    """

    list_filtered_result = list(filter(stop,list(filter(start, data))))
    return list_filtered_result

print (f" {przytnij(data=[1, 2, 3, 4, 5, 6, 7],start=lambda x: x > 3, stop=lambda x: x <= 6)}")