data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# def calculate_structure_sum(data_structure):
#     sum_ = 0
#     for i_item in data_structure:
#         if isinstance(i_item, tuple) or isinstance(i_item, list) or isinstance(i_item, set):
#             for element in i_item:
#                 if isinstance(element, int):
#                     sum_ += element
#                 elif isinstance(element, str):
#                     sum_ += len(element)
#                 elif isinstance(element, dict):
#                     for key, value in element.items():
#                         if isinstance(value, str):
#                             sum_ += len(value)
#                         elif isinstance(value, int):
#                             sum_ += value
#                         sum_ += len(key)
#                 else:
#                     sum_ += calculate_structure_sum(element)
#         elif isinstance(i_item, dict):
#             for key, value in i_item.items():
#                 if isinstance(value, str):
#                     sum_ += len(value)
#                 elif isinstance(value, int):
#                     sum_ += value
#                 sum_ += len(key)
#
#         elif isinstance(i_item, str):
#             sum_ += len(i_item)
#
#         elif isinstance(i_item, int):
#             sum_ += i_item
#
#     return sum_

def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, int):
            sum_ += i
        else:
            if isinstance(i, dict):
                i = tuple(i.items())
                sum_ += calculate_structure_sum(i)
            else:
                sum_ += calculate_structure_sum(i)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)
