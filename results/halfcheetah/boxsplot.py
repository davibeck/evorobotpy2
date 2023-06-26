import matplotlib.pyplot as plt

larissa = [2586.61, 1771.13, 2501.58, 2721.62, 2551.22, 2469.41, 2611.83, 1736.72, 2188.47, 1501.99]
n2_ninhes_85gen = [1132.06, 1098.24, 927.45, 1046.89, 2251.03, 1308.10, 1457.58, 886.21, 2523.80, 1102.83]
n3_ninhes_81gen = [1819.39, 2309.27, 1709.37, 1508.11, 388.77, 1585.04, 1313.88, 1521.28, 1875.00, 1041.78]
n3_ninhes_85gen = [1949.65, 2166.62, 1642.99, 1087.03, 567.61, 2028.04, 1884.61, 29.98, 862.59, 1377.13]
n5_ninhes_85gen = [1060.05, 799.99, 2166.92, 1385.61, 68.50, 1501.74, 1442.33, 2228.08, 1441.75, 2324.43]
same_seed = [1849.67, 2217.15, 1942.40, 12.44, 2396.38, 14.46, 46.13, 1977.26, 2688.30, 2433.91]
brenda_arthur = [2292.80, 14.60, 1972.14, 2151.44, 1771.35, 1768.26,  2314.94, 2522.45, 2702.26, 830.22]
different_seed = [480.38, 1119.48, 2582.86, 2003.30, 15.55, 1117.11,  2417.99, 16.35, 1311.22, 1352.12]


data = [larissa, n2_ninhes_85gen, n3_ninhes_81gen, n3_ninhes_85gen, n5_ninhes_85gen, same_seed, brenda_arthur, different_seed]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['Larissa', '2-85', '3-81', '3-85', '5-85', 'Same seed', 'Brenda', 'Different'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - OpenAi-Es vs OpenAi-Es-Ne')
#plt.figure(figsize=)
#plt.savefig('teste.png')
plt.show()
