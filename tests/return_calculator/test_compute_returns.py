# standard imports
import pytest

from datetime import datetime

# custom imports
from return_calculator.compute_returns import absolute_return, relative_return,\
    biggest_return, smallest_return, cummulative_returns, equity_evolution


def test_absolute_return_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    output = absolute_return(start_date, end_date)

    # validate output
    true_output = -1.4981
    assert (output - true_output) < 0.0001


def test_relative_return_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    output = relative_return(start_date, end_date)

    # validate output
    true_output = -1.7915
    assert (output - true_output) < 0.0001


def test_biggest_return_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    out_date, out_ret = biggest_return(start_date, end_date)

    # validate outputs
    true_output = datetime.strptime('2012-03-13', '%Y-%m-%d')
    assert out_date == true_output
    true_output = 0.3961
    assert (out_ret - true_output) < 0.0001


def test_smallest_return_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    out_date, out_ret = smallest_return(start_date, end_date)

    # validate outputs
    true_output = datetime.strptime('2012-03-15', '%Y-%m-%d')
    assert out_date == true_output
    true_output = -1.8402
    assert (out_ret - true_output) < 0.0001


def test_cummulative_returns_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    output = cummulative_returns(start_date, end_date)

    # validate output
    true_output = [0.0347, 0.0670, 0.1274, 0.5240, 0.6390, -1.2130, -1.4981]
    for i in range(len(output)):
        assert (output[i] - true_output[i]) < 0.0001


def test_equity_evolution_pass():
    # function parameters
    start_date = '2012-03-07'
    end_date = '2012-03-17'

    # call function
    output = equity_evolution(start_date, end_date)

    # validate output
    true_output = 2218743.06
    assert output == true_output
