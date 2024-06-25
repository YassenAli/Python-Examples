def convert_to_dict(lst1, lst2):
    return dict(zip(lst1, lst2))
student = ['yassin', 'ali', 'mamdouh']
values = [80, 90, 100]
result_dict  = convert_to_dict(student, values)
print(result_dict)