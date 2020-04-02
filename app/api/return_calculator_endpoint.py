# standard imports
from flask_apispec import doc
from flask import Response

# custom imports
from return_calculator import compute_returns as cr
from utils.validation import assert_date_range

from . import return_calculator_api
from app import logger


@return_calculator_api.route('/return/absolute/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute absolute return')
def _absolute_return(start_date, end_date):
    logger.info('_absolute_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    abs_ret = cr.absolute_return(start_date, end_date)

    # return parsed output
    response = '{:.4f}%'.format(abs_ret)
    return response


@return_calculator_api.route('/return/relative/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute relative return')
def _relative_return(start_date, end_date):
    logger.info('_relative_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    real_ret = cr.relative_return(start_date, end_date)

    # return parsed output
    response = '{:.4f}%'.format(real_ret)
    return response


@return_calculator_api.route('/return/biggest/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute biggest return')
def _biggest_return(start_date, end_date):
    logger.info('_biggest_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    date, max_ret = cr.biggest_return(start_date, end_date)

    # return parsed output
    response = date.strftime('%Y-%m-%d') + ', ' + '{:.4f}%'.format(max_ret)
    return response


@return_calculator_api.route('/return/smallest/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute smallest return')
def _smallest_return(start_date, end_date):
    logger.info('_smallest_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    date, min_ret = cr.smallest_return(start_date, end_date)

    # return parsed output
    response = date.strftime('%Y-%m-%d') + ', ' + '{:.4f}%'.format(min_ret)
    return response

@return_calculator_api.route('/return/cummulative/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute cummulative return')
def _cummulative_returns(start_date, end_date):
    logger.info('_cummulative_returns endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    series = cr.cummulative_returns(start_date, end_date)
    series = series.map('{:.4f}%'.format)

    # return parsed output
    response = Response(series.to_string())
    return response


@return_calculator_api.route('/equity/evolution/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute equity evolution')
def _equity_evolution(start_date, end_date):
    logger.info('_equity_evolution endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    diff = cr.equity_evolution(start_date, end_date)

    # return parsed output
    response = 'R$ {:,.2f}'.format(diff)
    return response
