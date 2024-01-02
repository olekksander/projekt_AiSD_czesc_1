import time
import random
import tabulate

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_flag(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time

def run_tests(size):
    random_data = [random.randint(1, 1000) for _ in range(size)]
    ascending_data = list(range(1, size + 1))
    descending_data = list(range(size, 0, -1))

    results = []

    for data, label in zip([random_data, ascending_data, descending_data], ['Random', 'Ascending', 'Descending']):
        row = [label]
        for sort_func, sort_label in zip([selection_sort, bubble_sort, bubble_sort_flag, insertion_sort],
                                        ['Selection', 'Bubble', 'Bubble with Flag', 'Insertion']):
            sorted_data = data.copy()
            elapsed_time = measure_time(sort_func, sorted_data)
            row.append(round(elapsed_time, 6))
        results.append(row)

    return results

def print_results(results):
    headers = ['Input Type', 'Selection Sort', 'Bubble Sort', 'Bubble Sort (Flag)', 'Insertion Sort']
    print(tabulate.tabulate(results, headers, tablefmt="grid"))

def main():
    sizes = list(range(1000, 100001, 1000))
    all_results = []

    for size in sizes:
        results = run_tests(size)
        all_results.extend(results)

    print_results(all_results)

if __name__ == "__main__":
    main()