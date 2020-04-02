# standard imports
import pytest

from datetime import datetime

# custom imports
from app.api.return_calculator_endpoint import _absolute_return, _relative_return,\
    _biggest_return, _smallest_return, _cummulative_returns, _equity_evolution


def test_absolute_return_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _absolute_return(start_date, end_date)
        output = output.response

        # validate output
        true_output = [b'"-1.4981%"\n']
        assert output == true_output


def test_relative_return_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _relative_return(start_date, end_date)
        output = output.response

        # validate output
        true_output = [b'"-1.7915%"\n']
        assert output == true_output


def test_biggest_return_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _biggest_return(start_date, end_date)
        output = output.response

        # validate output
        true_output = [b'"2012-03-13, 0.3961%"\n']
        assert output == true_output


def test_smallest_return_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _smallest_return(start_date, end_date)
        output = output.response

        # validate output
        true_output = [b'"2012-03-15, -1.8402%"\n']
        assert output == true_output


def test_cummulative_returns_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _cummulative_returns(start_date, end_date)
        output = output.response
        test_app.logger.info(output)

        # validate output
        true_output = [b'data\n2012-03-08     0.0347%\n2012-03-09     0.0670%\n2012-03-12     0.1274%\n2012-03-13     0.5240%\n2012-03-14     0.6390%\n2012-03-15    -1.2130%\n2012-03-16    -1.4981%']
        assert output == true_output


def test_equity_evolution_endpoint_pass(test_app):
    with test_app.app_context():
        # function parameters
        start_date = '2012-03-07'
        end_date = '2012-03-17'

        # call function
        output = _equity_evolution(start_date, end_date)
        output = output.response

        # validate output
        true_output = [b'"R$ 2,218,743.06"\n']
        assert output == true_output
