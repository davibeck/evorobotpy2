import matplotlib.pyplot as plt
import seaborn as sns


davi1 = [1163.76, 1132.11, 930.49 , 2240.85, 1618.00, 1878.97, 1841.37, 1609.50, 960.43 , 1058.69]
davi5 = [1696.09, 2014.77, 2143.36, 2013.19, 1506.54, 1648.72, 1968.14, 1781.34, 2349.49, 1924.12]
davi10 = [1936.20, 2209.71, 1795.31, 2310.07, 2208.95, 2265.03, 1256.07, 1466.56, 1704.81, 270.24]
larissa10 = [1691.02, 1953.19, 1652.34, 1627.58, 1618.62, 1815.49, 1999.38, 1859.27, 2047.88, 2109.81]


r_davi1 = [1346.35, 1363.48, 1735.80, 1880.34, 1722.69, 1144.52, 1625.03, 2113.52, 1360.63, 1037.83]
r_davi5 = [1834.92, 1895.39, 1552.28, 2280.14, 282.41, 1952.96, 1378.68, 1581.16, 2007.77, 2025.18]
r_davi10 = [2098.58, 1914.03, 1933.59, 1873.87, 1958.35, 2157.15, 2145.63, 2246.12, 2044.28, 2084.30]

brenda1 = [1578.34, 1295.90, -13.59, 1789.39, 1213.57, 2055.60, 2146.55, 1198.11, 1117.14, 1405.39]
brenda5 = [1244.24, 1803.94, 2131.52, 1317.69, 944.62, 1325.89, 1472.79, 2114.17, 1988.96, 1816.26]
brenda10 = [1119.49, 1300.68, 2000.04, 1385.62, 1965.39, 1275.55, 27.38  , 940.57 , 1824.46, 2123.31]


data = [[davi1, davi5, davi10, larissa10],
        [r_davi1, r_davi5, r_davi10, larissa10],
        [brenda1, brenda5, brenda10, larissa10]]

fig, axes = plt.subplots(ncols=3, figsize=(20, 5)) 

fig.suptitle('Boxplot - Hopper - Seeds')

axes[0].set_title('DB-Es')
sea = sns.boxplot(ax=axes[0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['1 Epsiode', '5 Episodes','10 Episodes', 'LA-Es'])
sea.set_ylim([0, 2500])

axes[1].set_title('RDB-Es')
sea = sns.boxplot(ax=axes[1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['1 Epsiode', '5 Episodes','10 Episodes', 'LA-Es'])
sea.set_ylim([0, 2500])

axes[2].set_title('OpenAi-Es-Ne')
sea = sns.boxplot(ax=axes[2], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['1 Epsiode', '5 Episodes','10 Episodes', 'LA-Es'])
sea.set_ylim([0, 2500])

plt.savefig('hopper_seeds.png')
