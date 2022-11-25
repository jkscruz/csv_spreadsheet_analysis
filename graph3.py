# ---- MONTH / SALES GRAPH (3) ----
import seaborn as sns
import csv
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        sp = csv.DictReader(sales_csv)
        for row in sp:
            data.append(row)

    return data

# ---- Function to Plot Sales/Month Graph ----


def graph_month_sales():
    data = read_data()

    # Transforming the Data
    df = pd.DataFrame.from_dict(data)  # Create Pandas DataFrame containing the data
    df = df.iloc[pd.to_datetime(df.year.astype(str) + df.month, format='%Y%b').argsort()]  # Sort by YEAR mon

    df[
        'month_num'] = df.index
    # Create new column of data numbering each month
    df['sales'] = df['sales'].astype("int")
    # Change the data type of the sales from float (decimal) to integer
    print(f"\nData to be Plotted:\n\n{df}")

    # Plotting Graph

    p = sns.regplot(data=df, x="month_num", y="sales", scatter=True, fit_reg=True)
    p.set_xlabel("Month")  # so it doesn't say "month_num"
    p.set_ylabel("Sales")
    p.set_xticks(
        [i for i in range(len(df))])  # position the xticks OR p.set_xticks(df['month_num']) # position the xticks
    p.set_xticklabels(df['month'] + ' ' + df['year'])  # set the x tick labels to the month names
    plt.show()

    return
