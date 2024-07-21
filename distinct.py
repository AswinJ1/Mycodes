def print_distinct_elements(arr):
    distinct_elements = set(arr)
    for i in distinct_elements:
        print(i, end=' ')
    print()  # for a new line after printing all elements

# Example usage
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print_distinct_elements(arr)
