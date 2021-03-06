from datetime import datetime
import math
import numpy as np


def mpc_chris(input_int):
    # Compute the square root of the input
    square_root = math.sqrt(input_int)

    # Return a nice string for Flask to display with the square root result.
    return f"The square root of <b>{input_int}</b> is {square_root}"


def mpc_federica(input_int):
    #Compute class 2 of the input
    mod = input_int % 2
    return  f"The base 2 of <b>{input_int}</b> is {mod}"


def mpc_dave(input_int):
    return 0


def mpc_peter(input_int):
    return 0


def mpc_paresh(input_int):

    # Exponential
    exp = math.exp(input_int)
    # Return a nice string for Flask to display with the square root result.
    return f"The exponential of <b>{input_int}</b> is {exp}"

def mpc_matt(input_int):
    # return the square of the input.
    return f"{input_int}^2=", np.asarray(input_int)**2


def mpc_rosemary(input_int):
    # return 10**random value
    val=10**input_int
    return f"10^<b>{input_int}</b> is {val}"


def mpc_mikea(input_int):
    # Compute the semi-major axis of the N:1 resonance with Neptune
    period = (30.07 ** 1.5) * (input_int * 1./1)
    semi_major_axis = period ** (2. / 3)
    return (f"The {input_int}:1 Mean-Motion-Resonance with "
            f"Neptune is at {semi_major_axis:6.2f} au.")


def mpc_mike_r(input_int):
    return 0


def mpc_margaret(input_int):

    # fake addition
    double = str(input_int)*2
    
    return f"{input_int} + {input_int} = "+double


def mpc_n(input_int):
    # normalize to color range
    factor = 360/10
    normalized = int(input_int*factor)

    # Return a nice div for Flask to display with the result as a color.
    return f"<div style=\"background-color: hsl({normalized}, 100%, 50%); padding: 1em; " \
           f"width: 10%; margin-left: 5%; text-align: center; font-size: 2rem;\">" \
           f"{input_int}</div>"
