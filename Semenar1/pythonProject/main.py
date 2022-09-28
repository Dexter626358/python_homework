def counting(a):
    for i in range(a):
        b = (-3) ** i
        print(b, end=" ")

counting(5)

def sequence_List(n):
    list_ = []
    print()
    for i in range(n):

        list_.append(3 * i + 1)
    return list_

print(sequence_List(6))

def count_sub_string(str1, str2):
    return len(str1.split(str2)) - 1

print(count_sub_string("aaaabcbbbabcccc", "abc"))



