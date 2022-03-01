#!/usr/bin/env python

from msilib.text import tables
from flask import Flask, json, render_template, request, send_file
import os
import pandas as pd
from read_site import antiques_scrape
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# create instance of Flask app
app = Flask(__name__)

# decorator

# initial page which gives instructions on use


@app.route("/")
def echo_hello():
    return app.send_static_file('instruct.html')

# if the file doesn't exist yet, a message will be give to use /scrape first


@app.route("/all")
def all():
    try:
        data = pd.read_csv("antiques_cl.csv")
        return data.to_html(header='true', table_id=tables)
    except FileNotFoundError:
        return "Use /scrape first to obtain data"
    except AttributeError as e:
        return e

# endpoint that calls the function to pull back data from craigslist for columbia/jeff city


@app.route("/scrape")
def read_site():
    # return "Trying to scrape"
    df = antiques_scrape()
    return df


if __name__ == "__main__":
    app.run(debug=True)
