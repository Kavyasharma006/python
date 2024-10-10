import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# years= np.array([2020,2021,2022,2023])
# grades=np.array([86,81,78,75])
# # show data in graph- line(x,y),pie(x),bar(x,y),scatters(x,y)
# plt.plot(years,grades,marker='o')
# # give the graph title
# plt.title("Academic Growth")
# # set the name for x and y axis
# plt.xlabel("Passing year")
# plt.ylabel("student marks")
# plt.show()

# trendinglanName=np.array(['Python','Javascript','Java','C#'])
# trendinglang=np.array([45,30,30,5]) 
# plt.title("Trending Language Marketplace")
# plt.pie(trendinglang)
# plt.legend(trendinglanName)
# plt.show()
# # Note:In line ,bar ,scatters graph the dataset must be of same size

# Jio 5 years sell growth (2020-2024)
year=np.array([2020,2021,2022,2023,2024])
sellgr=np.array([20,17,39,58,78])
plt.title("Sell Growth of Jio")
plt.bar(year,sellgr)
plt.xlabel("Years")
plt.ylabel("turnover(In cr.)")
plt.grid()/
plt.show()