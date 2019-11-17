import mock
from unittest import TestCase

from xProject import NeuralNetwork
from xProject import Neuron
from xProject import NeuronLayer

class NeuralNetworkTest(TestCase):
    
    def test_calculate_total_error(self):    
        training_sets = [
             [[0, 0], [0]],
             [[0, 1], [1]],
             [[1, 0], [1]],
             [[1, 1], [0]]
        ]   
        #nn = NeuralNetwork.NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
        #nn.calculate_total_error(training_sets)
