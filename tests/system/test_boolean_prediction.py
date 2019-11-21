import random
import mock
from unittest import TestCase

from xProject import NeuralNetwork
from xProject import Neuron
from xProject import NeuronLayer

class AIBooleanPredictionTest(TestCase):

	def test_ai_can_predict_the_or_operation(self):
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


	def test_ai_can_predict_the_xor_operation(self):
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


	def test_ai_can_predict_the_and_operation(self):
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
