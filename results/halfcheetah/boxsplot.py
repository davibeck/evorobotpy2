import matplotlib.pyplot as plt
import seaborn as sns

davi_2n_50g = [2232.16, 1471.19, 2508.74, 1381.31, 2662.64, 15.91  ,351.30 , 2249.77, 2655.73, 944.21]
brenda_2n_50g = [1692.05, 356.32 , 1288.87, 840.49 , 1753.54, 2204.37, 1300.69, 624.32 , 1392.67, 1085.66]
larissa_500 = [1982.69, 2235.67, 2333.56, 2524.10, 684.58 , 1561.83, 1975.81, 1664.63, 1221.70, 392.11 ]
#super_2n_50g = [1717.53, 1549.67, 1402.20, 2412.98, 1785.64, 2321.78, 2095.40, 22.52  , 2062.77, 2806.13]

davi_3n_50g = [2626.66, 2122.09, 2185.25, 639.55, 1819.46, 1991.76, 1619.81, 2616.79, 2282.71, 1537.18]
brenda_3n_50g = [2307.02, 15.11, 14.67, 844.06, 1935.48, 1909.44, 1243.27, 2336.71, 2437.67, 1644.63]
#random = [15.66  , 764.08 , 2192.59, 2586.86, 2513.57, 2267.97, 1351.68, 2289.44, 2352.87, 2489.71]
larissa_333 = [1558.69, 2323.05, 2665.83, 1912.86, 2647.51, 1607.58, 1052.73, 1231.22, 1001.41, 1861.34]

davi_5n_50g = [2096.79, 1882.49, 1708.87, 1761.49, 16.46, 1542.16, 1407.60, 2253.80, 2245.84, 1437.40]
brenda_5n_50g = [1286.96, 1605.22, 1599.83, 1356.35, 2239.50, 1281.39, 1762.46, 590.17, 2017.05, 1247.02]
larissa_500 = [1895.62, 2216.35, 676.84 , 2202.48, 1909.15, 916.04 , 1490.30, 1998.81, 2636.05, 2320.15]
#super_5n_50g = [2722.44, 2439.23, 2517.59, 1783.99, 2201.03, 2437.00, 1721.58, 2319.28, 2423.41, 2149.12]
#super_larissa = [2683.01, 2992.44, 2947.73, 2777.17, 1673.23, 2757.99, 2907.45, 1840.87, 2554.32, 2854.33]

davi_10n_50g = [1803.83, 1527.64, 14.73 , 1567.81, 2040.28, 84.69 , 1592.13, 16.85 , 1592.79, 1107.09]
brenda_10n_50g = [12.06,  291.76 ,42.37  ,761.07 ,14.58  ,770.81 ,1944.82,1890.16,1257.22,1564.35]
larissa_100 = [840.33, 2555.51, 2274.35, 1252.90, 2191.86, 1735.66, 2871.30, 2830.40, 2233.00, 2540.72]


data = [[brenda_2n_50g, davi_2n_50g, larissa_500],
        [brenda_3n_50g, davi_3n_50g, larissa_333],
        [brenda_5n_50g, davi_5n_50g, larissa_500],
        [brenda_10n_50g, davi_10n_50g, larissa_100]]

fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('Boxplot - HalfCheetah')

axes[0, 0].set_title('2 Niches')
sea = sns.boxplot(ax=axes[0, 0], data=data[0], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 3000])

axes[0, 1].set_title('3 Niches')
sea = sns.boxplot(ax=axes[0, 1], data=data[1], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES' , 'LA-ES'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 3000])

axes[1, 0].set_title('5 Niches')
sea = sns.boxplot(ax=axes[1, 0], data=data[2], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES'])
sea.set_ylabel('Fitness')
sea.set_ylim([0, 3000])

axes[1, 1].set_title('10 Niches')
sea = sns.boxplot(ax=axes[1, 1], data=data[3], width=(0.5), linewidth=(0.95))
sea.set(xticklabels=['OpenAi-ES-NE', 'DB-ES', 'LA-ES'])
sea.set_ylabel('Fitness')

plt.savefig('halfcheetah.png')
