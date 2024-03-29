# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:05:20 2024

@author: student
"""
def evaluate_expression(expression, variables):
    """
    Evaluates a logical expression using a truth table.

    Args:
        expression (str): The logical expression (e.g., "P and Q").
        variables (list): List of variable names (e.g., ["P", "Q"]).

    Returns:
        list: A list of dictionaries representing the truth table.
    """
    num_vars = len(variables)
    truth_table = []

    for i in range(2 ** num_vars):
        row = {}
        for j, var in enumerate(variables):
            row[var] = (i >> (num_vars - j - 1)) & 1
        row["Result"] = eval(expression, row)
        truth_table.append(row)

    return truth_table

# Example usage:
logical_expression = "(P and Q) or (not R)"
variable_names = ["P", "Q", "R"]
result = evaluate_expression(logical_expression, variable_names)

# Print the truth table
for row in result:
    print(row)
