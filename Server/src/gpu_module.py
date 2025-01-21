# gpu_module.py
import cupy as cp


def gpu_vector_addition(a_list, b_list):
    """Compute the sum of two vectors using the GPU."""

    a = cp.array(a_list)
    b = cp.array(b_list)

    result = a + b

    return result.tolist()  # Convert the result back to a Python list


# Define input and output data types (explicit definitions for API integration)
input_type = {"a_list": list, "b_list": list}
output_type = list

# Test
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    result = gpu_vector_addition(a, b)

    print(f"GPU Vector Addition Results: {result}")
