import time
import matplotlib.pyplot as plt

tlist = []
word = "question"
mistakes = 0
while len(tlist) < 5:
    start = time.time() 
    type = input("type question fast: ")
    end = time.time()
    laspe = end - start
    tlist.append(laspe)

    if type != word:
        mistakes += 1




x = [1,2,3,4,5]
print(tlist,mistakes)
plt.plot(x,tlist)
plt.show()
