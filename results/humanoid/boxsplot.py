import matplotlib.pyplot as plt
import seaborn as sns

davi2 = [77.46, 93.48, 96.05, 89.34, 147.01, 89.90, 90.36, 78.90, 163.99, 83.42]
brenda2 = [126.23, 108.51, 137.61, 124.77, 154.05, 96.18 , 94.60 , 82.88 , 109.12, 150.39]
larissa2 = [100.03, 86.54, 110.25, 99.75, 79.76, 103.34, 82.82, 93.66, 111.67, 99.00]
super_davi2 = [109.45, 91.32, 105.44, 91.58, 157.61, 93.97, 148.25, 68.43, 94.94, 139.68]
super_larissa2 = [105.24, 96.00, 125.61, 104.93, 84.16, 87.92, 82.53, 83.78, 102.25, 83.78, 103.41]

davi3 = [88.41, 92.14, 64.98, 72.99, 96.03, 93.52, 94.96, 93.24, 97.56, 119.04]
brenda3 = [96.36, 87.22, 86.60, 115.89, 132.55, 83.72, 128.33, 131.10, 112.52, 165.73]
larissa3 = [86.41, 91.30, 93.29, 80.11, 87.66, 107.37, 93.09, 86.08, 98.98, 87.12]
super_davi3 = [111.54, 87.06, 128.25, 129.47, 129.02, 145.42, 83.96, 107.25, 152.84, 152.97]
super_larissa3 = [84.80, 99.95, 96.90, 94.56, 84.46, 83.54, 103.03, 90.37, 89.42, 102.20]

brenda5 = [168.22, 122.52, 145.40, 132.72, 162.39, 111.62, 83.33, 111.85, 135.91, 115.34]
davi5 = [107.76, 88.20, 134.25, 157.70, 125.61, 93.16, 79.63, 103.18, 99.95, 125.09]
larissa5 = [97.39, 99.67, 95.52, 92.19, 114.19, 83.08, 96.99, 67.15, 84.74, 93.24, 92.33]
super_davi5 = [93.09, 91.96, 138.22, 126.53, 153.72, 95.95, 86.53, 117.71, 123.76, 105.97]
super_larissa5 = [78.57, 82.96, 95.41, 91.06, 74.86, 79.93, 88.43, 77.61, 88.09, 105.19]

brenda10 = [116.69, 113.75, 116.18, 132.42, 132.85, 124.11, 108.69, 118.28, 127.42, 170.18]
davi10 = [123.39, 193.10, 125.09, 163.31, 146.97, 125.62, 126.27, 129.18, 119.51, 153.67]
random_davi10 = [156.16, 132.53, 91.16, 141.83, 123.32, 86.93, 105.01, 106.63, 121.11, 136.59]
larissa10 = [65.95, 64.92, 73.95, 80.90, 78.50, 114.25, 74.55, 79.96, 85.58, 79.67]
super_davi10 = [99.18, 114.86, 118.14, 98.91, 146.47, 124.34, 129.81, 128.04, 107.57, 103.63]
super_larissa10 = [115.23, 108.48, 118.78, 105.96, 89.56, 92.35, 105.24, 85.52, 104.39, 96.71]

data = [[brenda2, davi2,  larissa2, super_davi2, super_larissa2],
        [brenda3, davi3, larissa3, super_davi3, super_larissa3],
        [brenda5, davi5, larissa5, super_davi5, super_larissa5],
        [brenda10, davi10, random_davi10, larissa10, super_davi10, super_larissa10]]

fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('Boxplot - Hopper')

axes[0, 0].set_title('2 Niches')
sea = sns.boxplot(ax=axes[0, 0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 200])

axes[0, 1].set_title('3 Niches')
sea = sns.boxplot(ax=axes[0, 1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 200])

axes[1, 0].set_title('5 Niches')
sea = sns.boxplot(ax=axes[1, 0], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 200])

axes[1, 1].set_title('10 Niches')
sea = sns.boxplot(ax=axes[1, 1], data=data[3], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'DB-ES-R', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 200])

plt.savefig('humanoid.png')
