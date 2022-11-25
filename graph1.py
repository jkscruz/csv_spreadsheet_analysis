# ---- EXPENDITURE / MONTH GRAPH (1) ----

import seaborn as sns
import csv
import pandas as pd  # Seaborn likes to receive the data in a special DataFrame format in the Pandas library
import matplotlib.pyplot as plt  # the Seaborn library needs matplotlib.pyplot to show the

# FUNCTIONS
# --- Loading the Data (csv) --


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        sp = csv.DictReader(sales_csv)
        for row in sp:
            data.append(row)

    return data


# ---- Function to Plot Expenditure/Month Graph ----
def graph_exp_month():
    data = read_data()

    # or simply: df = pd.read_csv('sales.csv') --->use this easier line for other graphs

    # Transforming the Data

    df = pd.DataFrame.from_dict(data)  # Create Pandas DataFrame containing the data
    df = df.iloc[
        pd.to_datetime(df.year.astype(str) + df.month, format='%Y%b').argsort()]
    # Sorted the dataframe by month + year
    # Already did this in 'main'

    df[
        'month_num'] = df.index
    # Create new column of data numbering each month (for doing the line of best fit)
    df['expenditure'] = df['expenditure'].astype(
        "int")
    # Change the data type of the expenditure from float (decimal) to integers

    print(f"\nData to be Plotted:\n\n{df}")

    # Plotting Graph

    p = sns.regplot(data=df, x="month_num", y="expenditure", scatter=True, fit_reg=True)
    p.set_xlabel("Month")  # so it doesn't say "month_num"
    p.set_ylabel("Expenditure")
    p.set_xticks(
        [i for i in range(len(df))])  # Position the xticks OR p.set_xticks(df['month_num']) # Position the xticks
    p.set_xticklabels(df['month'] + ' ' + df['year'])
    # Set the x tick labels to the month names
    plt.show()

    return
