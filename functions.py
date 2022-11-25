# ---- Importing All Needed ----

import csv
import pandas as pd
import datetime
from graph1 import read_data
from graph1 import graph_exp_month
from graph2 import *
from graph3 import *


# ---- Read sales.csv data ----
spreadsheet = pd.read_csv('sales.csv')

# ORGANISING

# --- Organising: Sorts spreadsheet rows by year and month columns ----

spreadsheet = spreadsheet.iloc[
    pd.to_datetime(spreadsheet.year.astype(str) + spreadsheet.month, format='%Y%b').argsort()]
spreadsheet.to_csv('sales.csv', index=False)

# ADDING NEW COLUMNS

# ---- Adds new column with monthly percentage changes in sales data ----

spreadsheet['monthly_percentage_change'] = spreadsheet['sales'].pct_change()
spreadsheet.to_csv('sales.csv', index=False)

# ---- Adds new 'profit' column by subtracting the 'expenditure' column from the 'sales' column ----

spreadsheet['profit'] = spreadsheet['sales'] - spreadsheet['expenditure']
spreadsheet.to_csv('sales.csv', index=False)


# ---- Adds new 'status' column / whether month made profit or loss ----

def profit_status(x):
    if x > 0:
        x = 'Profit'
    elif x <= 0:
        x = 'Loss'
    return x


spreadsheet['status'] = spreadsheet['profit'].apply(profit_status)
spreadsheet.to_csv('sales.csv', index=False)

# FUNCTIONS
# ---- Function to Read Data (using csv, not pandas) ----


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        sheet = csv.DictReader(sales_csv)

        for row in sheet:
            data.append(row)

    return data


# ---- Function to Read and Print SALES data ----
def read_sales():
    data = read_data()

    # Used pandas to determine average sales, sum, highest & lowest value.

    avg_sales = spreadsheet['sales'].mean()
    sum_sales = spreadsheet['sales'].sum()
    maximum_sales = spreadsheet['sales'].max()
    minimum_sales = spreadsheet['sales'].min()

    # Determining Month with the highest/lowest sale.

    data.sort(key=lambda x: x['sales'])
    month_max_sales = data[-1]['month'] + ' ' + data[-1]['year']
    month_min_sales = data[0]['month'] + ' ' + data[0]['year']

    # This outputs the MONTH and the YEAR - Better if new data is added.

    # Printing All

    print(f"\nAverage sales: {avg_sales:.2f}")
    print(f"Total sales: {sum_sales:.2f}")
    print(f"Highest sales: {maximum_sales:.2f}")
    print(f"Month with highest sales: {month_max_sales.title()}")
    print(f"Lowest sales: {minimum_sales:.2f}")
    print(f"Month with lowest sales: {month_min_sales.title()} \n")


# ---- Function to Read and Print EXPENDITURE data ----

def read_exp():
    data = read_data()

    # Determine average expenditure, sum, highest & lowest value.
    avg_exp = spreadsheet['expenditure'].mean()
    sum_exp = spreadsheet['expenditure'].sum()
    maximum_exp = spreadsheet['expenditure'].max()
    minimum_exp = spreadsheet['expenditure'].min()

    # Determining Month with the highest/lowest exp.
    data.sort(key=lambda x: x['expenditure'])
    month_max_exp = data[-1]['month'] + ' ' + data[-1]['year']
    month_min_exp = data[0]['month'] + ' ' + data[0]['year']

    # Printing All
    print(f"\nAverage expenditure: {avg_exp:.2f}")
    print(f"Total expenditure: {sum_exp:.2f}")
    print(f"Highest expenditure: {maximum_exp:.2f}")
    print(f"Month with highest expenditure: {month_max_exp.title()}")
    print(f"Lowest expenditure: {minimum_exp:.2f}")
    print(f"Month with lowest expenditure: {month_min_exp.title()} \n")


# ---- Function to Read and Print PROFIT Data ----

def read_profit():
    data = read_data()

    # Determine average profit, sum, highest & lowest value.
    avg_profit = spreadsheet['profit'].mean()
    sum_profit = spreadsheet['profit'].sum()
    maximum_profit = spreadsheet['profit'].max()
    minimum_profit = spreadsheet['profit'].min()

    # Determining Month with the highest/lowest profit.
    data.sort(key=lambda x: int(x['profit']))
    month_max_profit = data[-1]['month'] + ' ' + data[-1]['year']
    month_min_profit = data[0]['month'] + ' ' + data[0]['year']

    # Lists of profitable or unprofitable months with month, year & profit columns data.
    profitable_months = spreadsheet.loc[spreadsheet['status'] == 'Profit', ('month', 'year', 'profit')]
    unprofitable_months = spreadsheet.loc[spreadsheet['status'] == 'Loss', ('month', 'year', 'profit')]

    # Printing all
    print(f"\nAverage profit: {avg_profit:.2f}")
    print(f"Total profit: {sum_profit:.2f}")
    print(f"Highest profit: {maximum_profit:.2f}")
    print(f"Month with highest profit: {month_max_profit.title()}")
    print(f"Lowest profit: {minimum_profit:.2f}")
    print(f"Month with lowest profit: {month_min_profit.title()} \n")
    print(f"\nAll profitable months:\n {profitable_months}")
    print(f"\nAll unprofitable months:\n {unprofitable_months}")


