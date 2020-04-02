# standard imports
from flask import Response

# custom imports
from return_calculator.data import read_cdi_quota, read_fund_quota
from utils.validation import assert_date_range

from app import logger


def absolute_return(start_date, end_date):
    """
    Compute fund's absolute profitability in percentage form over a
    specified period
    """
    logger.info('absolute_return')

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute return
    abs_ret = df['cota'].pct_change().add(1).cumprod()[-1]
    abs_ret = (abs_ret - 1) * 100

    return '{:.4f}%'.format(abs_ret)


def relative_return(start_date, end_date):
    """
    Compute fund's relative profitability compared to the CDI in
    percentage form over a specified period
    """
    logger.info('relative_return')

    # read data
    fund = read_fund_quota()
    cdi = read_cdi_quota()

    # get data slice
    target = fund.loc[start_date:end_date]
    benchmark = cdi.loc[start_date:end_date]

    # take diff
    target_return = target['cota'].pct_change()
    benchmark_return = benchmark['variação diária']
    diff = target_return - benchmark_return

    # compute real return
    real_ret = diff.add(1).cumprod()[-1]
    real_ret = (real_ret - 1) * 100

    return '{:.4f}%'.format(real_ret)


def biggest_return(start_date, end_date):
    """
    Find fund's biggest daily return over a specified period. Return
    its value in percentage form, alongside the respective date in
    which it occurred
    """
    logger.info('biggest_return')

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute return
    abs_ret = df['cota'].pct_change()
    max_ret = abs_ret.max()

    # locate date index
    date = abs_ret[abs_ret == max_ret].index[0]

    return date.strftime('%Y-%m-%d') + ', ' + '{:.4f}%'.format(max_ret * 100)


def smallest_return(start_date, end_date):
    """
    Find fund's smallest daily return over a specified period. Return
    its value in percentage form, alongside the respective date in
    which it occurred
    """
    logger.info('smallest_return')

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute return
    abs_ret = df['cota'].pct_change()
    min_ret = abs_ret.min()

    # locate date index
    date = abs_ret[abs_ret == min_ret].index[0]

    return date.strftime('%Y-%m-%d') + ', ' + '{:.4f}%'.format(min_ret * 100)


def cummulative_return(start_date, end_date):
    """
    Given a specified period, return a series of the fund's cummulative
    return
    """
    logger.info('cummulative_return')

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute absolute return
    cum_ret = df['cota'].pct_change().add(1).cumprod()

    # format number into percent string
    cum_ret = cum_ret.add(-1) * 100
    series = cum_ret.map('{:.4f}%'.format)[1:]

    return Response(series.to_string())


def equity_evolution(start_date, end_date):
    """
    Compute fund's equity evolution in BRL over a specified period
    """
    logger.info('equity_evolution')

    # read data
    fund = read_fund_quota()

    # get data slice
    df = fund.loc[start_date:end_date]

    # compute equity diff
    diff = df['pl'][-1] - df['pl'][0]

    return 'R$ {:,.2f}'.format(diff)
