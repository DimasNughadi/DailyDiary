from datetime import datetime
now = datetime.now()
print(now)
date_time = now.strftime("%H-%M")
print(date_time)