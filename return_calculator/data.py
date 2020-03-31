# standard imports
import pandas as pd


def read_fund_quota():
    """
    Read and parse fund data
    """

    # read
    quota = pd.read_csv('zarathustra.csv')

    # set index
    quota['data'] = pd.to_datetime(quota['data'])
    quota = quota.set_index('data')
    return quota


def read_cdi_quota():
    """
    Read and parse CDI data
    """

    # read
    cdi = pd.read_csv('cdi.csv')

    # set index
    cdi['date'] = pd.to_datetime(cdi['date'])
    cdi = cdi.set_index('date')

    # format
    cdi['variação diária'] = cdi['variação diária'].str.rstrip('%').astype(float)
    cdi['variação diária'] = cdi['variação diária'] / 100
    return cdi