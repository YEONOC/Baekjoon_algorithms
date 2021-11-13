x, y, w, h = map(int, input().split())

a = w - x

b = h - y

number = [a, b, x, y]
print(min(number))