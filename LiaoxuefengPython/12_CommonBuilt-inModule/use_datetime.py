# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #re_datetime=re.compile(r'^(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)\s*?(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)$')
    re_utc=re.compile(r'^UTC(?P<mark>[+-])(?P<hour>\d{1,2}):(?P<minute>\d{2})$')
    m=re_utc.match(tz_str)
    utc_hours=int(m.group('mark')+m.group('hour'))
    utc_minute=int(m.group('minute'))
    utc=timezone(timedelta(hours=utc_hours,minutes=utc_minute))
    day=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    day=day.replace(tzinfo=utc)
    return day.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')