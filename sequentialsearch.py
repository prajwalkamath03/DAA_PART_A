def sequential_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i  # Return the index where the target was found
    return -1  # Return -1 if the target was not found

# Example usage:
if __name__ == "__main__":
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target_value = 9
    
    result = sequential_search(my_list, target_value)
    
    if result != -1:
        print(f"Target {target_value} found at index {result}")
    else:
        print(f"Target {target_value} not found in the list")
