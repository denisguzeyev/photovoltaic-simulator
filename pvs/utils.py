import os
import datetime
import json
from pvs.config import Config

config = Config()

def get_report_dir():
    """Get folder for reports"""
    return os.path.join(config.REPORT_FOLDER,
                        datetime.datetime.today().strftime('%Y-%m-%d'))


def write_report(dict_to_write, total_value):
    """Write reports in file"""
    report_dir = get_report_dir()
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    now = datetime.datetime.now()
    filename = 'report.txt'
    dict_to_write['total_value'] = total_value
    dict_to_write['total_value_kw'] = total_value/1000
    dict_to_write['ts'] = now.timestamp()
    dict_to_write['dt'] = str(now)
    with open(os.path.join(report_dir, filename), 'a') as report_file:
        report_file.write(json.dumps(dict_to_write) + "\n")
