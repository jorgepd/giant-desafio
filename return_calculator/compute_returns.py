# standard imports
# import pandas as pd

# custom imports
from return_calculator.data import read_cdi_quota, read_fund_quota
from return_calculator.utils import assert_date_range


def absolute_profitability(start_date, end_date):
    """
    Compute fund's absolute profitability in percentage form over a
    specified period
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute returns
    abs_ret = df['cota'].pct_change().add(1).cumprod()[-1]
    abs_ret = (abs_ret - 1) * 100
    return '{:.4f}%'.format(abs_ret)


def relative_profitability(start_date, end_date):
    """
    Compute fund's relative profitability compared to the CDI in
    percentage form over a specified period
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()
    cdi = read_cdi_quota()

    # get data slice
    target = fund.loc[start_date:end_date]
    benchmark = cdi.loc[start_date:end_date]

    # take diff
    target_returns = target['cota'].pct_change()
    benchmark_returns = benchmark['variação diária']
    diff = target_returns - benchmark_returns

    # compute real returns
    real_ret = diff.add(1).cumprod()[-1]
    real_ret = (real_ret - 1) * 100
    return '{:.4f}%'.format(real_ret)


def equity_evolution(start_date, end_date):
    """
    Compute fund's equity evolution in BRL over a specified period
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute equity diff
    diff = df['pl'][-1] - df['pl'][0]
    return 'R$ {:,.2f}'.format(diff)


def biggest_returns(start_date, end_date):
    """
    Find fund's biggest daily return over a specified period. Return
    its value in percentage form, alongside the respective date in
    which it occurred
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute returns
    abs_ret = df['cota'].pct_change()
    max_ret = abs_ret.max()

    # locate date index
    date = df[df == max_ret].index[0]

    return date.strftime('%Y-%m-%d'), '{:.4f}%'.format(max_ret)


def smallest_returns(start_date, end_date):
    """
    Find fund's smallest daily return over a specified period. Return
    its value in percentage form, alongside the respective date in
    which it occurred
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute returns
    abs_ret = df['cota'].pct_change()
    min_ret = abs_ret.min()

    # locate date index
    date = df[df == min_ret].index[0]

    return date.strftime('%Y-%m-%d'), '{:.4f}%'.format(min_ret)


def cummulative_returns(start_date, end_date):
    """
    Given a specified period, return a series of the fund's cummulative
    returns
    """

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute returns
    cum_ret = df['cota'].pct_change().add(1).cumprod()

    # fix first element
    cum_ret = cum_ret.replace(float('nan'), 1)

    # format number into percent string
    cum_ret = cum_ret.add(-1) * 100
    return cum_ret.map('{:.4f}%'.format)
