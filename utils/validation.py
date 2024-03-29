# standard imports
from datetime import datetime
from flask import abort

# custom imports
from app import logger


def assert_date_range(start_date, end_date):
    """
    Parameter validation function
    """
    logger.info('assert_date_range')

    # parse date input
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except Exception as e:
        logger.error('Please enter a valid date! Date format is yyyy-mm-dd')
        abort(400)

    # check date order
    if start_date >= end_date:
        logger.error('end_date must be bigger than start_date')
        abort(400)

    return start_date, end_date


def get_slice(start_date, end_date, df):
    # slice df
    sliced = df.loc[start_date: end_date]

    # no data
    if(len(sliced) <= 1):
        logger.error('There is no data between these 2 dates, try widening the range')
        abort(400)

    return sliced
