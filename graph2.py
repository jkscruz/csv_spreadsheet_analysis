# ---- EXPENDITURE / SALES GRAPH (2) ----

import seaborn as sns
import csv
import pandas as pd
import matplotlib.pyplot as plt

#FUNCTION
# ---- Function to Plot Expenditure/Sales Graph ----
def graph_exp_sales():
    data = pd.read_csv('sales.csv')

    #Transforming the Data

    df = pd.DataFrame.from_dict(data)  # create Pandas DataFrame containing the data
    df['expenditure'] = df['expenditure'].astype(
        "int")  # change the data type of the expenditure from float (decimal) to integers
    df['sales'] = df['sales'].astype("int")  # change the data type of the expenditure from float (decimal) to integers

    print(f"\nData to be Plotted:\n\n{df}")

    # Plotting Graph

    p = sns.regplot(data=df, x="expenditure", y="sales", scatter=True, fit_reg=True)
    p.set_xlabel("Expenditure")
    p.set_ylabel("Sales")
    plt.show()

    return