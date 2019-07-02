sequence = [5, 2, 6, 8, 14, 25, 1, 63, 48, 9]

def heap_sort(sequence):
  # первый вариант сортировки

  def sift_down(parent, limit):
    item = sequence[parent]
    while True:
      child = (parent << 1) + 1
      if child >= limit:
        break
      if child + 1 < limit and sequence[child] < sequence[child + 1]:
        child += 1
      if item < sequence[child]:
        sequence[parent] = sequence[child]
        parent = child
      else:
        break
    sequence[parent] = item

  length = len(sequence)
  # Формирование первичной пирамиды
  for index in range((length >> 1) - 1, -1, -1):
    sift_down(index, length)
  # Окончательное упорядочение
  for index in range(length - 1, 0, -1):
    sequence[0], sequence[index] = sequence[index], sequence[0]
    sift_down(0, index)
  return sequence

def heap_sort2(sequence):

  def swap_items(index1, index2):
    if sequence[index1] < sequence[index2]:
      sequence[index1], sequence[index2] = sequence[index2], sequence[index1]
  
  def sift_down(parent, limit):
    while True:
      child = (parent + 1) << 1
      if child < limit:
        if sequence[child] < sequence[child - 1]:
          child -= 1
        swap_items(parent, child)
        parent = child
      else:
        break

  length = len(sequence)
  # Формирование первичной пирамиды
  for index in range((length >> 1) - 1, -1, -1):
    sift_down(index, length)
  # Окончательное упорядочение
  for index in range(length - 1, 0, -1):
    swap_items(index, 0)
    sift_down(0, index)
  
  return sequence


if __name__ == '__main__':
  print('Первый вариант сортировки: ', heap_sort(sequence))
  print('Второй вариант сортировки: ', heap_sort2(sequence))