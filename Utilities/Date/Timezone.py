from datetime import datetime, timedelta, timezone

NYC_ET = timezone(timedelta(hours=-5))
print(NYC_ET)
# UTC-05:00

UTC_time = datetime(2023, 6, 7, 6, 6, 6)
print(UTC_time)
# 2023-06-07 06:06:06
NYC_time = datetime(2023, 6, 7, 6, 6, 6, tzinfo=NYC_ET)
print(NYC_time)
# 2023-06-07 06:06:06-05:00 # 5-hour UTC offset

NYC_time_2 = NYC_time.astimezone(NYC_ET)
print(NYC_time_2)
# 2023-06-07 06:06:06-05:00
