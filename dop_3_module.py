data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, (int, float)):
            sum_ += i
        elif isinstance(i, str):
           sum_ += len(i)
        elif isinstance(i, (list, tuple, set)):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sum_ += calculate_structure_sum(i.keys())
            sum_ += calculate_structure_sum(i.values())
    return sum_
result = calculate_structure_sum(data_structure)

print(result)

