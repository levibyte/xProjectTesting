import mock
import pytest
from unittest import TestCase
from pytest_testrail.plugin import testrail

from xProject import Neuron

@pytest.mark.describe('Unit testing of Neuron class')
class NeuronTest(TestCase):
    """
        Unit tests the Neuron class in isolation, meaning
        that all members functions will be tested using Mock object for any
        dependcies .. opertions and ...s
    """

    @testrail('C51')
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
