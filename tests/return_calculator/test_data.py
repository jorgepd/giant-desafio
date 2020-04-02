# standard imports
import pandas as pd

# custom imports
from return_calculator.data import read_cdi_quota, read_fund_quota


def test_read_cdi_quota_pass():
    # call function
    output = read_cdi_quota()

    # validate output
    true_output = [10.22, 9.53, 9.51, 9.48, 9.46]
    assert output['taxa anualizada'].head().to_list() == true_output


def test_read_fund_quota_pass():
    # call function
    output = read_fund_quota()

    # validate output
    true_output = [1.0, 1.0003475, 1.0006704, 1.0012742, 1.0052404]
    assert output['cota'].head().to_list() == true_output
