# standard imports
from datetime import datetime


def assert_date_range(start_date, end_date):
    """
    Parameter validation function
    """

    # parse date input
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except Exception:
        raise Exception('Please enter a valid date! Date format is yyyy-mm-dd')

    # check date order
    if start_date >= end_date:
        raise Exception('end_date must be bigger than start_date')

    return start_date, end_date
