import math
from testrasa1 import 	nlpClass
	

def compute(r):
    return math.sin(r)

def getNLP(txt):

	nlcl = nlpClass()
	#print nlcl.text2NLP(u"Find for an A-Class Diesel")

	return nlcl.text2NLP(txt)