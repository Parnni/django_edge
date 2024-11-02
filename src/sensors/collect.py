import random


def generate_random_temperature_value() -> float:
    """Generates random temperature value.

    Returns:
        float: Temperature in degree celsius.
    """
    return random.uniform(20, 60)
