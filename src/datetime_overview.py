import time
import datetime

print(f"Current timestamp: {time.time()}")
print(f"Current datetime (local): {datetime.datetime.now()}")
print(f"Current datetime (UTC): {datetime.datetime.utcnow()}")
print(f"Current date: {datetime.date.today()}")

datetime_iso_str = "2022-10-24 21:49:24"
date_iso_str = "2022-10-24"
print(f"Datetime from iso str: {datetime.datetime.fromisoformat(datetime_iso_str)}")
print(f"Date from iso str: {datetime.date.fromisoformat(date_iso_str)}")
