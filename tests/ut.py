from src.models import time_stamp, start_analysis
from fastapi.exceptions import HTTPException
import re


def test_timestamp_is_int():
    ts = time_stamp()
    assert type(ts) is int


def test_timestamp_match():
    ts = time_stamp()
    epoch_regex = re.compile(r'^[0-9]+$')
    assert epoch_regex.match(str(ts))


def test_start_analysis_invalid_scanner_name():
    try:
        start_analysis('https://github.com/manola/ruby-project', 'bandit',
                       'Ruby')
    except HTTPException as e:
        assert e.detail == 'Scanner not available'
