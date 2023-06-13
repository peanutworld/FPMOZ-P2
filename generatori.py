'''
Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
'''

def function(n):
  for i in range(n):
    if i % 2 == 0 or i % 2 != 0:
      yield i
    
iterator = iter(function(20))

while 1:
  try:
      print(next(iterator))
  except:
      break