import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

def animate(i):
    pullData = open("/Users/pushkarsingh/Desktop/twitter/test-yy_twitter.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0
    for l in lines[-100000:]:
        x += 1
        if "pos" in l:
            y+=1
        elif "neg" in l:
            y-=1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    ax1.plot(xar,yar)
    ax2.plot(xar,yar)
    ax3.plot(xar,yar)
    ax4.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000,save_count=1000)
plt.show()
