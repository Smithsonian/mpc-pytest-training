from datetime import datetime
import math


def mpc_chris(input_int):
    # Compute the square root of the input
    square_root = math.sqrt(input_int)

    # Return a nice string for Flask to display with the square root result.
    return f"The square root of <b>{input_int}</b> is {square_root}"


def mpc_federica(input_int):
    return 0


def mpc_dave(input_int):
    return 0


def mpc_peter(input_int):
    return 0


def mpc_paresh(input_int):
    return 0


def mpc_matt(input_int):
    return 0


def mpc_rosemary(input_int):
    return 0


def mpc_mikea(input_int):
    # Compute the semi-major axis of the N:1 resonance with Neptune
    period = (30.07 ** 1.5) * (input_int * 1./1)
    semi_major_axis = period ** (2. / 3)
    return (f"The {input_int}:1 Mean-Motion-Resonance with "
            f"Neptune is at {semi_major_axis:6.2f} au.")


def mpc_mike_r(input_int):
    return 0


def mpc_margaret(input_int):
    return 0


def mpc_n(input_int):
    return 0
