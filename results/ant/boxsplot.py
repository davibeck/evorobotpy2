import matplotlib.pyplot as plt

import seaborn as sns

brenda = [569.79 , 967.32 , 73.61  , 13.81  , 1078.41, 745.15 , 916.23 , 5.91 , 1010.00, 301.26 ]
davi = [897.15 , 714.81 , 1292.23, 1446.27, 661.58 , 17.92  , 57.24  , -2.33  , 923.54 , 1136.67]
random_davi = [706.64 , 1476.61, 702.85 , 1251.74, 441.51 , 10.39  , 75.43  , 1108.53, 724.01 , 1006.32]
larissa = [802.03 , 459.78 , 832.09 , 993.79 , 1099.31, 1544.66, 1053.97, 676.16 , 30.99  , 1222.83]
super_davi = [1075.94, 299.93 , 905.49 , 1211.24, -43.59 , 992.92 , 1197.40, 562.78 , 1239.50, 1323.91]
super_larissa = [1668.10, 877.70 , 1409.08, 623.21 , 1467.29, 745.22 , 981.61 , 1473.59, 991.49 , 792.80 ]

brenda2 = [-3.97  , 1383.64, 876.14 , 806.64 , 12.00  , 41.79  , 71.94  , 922.53 , 587.43 , 947.58 ]
davi2 = [959.29 , 402.03 , 24.88  , 934.61 , 23.99  , 30.69  , 200.19 , 1303.07, 751.27 , 883.58 ]
larissa2 = [293.90 , 1214.84, 534.91 , 638.72 , 1752.58, 23.67  , 1062.83, 1055.44, 1288.65, 1109.48]
super_davi2 = [1504.18, 400.26 , 1465.00, 1034.55, 1797.58, 946.51 , 899.04 , 1618.91, 1797.89, 1737.46]
super_larissa2 = [1494.09, 956.88 , 1636.86, 1336.67, 1199.77, 926.09 , 1160.42, 1558.24, 1280.56, 2256.17, 1680.66]

brenda5 = [751.08 , 820.54 , -7.93  , 48.70  , 3.97   , 875.85 , 1264.78, 55.18  , 1085.41, 315.30 ]
davi5 = [65.63  , 34.13  , 1143.82, 381.57 , 1220.91, 1237.89, 1126.28, 475.03 , 352.81 , 1360.22]
larissa5 = [1042.23, 986.44 , 1463.42, 788.16 , 866.81 , 1501.53, 64.26  , 983.56 , 1164.84, 985.55 ]
super_davi5 = [1300.20, 1659.51, 1666.34, 1246.22, 1705.65, 1255.89, 684.52 , 982.67 , 1556.87, 1410.08]
super_larissa5 = [1891.03, 2169.31, 2091.71, 1827.65, 1878.88, 2181.62, 2329.85, 1426.50, 1999.50, 1645.97]

brenda10 = [46.22 ,65.06 ,52.05 ,23.00 ,52.17 ,37.42 ,44.29 ,18.54 ,24.89 ,10.73]
davi10 = [96.84 , -7.82 , 50.14 , 153.10, 482.97, 78.16 , 65.86 , 191.77, 717.60, 579.02]
larissa10 = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]
super_davi10 = [1148.55 ,1232.64 ,1325.25 ,1113.42 ,1779.86 ,1049.20 ,1247.03 ,1276.91 ,1534.24 ,1227.99]
super_larissa10 = [2177.77, 2452.94, 1895.77, 2076.73, 2284.56, 2111.33, 2382.91, 2411.67, 1876.22, 2400.18]


data = [[brenda,  davi, random_davi, larissa, super_davi, super_larissa],
        [brenda2,  davi2, larissa2, super_davi2, super_larissa2],
        [brenda5,  davi5, larissa5, super_davi5, super_larissa5],
        [brenda10,  davi10, larissa10, super_davi10, super_larissa10]]

fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('Boxplot - Ant')

axes[0, 0].set_title('2 Niches')
sea = sns.boxplot(ax=axes[0, 0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES','DB-ES-R', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 2500])

axes[0, 1].set_title('3 Niches')
sea = sns.boxplot(ax=axes[0, 1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 2500])

axes[1, 0].set_title('5 Niches')
sea = sns.boxplot(ax=axes[1, 0], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylim([0, 2500])

axes[1, 1].set_title('10 Niches')
sea = sns.boxplot(ax=axes[1, 1], data=data[3], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])

plt.savefig('ant.png')
