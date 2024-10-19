#matplotlib 展示英伟达(美股代号 NVDA)的股票走势
import matplotlib.pyplot as plt
import pandas as pd


#该文件的时间是从现在到以前，因此展示的时候，需要变成逆序（从以前到现在）
#总行署5000多
NVDA_CSV_PATH="NVDA.csv"


df = pd.read_csv(NVDA_CSV_PATH)


x = df["index"]

#数据转换， reverse
y = df["close"][::-1]

plt.plot(x, y, color='r', marker='.')
plt.show()

