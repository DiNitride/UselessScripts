from datetime import datetime
import dateparser

start = dateparser.parse("01-04-2020")
now = datetime.now()

delta = now - start

print(delta.days * 12)