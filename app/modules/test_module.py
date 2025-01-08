# test_module.py
import cupy as cp

def gpu_sum_of_squares(data_list):
    gpu_data = cp.array(data_list, dtype=cp.float32)
    squared = cp.square(gpu_data)

    result = cp.sum(squared).get()
    return result

if __name__ == "__main__":
    test = [1, 2, 3, 4]
    print(gpu_sum_of_squares(test))
