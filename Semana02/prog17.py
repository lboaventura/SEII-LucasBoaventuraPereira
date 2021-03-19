import datetime
import pytz

tday = datetime.date.today()
print(tday)

tdelta = datetime.timedelta(days=20)
print(tday + tdelta)

bday = datetime.date(2021, 9, 24)
till_bday = bday - tday
print(till_bday.days)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow2)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
