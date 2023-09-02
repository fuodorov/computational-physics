"""
Documentation: http://neerc.ifmo.ru/wiki/index.php?title=Представление_вещественных_чисел&oldid=84685
"""

import numpy as np


class FloatingTypeError(TypeError):
    message: str = "The given floating point type must be either np.floating."

    def __init__(self, message: str = message):
        super().__init__(message)


def get_machine_epsilon(number_type: np.floating) -> np.floating:
    """Get the machine epsilon for a given floating point type.

    Args:
        number_type (np.floating): The floating point type to get the machine epsilon for.

    Returns:
        np.floating: The machine epsilon for the given floating point type.

    Raises:
        FloatingTypeError: The given floating point type must be either np.floating.

    Doctests:
        >>> get_machine_epsilon(np.float32) == np.finfo(np.float32).eps
        True
        >>> get_machine_epsilon(np.float64) == np.finfo(np.float64).eps
        True
    """

    if not isinstance(number_type(1.0), np.floating):
        raise FloatingTypeError()

    machine_epsilon = number_type(1.0)

    while number_type(1.0) + machine_epsilon > number_type(1.0):
        machine_epsilon /= number_type(2.0)

    return machine_epsilon * number_type(2.0)


def get_number_of_mantissa_bits(number_type: np.floating) -> int:
    """Get the number of mantissa bits for a given floating point type.

    Args:
        number_type (np.floating): The floating point type to get the number of mantissa bits for.

    Returns:
        int: The number of mantissa bits for the given floating point type.

    Raises:
        FloatingTypeError: The given floating point type must be either np.floating.

    Doctests:
        >>> get_number_of_mantissa_bits(np.float32) == np.finfo(np.float32).nmant
        True
        >>> get_number_of_mantissa_bits(np.float64) == np.finfo(np.float64).nmant
        True
    """

    if not isinstance(number_type(1.0), np.floating):
        raise FloatingTypeError()

    number_of_mantissa_bits = 0

    while number_type(1.0) + number_type(2.0 ** -(number_of_mantissa_bits + 1)) > number_type(1.0):
        number_of_mantissa_bits += 1

    return number_of_mantissa_bits


def get_maximum_exponent(number_type: np.floating) -> int:
    """Get the maximum exponent for a given floating point type.

    Args:
        number_type (np.floating): The floating point type to get the maximum exponent for.

    Returns:
        int: The maximum exponent for the given floating point type.

    Raises:
        FloatingTypeError: The given floating point type must be either np.floating.

    Doctests:
        >>> get_maximum_exponent(np.float32) == np.finfo(np.float32).maxexp
        True
        >>> get_maximum_exponent(np.float64) == np.finfo(np.float64).maxexp
        True
    """

    if not isinstance(number_type(1.0), np.floating):
        raise FloatingTypeError()

    maximum_exponent = 0
    maximum_exponent_value = number_type(1.0)

    while maximum_exponent_value != number_type("inf"):
        maximum_exponent_value *= number_type(2.0)
        maximum_exponent += 1

    return maximum_exponent


def get_minimum_exponent(number_type: np.floating) -> int:
    """Get the minimum exponent for a given floating point type.

    Args:
        number_type (np.floating): The floating point type to get the minimum exponent for.

    Returns:
        int: The minimum exponent for the given floating point type.

    Raises:
        FloatingTypeError: The given floating point type must be either np.floating.


    Doctests:
        >>> get_minimum_exponent(np.float32) == np.finfo(np.float32).minexp
        True
        >>> get_minimum_exponent(np.float64) == np.finfo(np.float64).minexp
        True
    """

    if not isinstance(number_type(1.0), np.floating):
        raise FloatingTypeError()

    minimum_exponent = 0
    minimum_exponent_value = number_type(1.0)

    while minimum_exponent_value != number_type(0.0):
        minimum_exponent_value /= number_type(2.0)
        minimum_exponent -= 1

    return minimum_exponent + get_number_of_mantissa_bits(number_type) + 1


if __name__ == "__main__":
    for np_type in [np.float32, np.float64]:
        epsilon = get_machine_epsilon(np_type)
        mantissa_bits = get_number_of_mantissa_bits(np_type)
        max_exp = get_maximum_exponent(np_type)
        min_exp = get_minimum_exponent(np_type)

        print(f"{np_type.__name__}:")
        print(f"Machine epsilon: {epsilon}")
        print(f"Number of mantissa bits: {mantissa_bits}")
        print(f"Maximum exponent: {max_exp}")
        print(f"Minimum exponent: {min_exp}")
        print()

    np_type = np.float32
    epsilon = get_machine_epsilon(np_type)
    print(f"1 < 1 + eps: {np_type(1.0) < np_type(1.0) + epsilon}")
    print(f"1 == 1 + eps / 2: {np_type(1.0) == np_type(1.0) + epsilon / np_type(2.0)}")
    print(f"1 < 1 + eps + eps / 2: {np_type(1.0) < np_type(1.0) + epsilon + epsilon / np_type(2.0)}")
    print(f"1 + eps/2 < 1 + eps: {np_type(1.0) + epsilon / np_type(2.0) < np_type(1.0) + epsilon}")
    print(
        f"1 + eps/2 < 1 + eps + eps / 2: {np_type(1.0) + epsilon / np_type(2.0) < np_type(1.0) + epsilon + epsilon / np_type(2.0)}"  # noqa: E501
    )
    print(
        f"1 + eps < 1 + eps + eps / 2: {np_type(1.0) + epsilon < np_type(1.0) + epsilon + epsilon / np_type(2.0)}"  # noqa: E501
    )
