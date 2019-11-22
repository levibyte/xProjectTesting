import mock
import pytest
from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import Neuron


@testrail('C51')
def test_construction_of_dummy_neuron():
	"""
	Tests construction of Neuron Object
	checks that bias and weights have expected values

	Args:
		- None

	Expected:
		- Weights should be uninitilaizd
		- Bias should be unchanged

	"""
	neuron = Neuron.Neuron(0.1)
	assert neuron.bias == 0.1
	assert neuron.weights == []
	
	

@testrail('C62')
@mock.patch('xProject.Neuron.Neuron.squash')
def test_calculating_the_output(mock_squash):
	"""
	Tests the behavior of ouput value calculation
	Given input i, the return value o should be calculated as follows
	o = squash(i)
	
	Mocks:
		- Neuron.Squash() => always returns 1

	Inputs:
		- [ 1, 1, 5 ]

	Epected:
		- Neuron.calculate_output() returns 1 
		- Neuron.squash() should be called
		
	"""
	mock_squash.return_value = 1
	neuron = Neuron.Neuron(0.1)
	neuron.weights = [0.2, 0.4, 0.1]
	inputs = [ 1, 1, 5 ]
	assert neuron.calculate_output(inputs) == 1 
	mock_squash.assert_called()

@testrail('C72')
def test_calculating_total_net_input():
	"""
	Tests behavior of Neuron.calculate_total_net_input() function
	Given input i1, i2, i3 , weights w1, w2, w2 and bias "B" 
	the output should be  total += .inputs[i] * .weights[i]

	Inputs:
		- neuron.weights = [0.2, 0.4, 0.1]
		- neuron.inputs = [ 1, 1, 5 ]

	Epected:
		- the output value should be beetween 1.1><1.3
		
	"""
	neuron = Neuron.Neuron(0.1)
	neuron.weights = [0.2, 0.4, 0.1]
	neuron.inputs = [ 1, 1, 5 ]
	assert neuron.calculate_total_net_input() > 1.1
	assert neuron.calculate_total_net_input() < 1.3
	

@testrail('C63')
@pytest.mark.parametrize("i,exp_range_begin,exp_range_end",[
    (0.9,0.6,0.8),
    (1.9,0.2,0.9),
    (-0.9,0.1,0.8)],
)
def test_consistency_of_squash_function(i,exp_range_begin,exp_range_end):
	"""
	Tests behavior of Neuron.squash() function
	the expected return value of function should be according following formula
	res = 1 / (1 + e^(-i))

	Inputs:
		- case1 : 0.9
		- case2 : -0.9
		- case3 : 1.9

	Epected:
		- case1 : a < return value < b
		- case2 : a < return value < b
		- case3 : a < return value < b
		
	"""

	input_val = i
	neuron = Neuron.Neuron(0.1)
	assert neuron.squash(input_val) < exp_range_end
	assert neuron.squash(input_val) > exp_range_begin

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

