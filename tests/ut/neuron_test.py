import mock
import pytest
from unittest import TestCase

from xProject import Neuron

@pytest.mark.describe('Unit testing of Neuron class')
class NeuronTest(TestCase):
    """
        Unit tests the Neuron class in isolation, meaning
        that all members functions will be tested using Mock object for any
        dependcies .. opertions and ...s
    """

    @pytest.mark.describe('test title1')
    def test_construction_of_dummy_neuron(self):
        """
        Tests Construscts of Neuron Object
        a ... of ... and.

        Checks:
            - whether valid 

        Args:
            - None

        Return:
            - None

        """
        neuron = Neuron.Neuron(0.1)

    @mock.patch('xProject.Neuron.Neuron.squash')
    def test_calculating_the_output(self,mock_squash):
        """
        Tests behavior of ouput value calculation
        Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
        the output should be  total += self.inputs[i] * self.weights[i]

        Mocks:
            - Squash()

        Inputs:
            - None

        Epected:
            - calculate_output to be 1
            - sqush member to be called
            
        """
        mock_squash.return_value = 1
        neuron = Neuron.Neuron(0.1)
        neuron.weights = [0.2, 0.4, 0.1]
        inputs = [ 1, 1, 5 ]
        assert neuron.calculate_output(inputs) == 1 
        mock_squash.assert_called()


    def test_consistency_of_squash_function(self):
        """
        Tests behavior of squash function
        Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
        the output should be  total += self.inputs[i] * self.weights[i]

        Inputs:
            - total_net_input

        Epected:
            - squash return value to be 1 / (1 + math.exp(-total_net_input))

        """

        input_val = 0.9
        neuron = Neuron.Neuron(0.1)
        assert neuron.squash(input_val) < 1
        assert neuron.squash(input_val) > 0

    def test_is_error_detection_valid(self):
        """
        Tests behavior of error detection
        Given currnet target output o1 , and current output o2 ,
        The error function... :  return 0.5 * (target_output - self.output) ** 2

        Inputs:
            - o1: 0.2 
            - o2: 0.5 

        Expected:
            - Return value 1

        """

        o1 = 0.2
        o2 = 0.3
        neuron = Neuron.Neuron(0.1)
        neuron.output = o1
        assert neuron.calculate_error(o2) < 1

