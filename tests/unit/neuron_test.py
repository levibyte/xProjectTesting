import mock
import pytest
from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import Neuron


@testrail('C51')
def test_construction_of_dummy_neuron():
	"""
	Tests construction of Neuron Object

	Args:
		- None

	Return:
		- None

	"""
	neuron = Neuron.Neuron(0.1)

@testrail('C62')
@mock.patch('xProject.Neuron.Neuron.squash')
def test_calculating_the_output(mock_squash):
	"""
	Tests behavior of ouput value calculation
	Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
	the output should be  total += .inputs[i] * .weights[i]

	Mocks:
		- Neuron.Squash()

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

@testrail('C63')
def test_consistency_of_squash_function():
	"""
	Tests behavior of squash function
	Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
	the output should be  total += .inputs[i] * .weights[i]

	Inputs:
		- total_net_input

	Epected:
		- squash return value to be 1 / (1 + math.exp(-total_net_input))

	"""

	input_val = 0.9
	neuron = Neuron.Neuron(0.1)
	assert neuron.squash(input_val) < 1
	assert neuron.squash(input_val) > 0

@testrail('C64')
@pytest.mark.parametrize("o1,o2,expected",[
    (0.1,0.2,0.3),
    (0.2,0.2,0.1)],
)
def test_the_error_detection_is_valid(o1,o2,expected):
    """
    Tests behavior of Neuron error detection function
    Given currnet target output o1 , and current output o2 ,
    The error function should calculate and return the difference
    Via following formulat: 0.5 * (o1 - o2) ** 2
		
    Inputs:
		- case1 : o1 = 0.1  o2 = 0.2 
		- case2 : o1 = 0.2  o2 = 0.2 

    Expected:
		- case1 : return_val < 1
		- case2 : return_val < 1
	
    """

    neuron = Neuron.Neuron(0.1)
    neuron.output = o1
    assert neuron.calculate_error(o2) < expected

