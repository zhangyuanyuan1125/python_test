import datetime

# 获取今天日期
today = datetime.date.today()

# 获取昨天日期
yesterday = today - datetime.timedelta(days=1)

print(yesterday, today)



