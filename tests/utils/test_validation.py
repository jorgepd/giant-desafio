# standard imports
import pytest

from datetime import datetime

# custom imports
from utils.validation import assert_date_range


def test_assert_date_range_pass():
    # function parameters
    str_start_date = '2020-01-01'
    str_end_date = '2020-01-05'

    # call function
    start_date, end_date = assert_date_range(str_start_date, str_end_date)

    # validate output
    assert start_date == datetime.strptime(str_start_date, '%Y-%m-%d')
    assert end_date == datetime.strptime(str_end_date, '%Y-%m-%d')


def test_assert_date_range_error_invalid_date():
    # function parameters
    str_start_date = 'date'
    str_end_date = 'date'

    # catch error
    with pytest.raises(Exception):
        assert_date_range(str_start_date, str_end_date)


def test_assert_date_range_error_unordered_dates():
    # call function
    str_start_date = '2020-01-05'
    str_end_date = '2020-01-01'

    # catch error
    with pytest.raises(Exception):
        assert_date_range(str_start_date, str_end_date)
