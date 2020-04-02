# standard imports
import pytest

from datetime import datetime

# custom imports
from utils.validation import assert_date_range, get_slice
from return_calculator.data import read_cdi_quota, read_fund_quota


@pytest.fixture()
def fund():
    return read_fund_quota()


@pytest.fixture()
def cdi():
    return read_cdi_quota()



def test_assert_date_range_pass():
    # function parameters
    str_start_date = '2020-01-01'
    str_end_date = '2020-01-06'

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
    str_start_date = '2020-01-06'
    str_end_date = '2020-01-01'

    # catch error
    with pytest.raises(Exception):
        assert_date_range(str_start_date, str_end_date)


def test_get_slice_pass(fund, cdi):
    # function parameters
    start_date = '2020-01-01'
    end_date = '2020-01-06'

    # call function
    fund_sliced = get_slice(start_date, end_date, fund)
    cdi_sliced = get_slice(start_date, end_date, fund)

    # validate output
    assert 3 == len(fund_sliced)
    assert 3 == len(cdi_sliced)


def test_get_slice_no_data(fund):
    # function parameters
    start_date = '2020-01-04'
    end_date = '2020-01-05'

    # catch error
    with pytest.raises(Exception):
        get_slice(start_date, end_date, fund)


def test_get_slice_one_data_point(fund):
    # function parameters
    start_date = '2020-01-04'
    end_date = '2020-01-06'

    # catch error
    with pytest.raises(Exception):
        get_slice(start_date, end_date, fund)
