# from collections import deque
# word = deque(["a", "b", "c"])
# print(word)
# word.popleft()
# print(word)
def add(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    print(sum)


add(10, 20, 30)
add(10, 20, 30, 40, 50)
