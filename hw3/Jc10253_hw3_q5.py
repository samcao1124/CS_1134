from ArrayQueue import ArrayQueue
def permutations(lst):
  queue = ArrayQueue()
  queue.enqueue([])
  for i in range(len(lst)):
    level = len(queue)
    for i in range(level):
      cur = queue.dequeue()
      for num in lst:
        if num not in cur:
          queue.enqueue(cur + [num])

  result = []
  while (not queue.is_empty()):
    result.append(queue.dequeue())
  return result

