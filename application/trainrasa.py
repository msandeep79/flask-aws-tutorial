import spacy
from rasa_nlu.training_data import TrainingData
from rasa_nlu.trainers.spacy_sklearn_trainer import SpacySklearnTrainer

nlp = spacy.load("en")
training_data = TrainingData('demo-rasa.json', 'spacy_sklearn', nlp)
trainer = SpacySklearnTrainer('en')
trainer.train(training_data)
trainer.persist('./')