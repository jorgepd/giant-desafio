# standard imports
from flask_apispec import doc

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
    return cr.absolute_return(start_date, end_date)


@return_calculator_api.route('/return/relative/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute relative return')
def _relative_return(start_date, end_date):
    logger.info('_relative_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    return cr.relative_return(start_date, end_date)


@return_calculator_api.route('/return/biggest/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute biggest return')
def _biggest_return(start_date, end_date):
    logger.info('_biggest_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    return cr.biggest_return(start_date, end_date)


@return_calculator_api.route('/return/smallest/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute smallest return')
def _smallest_return(start_date, end_date):
    logger.info('_smallest_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    return cr.smallest_return(start_date, end_date)


@return_calculator_api.route('/return/cummulative/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute cummulative return')
def _cummulative_return(start_date, end_date):
    logger.info('_cummulative_return endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    return cr.cummulative_return(start_date, end_date)


@return_calculator_api.route('/equity/evolution/<string:start_date>&<string:end_date>', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Return Calculator'], description='Compute equity evolution')
def _equity_evolution(start_date, end_date):
    logger.info('_equity_evolution endpoint')

    # validate inputs
    start_date, end_date = assert_date_range(start_date, end_date)

    # call appropriate function
    return cr.equity_evolution(start_date, end_date)


