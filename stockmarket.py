import streamlit as st
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime

st.title('株価ダータ')

# 投資先選択
# invest1 = st.sidebar.radio('投資先',['^DJI', 'QQQ'])
# invest2=invest1
# invest2 = st.sidebar.radio('投資先',['^DJI', 'QQQ'])

invest=st.sidebar.multiselect('投資先',['^DJI', 'QQQ'],default=['^DJI', 'QQQ'])
st.write(invest)

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

# # 全期間データ
# df1=data.DataReader(invest1,'stooq',start_original,end_original)
# df1=df1.iloc[::-1]
# date1=df1.index
# df2=data.DataReader(invest2,'stooq',start_original,end_original)
# df2=df2.iloc[::-1]
# date2=df2.index

# # グラフ
# fig = plt.figure()
# plt.subplots_adjust(hspace=0.6)

# ax1 = fig.add_subplot(2,1,1)
# ax1.plot(date1, df1['Close'],label=invest1,color='red')
# ax1.set_title('stock market')
# ax1.set_ylabel(invest1+'(USD)')
# ax1.legend()
# ax1.grid()
# ax1.tick_params(labelsize=7)

# ax2 = ax1.twinx()
# ax2.plot(date2, df2['Close'],label=invest2,color='blue')
# ax2.set_ylabel(invest2+'(USD)')
# ax2.legend(loc='center left')
# ax2.tick_params(labelsize=7)

# ax3 = fig.add_subplot(2,1,2)
# ax3.plot(date1, df1['Close'],label=invest1,color='red')
# ax3.set_xlabel('date')
# ax3.set_ylabel(invest1+'(USD)')
# ax3.legend()
# ax3.grid()
# ax3.tick_params(labelsize=7)

# ax4 = ax3.twinx()
# ax4.set_ylabel(invest2+'(USD)')
# ax4.plot(date2, df2['Close'],label=invest2,color='blue')
# ax4.legend(loc='center left')
# ax4.tick_params(labelsize=7)











# # 全期間データ
# df1=data.DataReader(invest[0],'stooq',start_original,end_original)
# df1=df1.iloc[::-1]
# date1=df1.index
# df2=data.DataReader(invest[-1],'stooq',start_original,end_original)
# df2=df2.iloc[::-1]
# date2=df2.index

# # グラフ
# fig = plt.figure()
# plt.subplots_adjust(hspace=0.6)

# ax1 = fig.add_subplot(2,1,1)
# ax1.plot(date1, df1['Close'],label=invest[0],color='red')
# ax1.set_title('stock market')
# ax1.set_ylabel(invest[0]+'(USD)')
# ax1.legend()
# ax1.grid()
# ax1.tick_params(labelsize=7)

# ax2 = ax1.twinx()
# ax2.plot(date2, df2['Close'],label=invest[-1],color='blue')
# ax2.set_ylabel(invest[-1]+'(USD)')
# ax2.legend(loc='center left')
# ax2.tick_params(labelsize=7)

# ax3 = fig.add_subplot(2,1,2)
# ax3.plot(date1, df1['Close'],label=invest[0],color='red')
# ax3.set_xlabel('date')
# ax3.set_ylabel(invest[0]+'(USD)')
# ax3.legend()
# ax3.grid()
# ax3.tick_params(labelsize=7)

# ax4 = ax3.twinx()
# ax4.set_ylabel(invest[-1]+'(USD)')
# ax4.plot(date2, df2['Close'],label=invest[-1],color='blue')
# ax4.legend(loc='center left')
# ax4.tick_params(labelsize=7)




# st.pyplot(fig)
