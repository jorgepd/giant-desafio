# standard imports
import pandas as pd
import os

# custom imports
from app import logger

mypath = os.path.dirname(__file__)


def read_fund_quota():
    """
    Read and parse fund data
    """
    logger.info('read_fund_quota')

    # read
    path = os.path.join(mypath, '../zarathustra.csv')
    quota = pd.read_csv(path)

    # set index
    quota['data'] = pd.to_datetime(quota['data'])
    quota = quota.set_index('data')
    return quota


def read_cdi_quota():
    """
    Read and parse CDI data
    """
    logger.info('read_cdi_quota')

    # read
    path = os.path.join(mypath, '../cdi.csv')
    cdi = pd.read_csv(path)

    # set index
    cdi['date'] = pd.to_datetime(cdi['date'])
    cdi = cdi.set_index('date')

    # format
    cdi['variação diária'] = cdi['variação diária'].str.rstrip('%').astype(float)
    cdi['variação diária'] = cdi['variação diária'] / 100
    return cdi