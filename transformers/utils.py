"""
A set of utility functions associated with feature engineering.
"""

from functools import reduce
import typing as t
import numpy as np
import pandas as pd


def get_names(pipeline_name):
    """Get variable names from an sklearn Pipeline
    """
    last_step = pipeline_name.steps[-1][0]
    return pipeline_name.named_steps[last_step].get_feature_names()


def get_feature_names(stages):
    """Get all variables names from a list of Pipelines
    """
    stages_names = [pipeline for name, pipeline in stages]

    #Reverse order since using reduce functio
    stages_names.reverse()

    feature_names = reduce(lambda acc, x: get_names(x) + acc, stages_names, [])

    return feature_names


def dataframe_from_pipeline(array, stages, dtypes):
    """Create a DataFrame from a transformed Pipeline
    """

    feature_names = get_feature_names(stages)

    df = pd.DataFrame(array, columns=feature_names)
    df = df.astype(dtypes)
    return df


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