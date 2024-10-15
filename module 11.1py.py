import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

a = np.zeros((3, 5))
b = np.ones((3, 5))
print(a)
print(b)
c = a + b
print(c)

x = np.linspace(0, 1, 100)
f1 = 0.5 - (x - 0.9)**2
f2 = x**2
plt.plot(x, f1, ':b')    # пунктирная синяя линия
plt.plot(x, f2, '--r')   # штрихованная красная линия
plt.plot(x, f1+f2, 'k')  # черная непрерывная линия
plt.show()


image = Image.open("Ввод.jpg")
rotated_image = image.rotate(45)
new_image = image.resize((200, 385))
new_image.show()
rotated_image.save("rotated.png")
