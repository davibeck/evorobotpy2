import matplotlib.pyplot as plt
import seaborn as sns


d_episode_1 = [959.29, 402.03, 24.88, 934.61, 23.99, 30.69, 200.19, 1303.07, 751.27, 883.58]
d_episode_5 = [1626.74, 1637.87, 1104.87, 1411.43, 1486.22, 240.64, 1722.92, 1469.98, 1339.69, 619.05]
d_episode_10 = [53.21, 2069.03, 1376.71, 1068.42, 1460.41, 944.82, 1028.23, 1455.17, 1691.06, 941.87]
la_es = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]


r_episode_1 = [811.61, 1331.04, 416.88, 1115.72, 1615.40, 708.64, 479.88, 1366.88, 1188.54, 1337.45]
r_episode_5 = [995.87, 1584.00, 1246.12, 1495.55, 942.67, 1296.84, 1310.79, 1200.12, 620.41, 1101.23]
r_episode_10 = [1575.84, 1435.35, 1750.31, 1621.40, 776.93, 1539.64, 1231.47, 1714.27, 1401.24, 1563.00]

#brenda1 = [1578.34, 1295.90, -13.59, 1789.39, 1213.57, 2055.60, 2146.55, 1198.11, 1117.14, 1405.39]
#brenda5 = [1244.24, 1803.94, 2131.52, 1317.69, 944.62, 1325.89, 1472.79, 2114.17, 1988.96, 1816.26]
#brenda10 = [1119.49, 1300.68, 2000.04, 1385.62, 1965.39, 1275.55, 27.38  , 940.57 , 1824.46, 2123.31]


data = [[d_episode_1, d_episode_5, d_episode_10, la_es],
        [r_episode_1, r_episode_5, r_episode_10, la_es]]

fig, axes = plt.subplots(ncols=2, figsize=(15, 5)) 

fig.suptitle('Boxplot - Ant - Seeds')

axes[0].set_title('FixedSeed-Es')
sea = sns.boxplot(ax=axes[0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['1 Epsiode', '5 Episodes','10 Episodes', 'LA-Es'])
sea.set_ylim([0, 2500])

axes[1].set_title('RandSeed-Es')
sea = sns.boxplot(ax=axes[1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['1 Epsiode', '5 Episodes','10 Episodes', 'LA-Es'])
sea.set_ylim([0, 2500])

plt.savefig('ant_seeds.png')
