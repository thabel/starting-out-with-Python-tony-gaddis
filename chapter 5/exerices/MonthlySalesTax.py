from app_frame import app_frame

"""
A retail company must file a monthly sales tax report listing the total sales for the month, 
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent 
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter 
the total sales for the month. From this figure, the application should calculate and display 
the following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
"""
STATE_TAX_PERCENT = 5 / 100
COUNTY_TAX_PERCENT = 2.5 / 100


def monthlySalesTax():
    total_sales_for_month = float(input("Enter the total sales for the month:  "))
    county_sales_tax = total_sales_for_month * COUNTY_TAX_PERCENT
    state_sales_tax = total_sales_for_month * STATE_TAX_PERCENT
    print("The amount of county sales tax .................... ", round(county_sales_tax, 2))
    print("The amount of state sales tax  .....................", round(state_sales_tax, 2))
    print("The total sales tax ................................", round(county_sales_tax + state_sales_tax, 2))
    print()


app_frame(monthlySalesTax)
