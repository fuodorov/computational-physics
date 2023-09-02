import numpy as np


def get_machine_epsilon(eps: np.float32 | np.float64) -> np.float32 | np.float64:
    """Get the machine epsilon for a given floating point type.

    Args:
        eps (np.float32|np.float64): The floating point type to get the machine epsilon for.

    Returns:
        np.float32|np.float64: The machine epsilon for the given floating point type.
    """

    # Initialize the machine epsilon to 1.0
    machine_epsilon = eps(1.0)

    # While the machine epsilon plus the machine epsilon divided by 2.0 is greater than the machine epsilon
    while eps(1.0) + machine_epsilon / eps(2.0) > eps(1.0):
        # Divide the machine epsilon by 2.0
        machine_epsilon /= eps(2.0)

    # Return the machine epsilon
    return machine_epsilon


def get_number_of_significant_digits(eps: np.float32 | np.float64) -> int:
    """Get the number of significant digits for a given floating point type.

    Args:
        eps (np.float32|np.float64): The floating point type to get the number of significant digits for.

    Returns:
        int: The number of significant digits for the given floating point type.
    """

    # Initialize the number of significant digits to 0
    number_of_significant_digits = 0

    # Get the machine epsilon for the given floating point type
    machine_epsilon = get_machine_epsilon(eps)

    # While the machine epsilon is greater than 0.0
    while machine_epsilon > eps(0.0):
        # Divide the machine epsilon by 10.0
        machine_epsilon /= eps(10.0)

        # Increment the number of significant digits
        number_of_significant_digits += 1

    # Return the number of significant digits
    return number_of_significant_digits


def get_max_power_of_number(number: np.float32 | np.float64, eps: np.float32 | np.float64) -> int:
    """Get the maximum power of a given number for a given floating point type.

    Args:
        number (np.float32|np.float64): The number to get the maximum power for.
        eps (np.float32|np.float64): The floating point type to get the maximum power for.

    Returns:
        int: The maximum power of the given number for the given floating point type.
    """

    # Initialize the maximum power to 0
    max_power_of_number = 0

    # Get the machine epsilon for the given floating point type
    machine_epsilon = get_machine_epsilon(eps)

    # While the machine epsilon is greater than 0.0
    while machine_epsilon > eps(0.0):
        # Divide the machine epsilon by the given number
        machine_epsilon /= number

        # Increment the maximum power
        max_power_of_number += 1

    # Return the maximum power
    return max_power_of_number


if __name__ == "__main__":
    # Get the machine epsilon for single precision
    epsilon = get_machine_epsilon(np.float32)
    significant_digits = get_number_of_significant_digits(np.float32)
    max_power = get_max_power_of_number(np.float32(2.0), np.float32)

    # Print the machine epsilon for single precision
    print(f"Machine epsilon for single precision: {epsilon}")
    print(f"Number of significant digits for single precision: {significant_digits}")
    print(f"Maximum power of ten for single precision: {max_power}")

    # Get the machine epsilon for double precision
    epsilon = get_machine_epsilon(np.float64)
    significant_digits = get_number_of_significant_digits(np.float64)
    max_power = get_max_power_of_number(np.float64(2.0), np.float64)

    # Print the machine epsilon for double precision
    print(f"Machine epsilon for double precision: {epsilon}")
    print(f"Number of significant digits for double precision: {significant_digits}")
    print(f"Maximum power of ten for double precision: {max_power}")

    # Compare four numbers with each other 1, 1+epsilon/2, 1+epsilon, 1+epsilon+epsilon/2
    print(f"1.0 == 1.0 + epsilon/2.0: / {np.equal(np.float64(1.0), np.float64(1.0) + np.float64(epsilon/2.0))}")
    print(f"1.0 == 1.0 + epsilon: {np.equal(np.float64(1.0), np.float64(1.0) + np.float64(epsilon))}")
    print(
        f"1.0 == 1.0 + epsilon + epsilon/2.0: {np.equal(np.float64(1.0), np.float64(1.0) + np.float64(epsilon + epsilon/2.0))}"
    )
    print(
        f"1.0 + epsilon/2.0 == 1.0 + epsilon: {np.equal(np.float64(1.0) + np.float64(epsilon/2.0), np.float64(1.0) + np.float64(epsilon))}"
    )
    print(
        f"1.0 + epsilon/2.0 == 1.0 + epsilon + epsilon/2.0: {np.equal(np.float64(1.0) + np.float64(epsilon/2.0), np.float64(1.0) + np.float64(epsilon + epsilon/2.0))}"
    )
    print(
        f"1.0 + epsilon == 1.0 + epsilon + epsilon/2.0: {np.equal(np.float64(1.0) + np.float64(epsilon), np.float64(1.0) + np.float64(epsilon + epsilon/2.0))}"
    )
