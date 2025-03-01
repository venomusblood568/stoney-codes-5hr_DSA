def sort_stack(input_stack):
    sorted_stack = []  # Auxiliary stack to store sorted elements

    while input_stack:
        temp = input_stack.pop()  # Pop the top element from the input stack

        # Move elements from sorted_stack back to input_stack if they are greater than temp
        while sorted_stack and sorted_stack[-1] > temp:
            input_stack.append(sorted_stack.pop())

        # Place temp in its correct position in sorted_stack
        sorted_stack.append(temp)

    return sorted_stack  # Sorted stack (smallest at the bottom, largest at the top)

# Example usage
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print(sorted_stack) 
