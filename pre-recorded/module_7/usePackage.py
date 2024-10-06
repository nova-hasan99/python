import matplotlib.pyplot as plt

x = [1, 3, 4, 5, 6, 7, 8]
y = [2, 5, 6, 7, 15, 16, 20]

plt.plot(x, y)
plt.title('Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.savefig('graph.jpg', format = 'jpg')
plt.show()
plt.close()
