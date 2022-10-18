from collections import deque

snake = deque([(0, 0)])
snake.appendleft((0, 1))
print(snake)