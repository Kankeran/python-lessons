import matplotlib.pyplot as plt
import random
mojaText = "blablaBlaBlabla"
for i in range(20):
    text = plt.annotate(mojaText, xy=(random.uniform(0, .7), random.uniform(0, 1)), size=random.randint(10, 30), color='#3192aa')
    text.set_alpha(random.uniform(.2, 1))
plt.axis('off')
plt.show()

