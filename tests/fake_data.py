import typing as t
import numpy as np


def random_categorical(categoricals: t.List[str], length: int) -> t.List[str]:
    """Returns a list of randomly chosen elements from a list of strings
    (categorical values) of length, length
    """
    
    return [np.random.choice(categoricals) for i in range(length)]


def random_integer(low: int, high: int, length: int) -> t.List[int]:
    """Returns a list of randomly chosen integers between the 
    range of low and high. Returned list is length, length
    """
    
    return [np.random.randint(low, high) for i in range(length)]


def random_float(low: int, high: int, decimals: int, length: int) -> t.List[float]:
    """Returns a list of randomly chosen floating point numbers 
    between the range of low and high. Returned list is length, length
    """
    
    return [round(np.random.uniform(low, high), decimals) for i in range(length)]