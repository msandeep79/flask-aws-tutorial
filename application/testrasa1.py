from rasa_nlu.interpreters.spacy_sklearn_interpreter import SpacySklearnInterpreter
from rasa_nlu.model import Metadata
import spacy
import os




class nlpClass:
    class __nlpClass:
        def __init__(self):
	    	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	    	modelpath = os.path.join(__location__, 'model_20170417-171745')
	    	self.metadata = Metadata.load(modelpath)
	    	self.nlp = spacy.load("en")
	    	self.interpreter = SpacySklearnInterpreter.load(self.metadata, nlp=self.nlp)
	    	self.interpreter_loaded = True
        def __str__(self):
            return repr(self)

        def text2NLP(self,txt):
        	print txt
        	return self.interpreter.parse(txt)

    instance = None

    def __init__(self):
        if not nlpClass.instance:
            nlpClass.instance = nlpClass.__nlpClass()
        else:
            pass
    def __getattr__(self, name):
        return getattr(self.instance, name)




	#print interpreter.parse(u"i m looking for a place in the north of town")
	#Look for an A-Class Diesel






if __name__ == '__main__':
	nlcl = nlpClass()
	print nlcl.text2NLP(u"Look C200 CDI")

	print nlcl.text2NLP(u"Look C200 CDI")
    

