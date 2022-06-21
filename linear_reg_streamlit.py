import streamlit as st
# st.set_page_config(layout="wide")
import numpy as np
import pandas as pd

st.title("Simple Linear Regression Calculator \U0001f4c8")

st.text("")

ch1 = st.checkbox("Entering datapoints manually", value = False)
if ch1:
    num_of_datapoints = st.number_input("Enter the number of data points : ", min_value = 1)

    st.text("")
    st.text("Enter datapoints : ")
    c1, c2 = st.columns(2)
    x = np.zeros(num_of_datapoints)
    y = np.zeros(num_of_datapoints)

    for i in range(num_of_datapoints):
        x[i] = (c1.number_input("Enter value of Indipendent variable :", key = i))
        y[i] = (c2.number_input("Enter value of Dependent variable :", key = i))


    data = {
        'Independent variable' : x,
        'Dependent variable' : y
    }

    x = pd.DataFrame(data['Independent variable'])
    y = pd.DataFrame(data['Dependent variable'])

    st.write("the data given is :")
    st.table(data)

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(x, y)

    x = (st.number_input("Enter the number which you want to predict for :"))
    x = [[x]]

    y_pred = lr.predict(x)
    st.write("the predicted value is : ", y_pred)

ch2 = st.checkbox("Upload a file for datapoints", value = False)
if ch2:
    file = st.file_uploader("Upload a CSV file")
    if file is not None:
        data = pd.read_csv(file)
        
        column_names = []
        for row in data:
            column_names.append(row)
        
        x = st.radio("Select the Independent column :", column_names)
        y = st.radio("Select the Dependent column :", column_names)

        st.write(x, y)

        x = data[x]
        y = data[y]

        data = {
            'Independent variable' : x,
            'Dependent variable' : y
        }

        x = pd.DataFrame(data['Independent variable'])
        y = pd.DataFrame(data['Dependent variable'])

        # st.write("the data given is :")
        # st.table(data)

        from sklearn.linear_model import LinearRegression
        lr = LinearRegression()
        lr.fit(x, y)

        x = (st.number_input("Enter the number which you want to predict for :"))
        x = [[x]]

        y_pred = lr.predict(x)
        st.write("the predicted value is : ", y_pred)