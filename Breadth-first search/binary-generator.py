import queue

q = queue.Queue()
q.put("")

for i in range(100):
  x = q.get()
  y = x + "0"
  z = x + "1"
  q.put(y)
  q.put(z)

for i in range(q.qsize()):
  print(q.get())