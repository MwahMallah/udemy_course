from datetime import datetime, timedelta


in_6_month = datetime.now() + timedelta(days=182)

print(in_6_month.strftime("%d/%m/%Y"))