# Function to read and print percentage variation data.
# Note: If possible, figure how to display
# A. All months with % increase (Done)
# B. All months with % decrease (Done)
# C. Reference to period of change, ie 'from Jun 2018 to Jul 2018 (No Time)

def read_percentage():

    avg_percentage = spreadsheet['monthly_percentage_change'].mean()
    max_per_increase = spreadsheet['monthly_percentage_change'].max()
    max_per_decrease = spreadsheet['monthly_percentage_change'].min()

    # Determining Month with the highest/lowest % variation

    sorted_df = spreadsheet.sort_values(by=["monthly_percentage_change"], ascending=True)
    # This sorts the spreadsheet in ascending order by % variation.

    date_max_decrease = str(sorted_df.iloc[0, 1]).title() + ' ' + str(sorted_df.iloc[0, 0])
    # Sets date_max_increase to row 0 (first row) column 1(month) + space + row 0 column 0(year)
    # Must convert the sorted_df.iloc values to string, so they can concatenate!

    date_max_increase = str(sorted_df.iloc[-2, 1]) + ' ' + str(sorted_df.iloc[-2, 0])
    # Sets date_max_decrease to row -2 (2nd-to-last) column 1(month) + space + row -2 column 0(year)
    # Convert to string, so it can concatenate.

    # Create list with month+year+% data for months with positive % change, and another for negative % change.
    positive_var = spreadsheet.loc[
        spreadsheet['monthly_percentage_change'] >= 0, ('month', 'year', 'monthly_percentage_change')]
    negative_var = spreadsheet.loc[
        spreadsheet['monthly_percentage_change'] < 0, ('month', 'year', 'monthly_percentage_change')]

    # Printing all
    print(f"\nAverage change in monthly sales by percentage: {avg_percentage:.2f}% \n")
    print(f"Highest increase in monthly sales by percentage: {max_per_increase:.2f}%")
    print(f"Month with the highest increase in monthly sales by percentage: {date_max_increase.title()} \n")
    print(f"Highest decrease in monthly sales by percentage: {max_per_decrease:.2f}%")
    print(f"Month with the highest decrease in monthly sales by percentage: {date_max_decrease.title()} \n")

    print(f"Months with an increase in monthly sales by percentage:\n\n{positive_var}")
    print(f"\nMonths with a decrease in monthly sales by percentage:\n\n{negative_var}")
    return


# ---- Function to AMEND existing data ----
def amend_data():

    # Reading the csv file
    df = pd.read_csv("sales.csv")

    print(f"Current Data:\n\n{df}")

    data_type = input("\nWhich data type would you like to amend? year/month/sales... ")
    row_num = input("\nWhich row number would you like to amend? ")
    new_value = input(f"\nPlease input the new {data_type} information for row {row_num}: ")

    column_name = data_type
    row_number = row_num

    # Updating the column value/data
    df.loc[int(row_number), column_name] = new_value

    # Writing into the file
    df.to_csv("sales.csv", index=False)

    # Printing amended Data.
    print(f"\nAmended Data:\n\n{df}")


# ---- Function to ADD NEW ROW of Data ----

