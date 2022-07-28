nambers = [9, 8, 5, 3, 7, 2, 1, 4, 6]
def bubble_sort(lsr):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
if __name__ == '__main__':
    lst = nambers
    bubble_sort(lst)
    print(lst)
    #тут я с интернета подсмотрел))


def binary_search(list, item):
    resultok = 0
    first = nambers[0]
    last = nambers[8]
    while first <= last:
        middle = (first+last) // 2
        guess = list[middle]
        if item == middle:
            return middle
        elif guess > item:
            last = middle - 1
        else:
            low = middle + 1
            resultok = resultok + 1
            print(resultok)

print(binary_search(nambers, 2))