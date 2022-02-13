import streamlit as st
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime
import plotly.graph_objs as go
from plotly.subplots import make_subplots

st.title('株価データ')

# 銘柄選択
brand=st.selectbox('銘柄',['^DJI', 'QQQ'])

# 株価取得期間
start = dt.date(year=1975,month=1,day=1)
end = dt.datetime.now().date()

# シミュレーション期間
start2 = st.date_input('シミュレーション期間：初日',
                       min_value=start,
                       max_value=end,
                      )
end2 = st.date_input('シミュレーション期間：最終日',
                     min_value=start,
                     max_value=end,
                    )

# 株価データ
df=data.DataReader(brand,'stooq',start,end)
df=df.iloc[::-1]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(df.index, df['Close'],label=brand)
ax.set_title('stock market')
ax.set_ylabel('usd')
ax.legend()
ax.grid()
# ax.tick_params(labelsize=7)
st.pyplot(fig)

def sim(df,start2,end2):
    # 積立計算
    df2=df.reset_index()
    df2 = df2.groupby([df2['Date'].dt.year, df2['Date'].dt.month]).head(1)
    df2.set_index('Date',inplace = True)

    # ドルコスト平均法
    df['purchases']=0
    df.loc[df2[start2:end2].index,'purchases']=1
    df['total_purchases']=df['purchases'].cumsum()
    s=max(df['total_purchases'])
    df.loc[df2[start2:end2].index,'purchases']=df.loc[df2[start2:end2].index,'purchases']/s
    df['total_purchases']=df['purchases'].cumsum()
    df['shares']=df['purchases']/df['Close']
    df['total_shares']=df['shares'].cumsum()
    df['value']=df['Close']*df['total_shares']

    # 一括投資
    df['purchases2']=0
    df.loc[df2[start2:end2].index[0],'purchases2']=1
    df['total_purchases2']=df['purchases'].cumsum()
    df['shares2']=df['purchases2']/df['Close']
    df['total_shares2']=df['shares2'].cumsum()
    df['value2']=df['Close']*df['total_shares2']

    # リターン
    df.loc[df2.index,'Return']=df2['Close'].pct_change(periods=12)

    # グラフ
    fig = make_subplots(rows=3,
                        cols=1,
                        subplot_titles=['投資シミュレーション','リターン','株価'],
                        shared_xaxes=True,
                        specs=[[{'secondary_y':False}],
                               [{'secondary_y':False}],
                               [{'secondary_y':False}]])
    fig.update_layout(height=600,
                      xaxis3=dict(title='date'),
                      xaxis3_rangeslider=dict(visible=True,
                                             thickness=0.1),
                      yaxis=dict(title='return',fixedrange=False),
                      yaxis2=dict(title='return',fixedrange=False),
                      yaxis3=dict(title='usd',fixedrange=False)
                     )
    fig.add_trace(go.Scatter(x=df.index,
                             y=df['Close'],
                             mode='lines',
                             name='^DJI'),
                 row=3,
                 col=1)
    fig.add_trace(go.Bar(x=df2.index,
                             y=df.loc[df2.index,'Return'],
                             name='年利'),
                 row=2,
                 col=1)   
    fig.add_trace(go.Scatter(x=df.loc[start2:end2].index,
                             y=df.loc[start2:end2,'total_purchases'],
                             mode='lines',
                             name='貯金'),
                 row=1,
                 col=1)
    fig.add_trace(go.Scatter(x=df.loc[start2:end2].index,
                             y=df.loc[start2:end2,'value'],
                             mode='lines',
                             name='ドル・コスト平均法'),
                 row=1,
                 col=1)
    fig.add_trace(go.Scatter(x=df.loc[start2:end2].index,
                             y=df.loc[start2:end2,'value2'],
                             mode='lines',
                             name='一括投資'),
                 row=1,
                 col=1)
    fig.show()

if st.button('開始'):
    sim(df,start2,end2)
    fig.write_html('first_figure2.html', auto_open=True)