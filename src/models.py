from asyncio import subprocess
from mimetypes import init
from sqlite3 import Timestamp
import time
import subprocess
from pathlib import Path
import datetime
import os
import json
import shutil
from fastapi import HTTPException

scan_path = 'scan-path'
brakeman_scanner_path = 'brakeman'
scanners_list = {'brakeman': ['ruby']}


# Function to generate epoch timestamp
def time_stamp():
    time = datetime.datetime.now().timestamp()
    return int(time)


# Decorator to validate request payload
def validate_scan_request(func):

    def inner(source_code_url, scanner_name, language):

        if scanner_name.lower() in scanners_list:
            if language.lower() not in scanners_list[scanner_name.lower()]:
                raise HTTPException(status_code=404,
                                    detail="Language not supported by Scanner")

        else:
            raise HTTPException(status_code=404,
                                detail="Scanner not available")

        # I kept it simple, a regex to validate the url will be a proper implemenation,
        if 'http' not in source_code_url:
            raise HTTPException(status_code=400, detail="Not a valid Gitrepo")
        return func(source_code_url, scanner_name, language)

    return inner


# Start scan analysis
@validate_scan_request
def start_analysis(source_code_url, scanner_name, language):
    time = time_stamp()
    try:
        checkoutproject(source_code_url)
        cmd = f'{brakeman_scanner_path} -p {scan_path} -q -o brakeman-result-{time}.json . '
        cp = subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        raise e
    except Exception as e:
        raise e

    return time


# Checkout Project
def checkoutproject(source_code_url):
    cmd = f'cd {scan_path} && git clone {source_code_url} .'

    try:
        # remove previous repo
        remove_scan_path_forcefully()
        # create scan-path is not exits
        if not os.path.exists(scan_path):
            os.makedirs(scan_path, exist_ok=True)
        cp = subprocess.run(cmd, shell=True, check=True, timeout=60)

    except subprocess.TimeoutExpired as e:
        raise HTTPException(status_code=408,
                            detail="Git repo is wrong/private")
    except subprocess.CalledProcessError as e:
        raise e

    except Exception as e:
        raise e


def read_report(time_stamp):
    file_path = f'brakeman-result-{time_stamp}.json'
    if (os.path.exists(file_path)):
        data = open(file_path, 'r')
        return (json.loads(data.read()))
    else:
        raise HTTPException(status_code=404, detail="Report not found")


def remove_scan_path_forcefully():
    rm_cmd = f'rm -rf {scan_path}'
    try:
        if os.path.exists(scan_path):
            subprocess.run(rm_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        raise e
