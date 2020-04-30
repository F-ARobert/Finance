from math import log as log

##########################################
# Converts float to string as percentage
# Parameters: Value to convert
#
# Returns:    Percentage as string


def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)

########################################
# Calculates a simple rate of return
# Parameters: Start price
#             End price
#             Dividends earned (optional, default 0)
#
# Returns:    Rate of return


def calculate_simple_return(start_price, end_price, dividend=0):
    return (end_price - start_price + dividend)/start_price

########################################
# Calculates a compounded rate of return
# Parameters: Start price
#             End price
#
# Returns:    Continuous rate of return


def calculate_log_return(start_price, end_price):
    return log(end_price/start_price)

########################################
# Annualizes returns over a year
# Parameters: log_return: Compounded return of time period
#             t: the number of original periods in the new time period
#
# Returns:    Annualized return


def annualize_return(log_return, t):
    return log_return * t


########################################
# Converts list of eturns over a specified time period
# Parameters: log_return: a list of returns
#             t: the number of original time periods the new time period
#                Example, there are 252 trading days in a typical year
#
# Returns:    Annualized return


def convert_returns(log_return, t):
    return sum(log_return)/len(log_return) * t


########################################
# Calculates variance of a list
# Parameters: list: iterable list of values (in or float)
#
# Returns:    Annualized return


def calculate_variance()
