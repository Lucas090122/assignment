#a = 0
#while a > 5:
#    b = 0
#    while b < 6:
#        b+=1
#        print(f"{a} multiplied with {b} is {a * b}")
#    a+=1

#lst = []
#while len(lst) < 5:
#    n = input("provide a name:\n")
#    lst.append(n)
#print(lst)
#用户添加字符进列表直到列表容量为5

#n = "hello world!"
#print(n[5])

#n = 'hello world!'
#print('n')
#print(n)
#print(n[:])


#lst = [323, 323, 'adsf', 3.2, []]

#tup = (323, 223, 'adf')

#lst = [1, 2, 3]
#n = enumerate(lst)
##print(list(n))

#for i, j in n:
#    print(f"i is {i}, j is {j}")
#print(list(n))
#
import time
start_time = time.time()
import random
def estimate_pi(points):
    inside_circle = 0

    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2

        if distance < 1:
            inside_circle += 1

    return 4 * inside_circle / points

def main():
    points = int(input("Enter the number of random points to generate: "))
    pi_approximation = estimate_pi(points)
    print(f"Approximation of pi using {points} points: {pi_approximation}")

if __name__ == "__main__":
    main()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行花费了{elapsed_time:.2f}秒。")
#
# #
# l = []
# while True:
#     item = input("Please add item to your list:")
#     if item == "stop":
#         break
#     else:
#         l.append(item)
# for i in l:
#     print(i)
