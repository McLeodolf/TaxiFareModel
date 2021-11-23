from TaxiFareModel.trainer import Trainer

def test_trainer():
    trainer = Trainer()
    assert isinstance(trainer, Trainer())
