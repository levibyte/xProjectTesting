import mock
import pytest
from unittest import TestCase

from xProject import Neuron

@pytest.mark.describe('Unit testing of Neuron class ')
class NeuronTest(TestCase):
    """
        Class Unit tests the Neuron class in isolation, meaning
        that all ... used as Mock object to complete certain
        .. opertions and ...s
    """
    
    def test_construction(self):    
        """
        Tests construction of Neuron Object
        
        Checks: 
            whether valid 
        
        Args: 
            None
        
        Return: 
            None
        """
        neuron = Neuron.Neuron(0.1)

    @mock.patch('xProject.Neuron.Neuron.squash')
    def test_calculate_output(self,mock_squash):    
        mock_squash.return_value = 1
        #neuron = Neuron.Neuron(0.1)
        #neuron.weights = [0.2, 0.4, 0.1]
        #inputs = [ 1, 1, 5 ]
        #print(neuron.calculate_output(inputs))
        #mock_squash.assert_called()

    
