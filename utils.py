from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

# Desc: Utility functions for the webapp


# return a HTML table of all the tables in the database
def my_sql_to_html_table():
    
    

