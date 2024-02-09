import datetime
from .Config import Config

Config = Config()


# Supporting methods
def get_hdr_date():
    date = datetime.datetime.utcnow()
    dt = date.strftime("%a, %d %b %Y %H:%M:%S")
    return dt + " UTC"


def get_current_date():
    date = datetime.datetime.now()
    # 2019-12-03T10:15:30+0000
    date = date.strftime("%Y-%m-%dT%H:%M:%S+0200")
    return date


def get_old_date(old_date=None):
    if old_date:
        old_datetime = datetime.datetime.strptime(old_date, "%Y-%m-%dT%H:%M:%S+0200")
        old_date_delta = datetime.datetime.now() - old_datetime
        date = datetime.datetime.now() - datetime.timedelta(seconds=old_date_delta.total_seconds())
    else:
        date = datetime.datetime.now() - datetime.timedelta(days=14)
    date = date.strftime("%Y-%m-%dT%H:%M:%S+0200")
    return date
