import matplotlib.pyplot as plt
import seaborn as sns

brenda2 = [24.84  , 1281.87, 1192.89, 1588.59, 1523.10, 834.65 , 1425.22, 971.58 , 1938.87, 1545.74]
davi2 = [1099.09, 1515.24, 1726.76, 1514.44, 1387.73, 1907.77, 1454.61, 1441.08, 16.06  , 1723.47]
larissa2 = [1119.49, 1300.68, 2000.04, 1385.62, 1965.39, 1275.55, 27.38  , 940.57 , 1824.46, 2123.31]
#random_davi2 = [1574.62, 1522.07, 1906.55, 1698.16, 2092.44, 1349.22, 1441.61, 1721.40, 1620.04, 1775.66]
super_davi2 = [1309.40, 1711.05, 1147.97, 1062.49, 1415.73, 1509.84, 3.97   , 1438.10, 2067.40, 1979.26]
super_larissa2 = [1311.60, 1339.94, 1525.89, 1794.36, 1528.63, 1721.22, 1823.29, 2009.18, 1831.85, 1693.03]

brenda3 = [1578.34, 1295.90, -13.59 , 1789.39, 1213.57, 2055.60, 2146.55, 1198.11, 1117.14, 1405.39]
davi3 = [1163.76, 1132.11, 930.49 , 2240.85, 1618.00, 1878.97, 1841.37, 1609.50, 960.43 , 1058.69]
larissa3 = [1268.97, 1885.22, 236.86 , 2062.58, 1893.48, 1531.03, 1567.79, 1667.87, 1990.61, 233.72 ]
super_davi3 = [1263.52, 1499.21, 1918.60, 2004.17, 1876.71, 1787.56, 2094.18, 2161.57, 1162.04, 1717.05]
super_larissa3 = [1427.37, 1553.29, 1979.35, 1589.56, 1995.10, 2164.77, 1074.79, 1870.94, 1907.50, 1967.66]

brenda5 = [1235.89, 1450.44, 1350.04, 1542.17, 1169.90, 1438.30, 1185.31, 1446.52, 2131.47, 1219.80]
davi5 = [897.15 , 714.81 , 1292.23, 1446.27, 661.58 , 17.92  , 57.24  , -2.33  , 923.54 , 1136.67]
larissa5 = [1662.42, 1676.18, 1343.32, 1867.76, 1729.07, 1884.13, 1413.59, 1649.83, 2150.13, 1750.52]
super_davi5 = [1669.24, 1487.05, 1962.90, 2203.44, 1481.63, 1560.19, 1459.67, 1717.82, 2033.88, 1492.93]
super_larissa5 = [1839.70, 1472.02, 1610.30, 2522.95, 1511.00, 1589.31, 1830.36, 1447.09, 1739.53, 2111.75]

brenda10 = [1063.09, 1173.03, 1190.32, 1285.13, 912.61 , 1058.03, 967.19 , 1369.74, 1327.43, 1456.71]
davi10 = [1301.21, 1374.82, 1257.51, 1099.81, 1751.52, 1408.33, 383.46 , 1103.43, 1367.56, 1380.36]
larissa10 = [1691.02, 1953.19, 1652.34, 1627.58, 1618.62, 1815.49, 1999.38, 1859.27, 2047.88, 2109.81]
super_davi10 = [1509.52, 1649.77, 1975.61, 1765.82, 1662.44, 1492.95, 1811.15, 1963.10, 2010.98, 2319.25]
super_larissa10 = [1687.19, 1865.10, 2001.02, 2051.33, 1913.84, 1373.45, 1903.17, 2123.76, 1837.16, 2139.66]

data = [[brenda2, davi2,  larissa2, super_davi2, super_larissa2],
        [brenda3, davi3, larissa3, super_davi3, super_larissa3],
        [brenda5, davi5, larissa5, super_davi5, super_larissa5],
        [brenda10, davi10, larissa10, super_davi10, super_larissa10]]

fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('Boxplot - Hopper')

axes[0, 0].set_title('2 Niches')
sea = sns.boxplot(ax=axes[0, 0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2500])

axes[0, 1].set_title('3 Niches')
sea = sns.boxplot(ax=axes[0, 1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2500])

axes[1, 0].set_title('5 Niches')
sea = sns.boxplot(ax=axes[1, 0], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2500])

axes[1, 1].set_title('10 Niches')
sea = sns.boxplot(ax=axes[1, 1], data=data[3], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 2500])


plt.savefig('hopper.png')
