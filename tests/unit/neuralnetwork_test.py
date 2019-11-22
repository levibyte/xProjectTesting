import mock
from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import NeuralNetwork
from xProject import Neuron
from xProject import NeuronLayer

#class NeuralNetworkTest(TestCase):

@testrail('C68')
def test_creating_simple_neural_network_with_5_hidden_layers():
	"""
	Tests behavior of NeuralNetwork "calculate_total_error" function.
	Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
	the output should be  total += .inputs[i] * .weights[i]

	Inputs:
		- Vector of 2 bits

	Epected:
		- Error should be less then 1%

	"""
	training_sets = [
			[[0, 0], [0]],
			[[0, 1], [1]],
			[[1, 0], [1]],
			[[1, 1], [0]]
		]
	nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
	nn.calculate_total_error(training_sets)

@testrail('C69')
def test_valid_behavior_of_train_function():
	pass


@testrail('C70')
def test_calculating_total_error():
	pass

