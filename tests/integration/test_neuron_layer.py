import mock
import pytest
from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import NeuronLayer

@pytest.mark.describe('Intergation testing of NeuronLayer class')
class ITNeuronLayerTest(TestCase):
    """
        Integration testing of NeuronLayer class with depency
        on real Neuron NeuronNetwork classes 
    """

    @testrail('C51')
    def test_feeding_layer(self):
        """
        Tests behavior of ouput value calculation
        Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
        the output should be  total += self.inputs[i] * self.weights[i]

        Inputs:
            - None

        Epected:
            - calculate_output to be 1
            - sqush member to be called
 
        """
        nl = NeuronLayer.NeuronLayer(4,0.1)
        inputs = [ 0.1, 0.1, 0.5, 0.6 ]
        #nl.feed_forward(inputs)
        #assert nl.feed_forward(inputs) != 0

