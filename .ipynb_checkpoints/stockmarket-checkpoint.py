import streamlit as st
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime

st.title('株価データ')

# 銘柄選択
invest=st.sidebar.multiselect('銘柄',['^DJI', 'QQQ'],default=['^DJI', 'QQQ'])

# 株価取得期間
start_original = dt.date(year=1975,month=1,day=1)
end_original = dt.datetime.now().date()

# シミュレーション期間入力
start, end  = st.slider('シミュレーション期間', 
                   format='YYYY/MM',
                   min_value=start_original, 
                   value=(end_original-relativedelta(years=10),
                   end_original),
                   max_value=end_original
                   # step=relativedelta(months=1)
                  )

# 全期間データ
df1=data.DataReader(invest[0],'stooq',start_original,end_original)
df1=df1.iloc[::-1]
df2=data.DataReader(invest[-1],'stooq',start_original,end_original)
df2=df2.iloc[::-1]

# リターン
p1=st.sidebar.number_input('リターン計算期間(年)：case1',1)
df1_r1=df1.loc[start:end,'Close'].reset_index()
df1_r1=df1_r1.groupby([df1_r1['Date'].dt.year]).head(1)
df1_r1.set_index('Date',inplace = True)
df1_r1['Return']=df1_r1['Close'].pct_change(periods=p1)
df1_r1['Return']=df1_r1['Return'].shift(-p1)
p2=st.sidebar.number_input('リターン計算期間(年)：case2',5)
df1_r2=df1.loc[start:end,'Close'].reset_index()
df1_r2=df1_r2.groupby([df1_r2['Date'].dt.year]).head(1)
df1_r2.set_index('Date',inplace = True)
df1_r2['Return']=df1_r2['Close'].pct_change(periods=p2)
df1_r2['Return']=df1_r2['Return'].shift(-p2)





# グラフ
fig = plt.figure()
plt.subplots_adjust(hspace=0.6)

ax1 = fig.add_subplot(3,1,1)
ax1.plot(df1.index, df1['Close'],label=invest[0],color='red')
ax1.set_title('stock market')
ax1.set_ylabel(invest[0]+'(USD)')
ax1.legend()
ax1.grid()
ax1.tick_params(labelsize=7)

ax2 = ax1.twinx()
ax2.plot(df2.index, df2['Close'],label=invest[-1],color='blue')
ax2.set_ylabel(invest[-1]+'(USD)')
ax2.legend(loc='center left')
ax2.tick_params(labelsize=7)

ax3 = fig.add_subplot(3,1,2)
ax3.plot(df1[start:end].index, df1.loc[start:end,'Close'],label=invest[0],color='red')
ax3.set_ylabel(invest[0]+'(USD)')
ax3.grid()
ax3.tick_params(labelsize=7)

ax4 = ax3.twinx()
ax4.set_ylabel(invest[-1]+'(USD)')
ax4.plot(df2[start:end].index,df2.loc[start:end,'Close'],label=invest[-1],color='blue')
ax4.tick_params(labelsize=7)

ax5 = fig.add_subplot(3,1,3)
ax5.plot(df1[start:end].index, df1.loc[start:end,'Close'],label=invest[0],color='red')
ax5.set_xlabel('date')
ax5.set_ylabel(invest[0]+'(USD)')
ax5.grid()
ax5.tick_params(labelsize=7)

ax6 = ax5.twinx()
ax6.set_ylabel('return')
ax6.plot(df1_r1.index, df1_r1['Return'],label=str(p1)+'year(s) return',color='blue')
ax6.plot(df1_r2.index, df1_r2['Return'],label=str(p2)+'year(s) return',color='green')
ax6.legend()
ax6.tick_params(labelsize=7)

st.pyplot(fig)

