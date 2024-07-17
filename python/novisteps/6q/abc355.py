N, M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

a_dict = {key: "a" for key in A}
b_dict = {key: "b" for key in B}

c_dict = a_dict | b_dict
sorted_c_dict = dict(sorted(c_dict.items()))
sorted_c_dict_values_joined = "".join(map(str, list(sorted_c_dict.values())))

if "aa" in sorted_c_dict_values_joined:
    print("Yes")
else:
    print("No")
