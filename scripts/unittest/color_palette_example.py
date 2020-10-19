import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from lib.color_lib import rainbow

def plot_rainbow(colors):
    fig, ax = plt.subplots()
    for i, color in enumerate(colors):
        rect = mpatches.Rectangle([0, i], 1, 1, color=color)
        ax.add_patch(rect)

    ax.set_ylim([0, len(colors)])
    plt.show()

colors = rainbow(11)
plot_rainbow(colors)