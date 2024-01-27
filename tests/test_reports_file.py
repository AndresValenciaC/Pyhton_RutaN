import glob
import logging
import os

import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
reports_file = os.path.join(current_dir, '..', 'proyecto_final', 'DEVICES', 'reports.py')
LOG_DIR = os.path.join(current_dir, '..', 'proyecto_final', 'DEVICES', 'REPORTS')

@pytest.fixture
def sample_data():
    return [
        {'Mission': 'Unknown', 'Device Type': 'Unknown', 'Device Status': 'unknown'},
        {'Mission': 'CLNM', 'Device Type': 'Space_vehicle', 'Device Status': 'excellent'},

    ]

def test_log_file_content(caplog):

    log_file_path = os.path.join(LOG_DIR, "APLSTATS*.log")
    logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(message)s')

    os.system(f'python {reports_file}')

    captured = caplog.text
    print(f"captured {captured}")

    matching_files = glob.glob(log_file_path)
    print(f"matching_files {matching_files}")

    assert matching_files


