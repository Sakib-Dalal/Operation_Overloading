# Complex Number Module

This Python module provides a `Complex` class that allows you to perform arithmetic operations on complex numbers. The module includes methods for addition, subtraction, multiplication, division, and modulo operations.

## Usage

1. Import the `module` in your main script (e.g., `main.py`):

    ```python
    import module
    ```

2. Create instances of the `Complex` class and perform arithmetic operations:

    ```python
    c1 = module.Complex(1.0, 2.0)
    c2 = module.Complex(1.0, 2.0)

    # Addition
    c3 = c1 + c2
    c3.display()

    # Subtraction
    c3 = c1 - c2
    c3.display()

    # Multiplication
    c3 = c1 * c2
    c3.display()

    # Division
    c3 = c1 / c2
    c3.display()

    # Modulo
    c3 = c1 % c2
    c3.display()
    ```

## Complex Class

The `Complex` class has the following attributes:

- `__real`: Represents the real part of the complex number.
- `__imag`: Represents the imaginary part of the complex number.

## Arithmetic Operations

The class provides the following arithmetic operators:

- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulo)

These operators can be used to perform the corresponding complex number arithmetic operations.

## Displaying Output

The `display` method is available to print the real and imaginary parts of a complex number:

```python
c3.display()
```

This will print the real and imaginary parts of the result of the arithmetic operation.

Feel free to modify and integrate this module into your projects as needed.
