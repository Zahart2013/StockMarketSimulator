import matplotlib.pyplot as plt
from market import Market

mrkt = Market()

for company in mrkt.basic:
    plt.style.use('dark_background')
    plt.plot(mrkt.basic[company],
             color='#A967D5',
             marker='o',
             linewidth=2,
             markersize=5)
    plt.savefig('{}.jpg'.format(company))