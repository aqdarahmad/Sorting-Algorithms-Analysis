import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000) 



def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

#  Quick Sort 
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot_index = random.randint(low, high)  # ✅ اختيار pivot عشوائي
        items[high], items[pivot_index] = items[pivot_index], items[high]  # ✅ تبديل
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)



def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()
    return (end - start) * 1000  



def run_experiment():
    sizes = [100, 1000, 5000] 
    data_types = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array,
    }
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    results = {alg: {dtype: [] for dtype in data_types} for alg in algorithms}

    for size in sizes:
        print(f"Testing size: {size}")
        for dtype, gen_func in data_types.items():
            for alg_name, alg_func in algorithms.items():
                times = []
                for _ in range(5): 
                    data = gen_func(size)
                    data_copy = data.copy()
                    elapsed = measure_time(alg_func, data_copy)
                    times.append(elapsed)
                avg_time = sum(times) / len(times)
                results[alg_name][dtype].append(avg_time)
                print(f"{alg_name} on {dtype} data: {avg_time:.2f} ms")
    return sizes, results


def plot_results(sizes, results):
    for dtype in ["Random", "Sorted", "Reverse Sorted"]:
        plt.figure(figsize=(10, 6))
        for alg_name, data in results.items():
            plt.plot(sizes, data[dtype], marker='o', label=alg_name)
        plt.title(f"Execution Time on {dtype} Data")
        plt.xlabel("Input Size")
        plt.ylabel("Time (ms)")
        plt.yscale('log') 
        plt.legend()
        plt.grid(True, which="both", ls="--", linewidth=0.5)
        plt.show()




if __name__ == "__main__":
    sizes, results = run_experiment()
    plot_results(sizes, results)
