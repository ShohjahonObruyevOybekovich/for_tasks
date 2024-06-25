
# Задача: создать функцию, которая будет на выходе иметь один общий отсортированный список res (по убыванию).
# Пользоваться sort или иными функциями для сортировки ЗАПРЕЩЕНО!



def sort_reverce(list1, list2):
    i, j = len(list1) - 1, len(list2) - 1
    res = []

    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            res.append(list1[i])
            i -= 1
        else:
            res.append(list2[j])
            j -= 1

    while i >= 0:
        res.append(list1[i])
        i -= 1

    while j >= 0:
        res.append(list2[j])
        j -= 1

    return res



list1 = [1,6,9,10,11]
list2 = [2,5,6,11,13,14]

result = sort_reverce(list1, list2)
print(result)  
