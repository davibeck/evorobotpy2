import matplotlib.pyplot as plt
import seaborn as sns

brenda2 = [284.92, 94.55 , 523.27, 508.98, 70.91 , 55.09 , 106.83, 209.38, 83.13 , 310.64]
davi2 = [111.59, 119.59, 390.45, 920.62, 422.62, 12.20 , 26.41 , 75.05 , 180.49, 478.04]
larissa2 = [118.79 ,620.39 ,589.44 ,1177.23,122.24 ,112.89 ,254.57 ,112.73 ,402.21 ,1365.03]
super_davi2 = [108.99 , 1122.09, 681.37 , 782.30 , 1140.09, 12.34  , 598.31 , 364.65 , 679.76 , 1175.42]
super_larissa2 = [14.37  , 364.13 , 520.61 , 512.21 , 1500.18, 435.07 , 619.68 , 370.00 , 1580.70, 1752.64]

brenda3 = [12.80 , 11.98 , 74.62 , 471.60, 237.86, 104.35, 372.94, 196.51, 169.33, 324.70]
davi3 = [12.60  , 83.13  , 88.45  , 703.30 , 435.81 , 82.70  , 447.04 , 1228.85, 610.88 , 869.95 ]
random_davi3 = [12.46  , 888.82 , 1265.24, 505.56 , 825.87 , 720.00 , 526.47 , 1072.33, 1468.38, 1531.24]
larissa3 = [718.81 , 614.22 , 920.25 , 848.58 , 588.62 , 160.63 , 1373.55, 199.94 , 854.87 , 870.88 ]
super_davi3 = [1210.80, 973.53 , 12.50  , 58.66  , 12.19  , 309.14 , 1002.83, 1443.90, 127.00 , 416.87 ]
super_larissa3 = [741.34 , 668.10 , 588.62 , 1369.87, 1642.38, 727.13 , 270.20 , 644.54 , 648.38 , 608.35 ]

brenda5 = [120.44, 105.92, 424.59, 784.00, 692.93, 12.19 , 73.15 , 275.48, 168.76, 460.39]
davi5 = [12.01 , 72.93 , 106.26, 439.61, 787.42, 12.31 , 11.12 , 90.06 , 299.08, 287.48]
larissa5 = [14.58  , 172.29 , 576.46 , 1385.97, 299.27 , 1443.33, 1133.08, 456.65 , 634.15 , 757.37 ]
super_davi5 = [789.16 , 660.36 , 83.25, 512.67 , 971.75 , 1412.65, 856.36 , 438.62 , 659.33 , 676.94 ]
super_larissa5 = [11.82  , 1179.68, 755.75 , 1409.34, 1410.98, 787.56 , 861.88 , 1581.81, 1263.18, 1590.91]

brenda10 = [10.63 , 92.26 , 268.29, 91.36 , 102.00, 172.82, 102.04, 11.08 , 465.51, 103.24]
davi10 = [134.69, 82.09 , 397.70, 325.77, 140.38, 314.99, 135.86, 383.11, 103.04, 555.45]
larissa10 = [232.45 ,1119.44,512.75 ,106.27 ,105.27 ,463.79 ,1118.21, 767.63 ,1202.95]
super_davi10 = [789.16 , 660.36 , 83.25, 512.67 , 971.75 , 1412.65, 856.36 , 438.62 , 659.33 , 676.94 ]
super_larissa10 = [11.82  , 1179.68, 755.75 , 1409.34, 1410.98, 787.56 , 861.88 , 1581.81, 1263.18, 1590.91]

data = [[brenda2, davi2,  larissa2, super_davi2, super_larissa2],
        [brenda3, davi3, random_davi3, larissa3, super_davi3, super_larissa3],
        [brenda5, davi5, larissa5, super_davi5, super_larissa5],
        [brenda10, davi10, larissa10, super_davi10, super_larissa10]]

fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('Boxplot - Walker')

axes[0, 0].set_title('2 Niches')
sea = sns.boxplot(ax=axes[0, 0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2000])

axes[0, 1].set_title('3 Niches')
sea = sns.boxplot(ax=axes[0, 1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'DB-ES-R', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2000])

axes[1, 0].set_title('5 Niches')
sea = sns.boxplot(ax=axes[1, 0], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2000])

axes[1, 1].set_title('10 Niches')
sea = sns.boxplot(ax=axes[1, 1], data=data[3], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2000])

plt.savefig('walker.png')
