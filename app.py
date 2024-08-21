import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt

def total_days(s_date,e_date):
    start_date = list(map(int, s_date.split('-')))
    end_date = list(map(int, e_date.split('-')))
    print(start_date)
    print(end_date)
    sy, sm, sd = start_date[0], start_date[1], start_date[2]
    ey, em, ed = end_date[0], end_date[1], end_date[2]
    if ed<sd:
        ed1=ed+30
        em1=em-1
        days=ed1-sd
        if em1<sm:
            em2=em1+12
            ey1=ey-1
            months=em2-sm
            if ey1<sy:
                print("please check your values")
            else:
                years=ey1-sy
        else:
            months=em1-sm
            if ey<sy:
                print("please check your values")
            else:
                years=ey-sy
    else:
        days=ed-sd
        if em<sm:
            em3=em+12
            ey2=ey-1
            months=em3-sm
            if ey2<sy:
                print("please check your details")
            else:
                years=ey2-sy
        else:
            months=em-sm
            if ey<sy:
                print("please check your values")
            else:
                years=ey-sy

    td=days+(months*30)
    td1=td+(years*360)
    return td1

def c_interest(p,r,s_date,e_date):
    rt=(r*12)/100
    start_date = list(map(int, s_date.split('-')))
    end_date = list(map(int, e_date.split('-')))
    print(start_date,end_date)
    sy, sm, sd = start_date[0], start_date[1], start_date[2]
    ey, em, ed = end_date[0], end_date[1], end_date[2]
    if ed<sd:
        ed1=ed+30
        em1=em-1
        days=ed1-sd
        if em1<sm:
            em2=em1+12
            ey1=ey-1
            months=em2-sm
            if ey1<sy:
                print("please check your values")
            else:
                years=ey1-sy
        else:
            months=em1-sm
            if ey<sy:
                print("please check your values")
            else:
                years=ey-sy
    else:
        days=ed-sd
        if em<sm:
            em3=em+12
            ey2=ey-1
            months=em3-sm
            if ey2<sy:
                print("please check your details")
            else:
                years=ey2-sy
        else:
            months=em-sm
            if ey<sy:
                print("please check your values")
            else:
                years=ey-sy


    td=days+(months*30)
    td1=td+(years*360)
    t=td1/360

    i1 = (p*(1+rt)**(int(t))) - p
    p1 = i1 + p
    i2 = (p1*rt*(t-int(t))) + p1
    return i2

def s_interest(principle, r, s_date, e_date):
    rt=(r*12)/100
    start_date = list(map(int, s_date.split('-')))
    end_date = list(map(int, e_date.split('-')))
    sy, sm, sd = start_date[0], start_date[1], start_date[2]
    ey, em, ed = end_date[0], end_date[1], end_date[2]
    if ed < sd:
        ed1 = ed + 30
        em1 = em - 1
        days = ed1 - sd
        if em1 < sm:
            em2 = em1 + 12
            ey1 = ey - 1
            months = em2 - sm
            if ey1 < sy:
                print("please check your values")
            else:
                years = ey1 - sy
        else:
            months = em1 - sm
            if ey < sy:
                print("please check your values")
            else:
                years = ey - sy
    else:
        days = ed - sd
        if em < sm:
            em3 = em + 12
            ey2 = ey - 1
            months = em3 - sm
            if ey2 < sy:
                print("please check your details")
            else:
                years = ey2 - sy
        else:
            months = em - sm
            if ey < sy:
                print("please check your values")
            else:
                years = ey - sy

    td = days + (months * 30)
    td1 = td + (years * 360)
    t = td1 / 360

    interest = principle*t*rt
    return interest
st.set_page_config(page_title="Interest Calculator", layout="wide", initial_sidebar_state="expanded")
st.title('Interest Calculator')
uploaded_file = st.file_uploader("Upload an excel file", type=['xlsx'])
date_option = st.radio("Select End Date", ["Today", "Choose Date"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['start_date'] = df['start_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    if date_option == "Today":
        end_date = date.today().strftime('%Y-%m-%d')
    else:
        end_d = st.date_input("Choose Date")
        end_date = end_d.strftime('%Y-%m-%d')
    df['days'] = df.apply(lambda row: total_days(row['start_date'], end_date), axis=1)
    df['s_interest'] = df.apply(lambda row: s_interest(row['principle'], row['rate_of_interest'], row['start_date'], end_date)+row['principle'], axis=1)
    df['c_interest'] = df.apply(lambda row: c_interest(row['principle'], row['rate_of_interest'], row['start_date'], end_date), axis=1)
    st.write(df)
    st.write("total amount")
    st.write(round(df['principle'].sum(), 2))
    st.write("total simple interest")
    st.write(round(df['s_interest'].sum(), 2))
    st.write("total compound interest")
    st.write(round(df['c_interest'].sum(), 2))

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(['Total Amount', 'Total Simple Interest', 'Total Compound Interest'], [round(df['principle'].sum(), 2), round(df['s_interest'].sum(), 2), round(df['c_interest'].sum(), 2)])
    plt.title('Principle Amount, Simple Interest, and Compound Interest')
    plt.ylabel('Amount in Crores')
    st.pyplot(plt)
  
