import pandas as pd
from sklearn.pipeline import make_pipeline

from transformers.strings import TokenRemover


def test_TokenRemover():

    data = {'col_1': ['Cisco corporation',  ' Corporation of Cisco', 'Cisco Corporation   of America  Corporation '],
            'col_2': ['Assoc of Homeowners', 'Homeowners Assoc of Assoc', 'Assoc Home   assoc ']}

    data_expected = {'col_1': ['Cisco corporation',  ' Corporation of Cisco', 'Cisco Corporation   of America  Corporation '],
                     'col_2': ['Assoc of Homeowners', 'Homeowners Assoc of Assoc', 'Assoc Home   assoc '],
        
                     'col_1_tk_removed': ['Cisco',  'of Cisco', 'Cisco of America'],
                     'col_2_tk_removed': ['of Homeowners', 'Homeowners of', 'Home']}

    df = pd.DataFrame(data)
    df_expected = pd.DataFrame(data_expected)

    tokens_to_remove = ['Corporation', 'Assoc']

    transformation = make_pipeline(TokenRemover(tokens_to_remove = tokens_to_remove))

    result = transformation.fit_transform(df)
    
    assert result.equals(df_expected)