import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

# try the direct API stuff
# 

mySite = "minicab"  # just the name

class boboTest:

    def fullUrl():
        return "http://" + mySite + "/"

    def try_just_onetest():
        """Queries the weather API and returns the weather data for a particular city."""
        print('request starting....')

    
