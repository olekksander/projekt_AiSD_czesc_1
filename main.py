import time
import random
import pandas as pd

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time_sorting(method, data):
    start_time = time.time()
    method(data)
    end_time = time.time()
    return end_time - start_time

def run_experiment(data_generator, method_names):
    sizes = list(range(10, 1001, 10))
    results = {"Data Size": sizes}

    for method_name in method_names:
        method_results = []
        for size in sizes:
            data = data_generator(size)
            time_taken = measure_time_sorting(eval(method_name), data.copy())
            method_results.append(time_taken)
        results[method_name] = method_results

    return results

def random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def ascending_data(size):
    return list(range(1, size + 1))

def descending_data(size):
    return list(range(size, 0, -1))

def save_to_excel(results, filename):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    method_names = ["selection_sort", "bubble_sort", "optimized_bubble_sort", "insertion_sort"]

    random_results = run_experiment(random_data, method_names)
    ascending_results = run_experiment(ascending_data, method_names)
    descending_results = run_experiment(descending_data, method_names)

    save_to_excel(random_results, "random_results.xlsx")
    save_to_excel(ascending_results, "ascending_results.xlsx")
    save_to_excel(descending_results, "descending_results.xlsx")

    print("Results saved to Excel files.")