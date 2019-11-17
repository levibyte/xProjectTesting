import mock
from unittest import TestCase

#from xProject import Neuron

class NeuronTest(TestCase):
    
    def test1(self):
        pass    
    #def test_construction(self):    
    #    neuron = Neuron.Neuron(0.1)

    @mock.patch('xProject.Neuron.Neuron.squash')
    def test_calculate_output(self,mock_squash):    
        mock_squash.return_value = 1
        #neuron = Neuron.Neuron(0.1)
        #neuron.weights = [0.2, 0.4, 0.1]
        #inputs = [ 1, 1, 5 ]
        #print(neuron.calculate_output(inputs))
        #mock_squash.assert_called()

    
