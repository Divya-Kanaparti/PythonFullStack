#QUEUE USING DEQUEUE
from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
print(queue)
queue.appendleft(5)
print(queue)
queue.pop()
print(queue)