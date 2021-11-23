from TaxiFareModel.trainer import Trainer
from TaxiFareModel.data import get_data, clean_data
import pandas as pd

def test_trainer():
    df = clean_data(get_data())
    y = df.pop("fare_amount")
    X = df
    assert isinstance(df, pd.DataFrame)
    trainer = Trainer(X,y)
    assert isinstance(trainer, Trainer)
