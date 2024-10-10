from datetime import datetime

now = datetime.now()
str_date_time = "10/08/1992 16:15"
mask_1 = "%d/%m/%Y %a %H:%M"
mask_2 = "%d/%m/%Y %H:%M"

now_str = now.strftime(mask_1)
print(now_str)
date_time = datetime.strptime(str_date_time, mask_2)
print(date_time)