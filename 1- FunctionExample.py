def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    else:
        raise ValueError("Invalid operation. Please choose 'add', 'subtract', or 'multiply'.")

# Test methods
def test_calculator():
    assert calculator('add', 5, 3) == 8
    assert calculator('subtract', 5, 3) == 2
    assert calculator('multiply', 5, 3) == 15
    print("All tests passed!")

# Run the tests
test_calculator()
