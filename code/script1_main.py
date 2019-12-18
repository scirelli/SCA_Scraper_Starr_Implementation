# DOCUMENTATON -------------------------------------------------
'''
Description:    This script contains the required dependencies for the SCA Scraper 
                and the driver function that controls it. 

'''

# LOAD PROJECT PACKAGES ----------------------------------------
import module0_setup as m0

# SETUP --------------------------------------------------------
m0.program_setup()

# LOAD PYTHON PACKAGES -----------------------------------------

import mysql.connector
import pandas as pd
import nltk
import re
import string
from nltk.stem import *
stemmer = PorterStemmer()
from nltk import corpus
import nltk
from datetime import datetime
import logging


# INSTANTIATE CONNECTION TO DATABASE --------------------------
#m0.instantiate_connection_to_db('ccirelli2', 'Work4starr!', 'SCA_DATABASE_STARR')





