def add_new_row():
    from csv import writer
    new_row = []
    print("Please enter data for the new row below.\n")

    # Collect input
    new_year = int(input("New Year: "))
    new_month = input("New Month (First three letters): ").lower()
    new_sales = int(input("New Sales Data: "))
    new_exp = int(input("New Expenditure Data: "))

    # Append rows w/ input
    new_row.append(new_year)
    new_row.append(new_month)
    new_row.append(new_sales)
    new_row.append(new_exp)

    # Append sales.csv file
    with open('sales.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new_row)

        f_object.close()
    return


# NOTE: Very basic. Doesn't give out any error messages or ensure the data one inputs is valid in any way.


# USER INPUT

# ---- User Input: Command Action Choice ----

def user_action_choice():
    while True:
        try:
            user_command = str(input("\nPlease tell us what you would like to do: ")).lower()
            command_list = user_command.split()
            print(f"Your command: {command_list}")
            # The command list is being printed here just so we can see it working.

            graph_choice = ['graph', 'graphs', 'plot']

        except ValueError:  # Case: Not string
            print("Oh-oh! Try again!")
            continue

        if 'read' in command_list:

            if 'amend' in command_list or 'append' in command_list or 'add' in command_list or any(item in command_list for item in graph_choice):
                print("Please pick one action at a time!\n")
                continue

            elif 'sales' in command_list and (
                    'profit' in command_list or 'expenditure' in command_list or 'percentage' in command_list):
                print("\nYou can only read one type of data at a time! Please try again.")
                continue

            elif 'profit' in command_list and ('expenditure' in command_list or 'percentage' in command_list):
                print("\nYou can only read one type of data at a time! Please try again.\n")
                continue

            elif 'expenditure' in command_list and 'percentage' in command_list:
                print("\nYou can only read one type of data at a time! Please try again.\n")
                continue

            elif 'sales' in command_list:
                print("\n Sales Data:")
                read_sales()
                break

            elif 'profit' in command_list:
                print("\n Profit Data:")
                read_profit()
                break

            elif 'expenditure' in command_list:
                print("\n Expenditure Data:")
                read_exp()
                break

            elif 'percentage' in command_list:
                print("\n Percentage Data:")
                read_percentage()
                break

            else:  # Case: action not specified - only 'read'
                data_choice = input(
                    "\nPlease pick which data to read. You can read data on Sales, Profit, Expenditure or Monthly Sales Percentage Change: \n ").lower()

                if data_choice == 'sales':
                    print("\n Sales Data:")
                    read_sales()
                    break

                elif data_choice == 'profit':
                    print("\n Profit Data:")
                    read_profit()
                    break

                elif data_choice == 'expenditure':
                    print("\n Expenditure Data:")
                    read_exp()
                    break

                elif data_choice == 'percentage':
                    print("\n Percentage Data:")
                    read_percentage()
                    break

                else:
                    print(
                        "Invalid Input! Please try again.\n"
                        "Remember to:\n"
                        " (1) Pick one action at a time, and\n"
                        " (2) Specify the type of data you want to read\n"
                        "    (i.e. 'read sales data')")
                    continue

        elif 'amend' in command_list:
            if 'add' in command_list:
                print("\nPlease pick either to amend existing data OR add new data!")
            else:
                print("\n Current Data: ")
                amend_data()
                break

        elif 'add' in command_list:
            print("\n")
            add_new_row()
            break

        elif any(item in command_list for item in graph_choice):
            print("\n"
                  "Your graph options are:\n"
                  " (1) Expenditure per Month;\n"
                  " (2) Expenditure per Sales;\n"
                  " (3) Sales per Month.\n"
                  "")
            graph_no = None

            while graph_no != (1, 2 or 3):
                try:
                    graph_no = int(input("Please input a number for the graph you wish to plot: "))

                    if graph_no == 1:
                        print("\nPlotting Expenditure per Month Data...")
                        graph_exp_month()
                        break

                    elif graph_no == 2:
                        print("\nPlotting Expenditure per Sales Data...")
                        graph_exp_sales()
                        break

                    elif graph_no == 3:
                        print("\nPlotting Sales per Month Data...")
                        graph_month_sales()
                        break

                except ValueError:
                    print("\nInvalid input!\n"
                          "Please input a number between 1 to 3 depending on the graph you wish to plot!\n")
                    continue
        else:
            print("\nThat's not a valid command! Try again!")
            continue
        return

# ---- Functions: User Input: Choice to Continue Program ----


def continuing_action():
    while True:
        try:
            yes = ['y', 'yes', ',y', ',yes', 'y,', 'yes,']
            no = ['n', 'no', ',n', ',no', 'n,', 'no,']
            # Very rudimentary solution to avoid common errors.

            continuing_choice = str(input("\nWould you like to do anything else? (y/n) ")).lower()
            continuing_command_list = continuing_choice.split()
            print(f"Your command: {continuing_command_list}")  # Prints command so we can see what is happening.
            # This asks for user input, then splits the strings into a list.

            yes_choice = any(item in continuing_command_list for item in yes)
            no_choice = any(item in continuing_command_list for item in no)
            # Checking if any item in command list above matches any item of both 'yes' and 'no' lists.

            if no_choice and yes_choice:
                # If commands contain elements of both 'yes' and 'no', the program will pick a random choice.
                import random
                maybe = random.randint(1, 2)

                if maybe == 1:
                    random_choice = 'Yes'
                else:
                    random_choice = 'No'
                print(f"\nYes and no means MAYBE! \n"
                      f"Your randomly generated choice: {random_choice}.")
                # Just a little fun way to incorporate what we learned about random and the randint() function.

                if random_choice == 'Yes':
                    user_action_choice()
                    continue

                else:
                    print(
                        "\nThat is okay! We hope you've enjoyed our program.\n"
                        "Please run it again if you change your mind!")
                    break

            elif yes_choice:
                user_action_choice()
                continue

            elif no_choice:
                print(
                    "\nThat is okay! We hope you've enjoyed our program.\nPlease run it again if you change your mind!")
                break

            else:
                print("\nHm, that is not a valid command. Please try again!")

        except ValueError:
            print("\nOops, try again!")
            continue
        # This doesn't really work with strings.

    return
