from replit import db
db['message'] = 'Hello!'
msg = db.keys()


val = db['message']
print(val)
lastval = val


path = input('path')
if path == 'ontvang':
  while True:
    val = db['message']
    if val != lastval:
      print(val)
      lastval = val
else:
  while True:
    send = input('\n')
    db['message'] = send
