import random
import mock
#from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import NeuralNetwork
from xProject import Neuron
from xProject import NeuronLayer

#class AIBooleanPredictionTest(TestCase):

@testrail('C52')
def test_ai_can_predict_the_or_operation():
	"""
	System/behavior testing of NeuralNetwork predicting
	the behavior of two bit OR operation. 

	Inputs:
		- [0, 0] -> 0
		- [0, 1] -> 1
		- [1, 0] -> 1

	Epected:
		- [1, 1] => 1
		
	"""

	training_sets = [
		[[0, 0], [0]],
		[[0, 1], [1]],
		[[1, 0], [1]]
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
	for i in range(10000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([1,1])[0] > 0.9
	#print ("Predication OR when [1,1] --> {}".format(nn.feed_forward([1,1])))

@testrail('C53')
def test_ai_can_predict_the_xor_operation():
	training_sets = [
		[[0, 0], [0]],
		[[0, 1], [1]],
		[[1, 1], [0]]
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
	for i in range(10000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([1,0])[0] < 0.1
	#print ("Predication XOR when [1,0] --> {}".format(nn.feed_forward([1,0])))

@testrail('C54')
def test_ai_can_predict_the_and_operation():
	training_sets = [
		[[0, 0], [0]],
		[[1, 0], [0]],
		[[1, 1], [1]]
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 4, len(training_sets[0][1]))
	for i in range(1000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([0,1])[0] > 0.1
	#print ("Predication AND when [1,0] --> {}".format(nn.feed_forward([0,1])))

@testrail('C56')
def test_ai_can_predict_the_or_operation_on_3_inputs():
	training_sets = [
		[[0, 0, 0], [0]],
		[[0, 0, 1], [1]],
		[[0, 1, 0], [1]],
		[[1, 0, 0], [1]],
		[[1, 0, 1], [1]],
		[[1, 1, 1], [1]],
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
	for i in range(10000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([0,1,1])[0] > 0.9
	assert nn.feed_forward([1,0,0])[0] > 0.9
	#print ("Predication OR when [1,1] --> {}".format(nn.feed_forward([1,1])))

@testrail('C57')
def test_ai_can_predict_the_sum_operation_on_3_bits():
	training_sets = [
		[[0, 0, 0], [0, 0, 1]],
		[[0, 0, 1], [0, 1, 0]],
		#[[0, 1, 0], [0, 1, 1]],
		[[0, 1, 1], [1, 0, 0]],
		[[1, 0, 0], [1, 0, 1]],
		[[1, 0, 1], [1, 1, 0]],
		[[1, 1, 0], [1, 1, 1]],
		[[1, 1, 1], [0, 0, 0]],
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 3, len(training_sets[0][1]))
	for i in range(100000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([0,1,1])[0] > 0.9
	assert nn.feed_forward([0,1,1])[1] > 0.9
	assert nn.feed_forward([0,1,1])[2] > 0.9
	
	#assert nn.feed_forward([1,0,0])[0] > 0.9
	#print ("Predication SUM when input is [0,1,0] --> {}".format(nn.feed_forward([0,1,0])))

@testrail('C58')
def test_ai_can_predict_the_or_operation_on_3bits():
	training_sets = [
		[[0, 0], [0]],
		[[0, 1], [1]],
		[[1, 0], [1]]
	]
	
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
	for i in range(10000):
		training_inputs, training_outputs = random.choice(training_sets)
		nn.train(training_inputs, training_outputs)
	
	assert nn.feed_forward([1,1])[0] > 0.9
	#print ("Predication OR when [1,1] --> {}".format(nn.feed_forward([1,1])))
