count = 0
while True:
    try:
        sqnc = list(map(float, input('Введите последовательность чисел через пробел: ').split()))
        num = float(input('Введите любое число: '))
        break
    except ValueError:
        print('Некорректный ввод данных')
        count += 1
        if count < 5:
            continue
        else:
            print('Поздравляю тебя, Шарик, ты - балбес!')
            exit()


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element and array[middle - 1] != element:
        return middle
    elif array[middle] == element and array[middle - 1] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sqnc_sort = merge_sort(sqnc)
print(f'Введённая последовательность после сортировки: {sqnc_sort}')

if num < sqnc_sort[0] or num > sqnc_sort[-1]:
    print('Введённое число не является частью выбранного диапазона')
elif num == sqnc_sort[0]:
    print('Введённое число является первым в последовательности')
else:
    sqnc_sort.append(num)
    nxt_sqnc = merge_sort(sqnc_sort)
    num_i = binary_search(nxt_sqnc, num, 0, len(nxt_sqnc) - 1)
    print(f'Индекс числа, которое меньше введённого, а следующее за ним больше или равно ему: {num_i - 1}')
