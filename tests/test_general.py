"""
pip install mypy
mypy transformers/ --config-file ./transformers/mypy.ini
"""

import typing as t

import pytest
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline, FeatureUnion, Pipeline

from fake_data import random_categorical, random_integer, random_float
from src.general import (DataFrameSelector, NumpyConverter, GetDummies,
                    CategoricalEncoder)


def test_DataFrameSelector() -> None:

    rows = 5

    data = {'a': random_categorical(['x', 'y', 'z'], rows),
            'b': random_categorical(['h', 'i', 'j'], rows),
            'c': random_integer(0, 5, rows)}

    df = pd.DataFrame(data)

    transformation = make_pipeline(DataFrameSelector(['a', 'b']))

    result = transformation.fit_transform(df)
    expected = df[['a', 'b']]
    
    assert result.equals(expected)


    






