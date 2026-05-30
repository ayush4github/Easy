from collections import deque
def generate_binary(n):
    queue = deque()
    queue.append("1")
    for i in range(n):
        current = queue.popleft()
        print(current)

        queue.append(current + "0")
        queue.append(current + "1")

#Driver Code
generate_binary(5)