data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(things):
    a = 0
    if isinstance(things, int):
        a += things
        return a
    for i in things:
        if isinstance(i, (list, tuple, set)):
            a += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for j in i.keys():
                a += calculate_structure_sum(j)
            for j in i.values():
                a += calculate_structure_sum(j)
        elif isinstance(i, str):
            a += len(i)
        else:
            a += i
    return a

result = calculate_structure_sum(data_structure)
print(result)