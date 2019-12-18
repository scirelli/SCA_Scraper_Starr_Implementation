# DOCUMENTATION ------------------------------------------------
'''
Description:    Module to house the utility functions for this program.

'''

# LOAD LIBRARIES -----------------------------------------------

# Python
import subprocess
import sys
import pkg_resources
# import mysql.connector


# FUNCTIONS - INSTALL DEPENDENCIES -----------------------------


def install_dependency(package, version):

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '{0}=={1}'
                           .format(package, version)])


def get_list_installed_pkgs():
    'Description: return list of installed packages on host comp'
    # Logging

    # Get list of installed packages
    list_pkgs = list(pkg_resources.working_set)

    # Return List of Installed Packages
    return list_pkgs


def setup_dependencies():
    required_pkgs = ['pandas==0.25.3', 'mysql-connector==2.1.6',
                     'beautifulsoup4==4.8.0', 'urllib3==1.22',
                     'nltk==3.2.4']

    # Logging
    print('The following dependencies are required to run this program {}\n'.format(required_pkgs))
    resp = input('Do you want to check for and install these packages? ')

    # Check Dependencies & Install Missing Packages
    if resp == 'Yes' or resp == 'yes':

        # Cross Reference Installed Packages, Install Missing P's
        list_installed_pkgs = get_list_installed_pkgs()

        # Dependencies Installed
        list_deps_installed = []

        # Iterate Dependencies
        for dependency in required_pkgs:
            # Split package name into name + version
            pkg_split = dependency.split('==')
            pkg_name = pkg_split[0]
            pkg_version = pkg_split[1]

            if dependency not in list_deps_installed:
                install_dependency(pkg_name, pkg_version)
                list_deps_installed.append(dependency)
        # Logging
        print('\nThe following dependencies are or were installed => {}'
              .format(list_deps_installed))

    # Logging
    else:
        print('Dependencies will not be installed\n')

    # End
    pass


# FUNCTIONS - SETUP DATABASE --------------------------------------------

def setup_database():
    db_program = input('\nWhich database are you using (MySQL or SQL_Server)? ')
    if db_program == 'MySQL':
        db_name = input('Please choose a short name for your db. ')
        print('\nConnecting to local instance of MySQL')
        # Connect to Database
        mydb = mysql.connector.connect(host="localhost", user=input('Username => '),
                                       passwd=input('Password => '))
        mycursor = mydb.cursor()
        mycursor.execute('CREATE DATABASE {}'.format(db_name))
        # Logging
        print('Database -{}- was successfully created'.format(db_name))
        # Return database name
        return db_name

    # SQL Server
    elif db_program == 'SQL_Server':
        pass

    # DB Not Recognized
    else:
        db_name = input('Database not recognized.  Please input db name manually => ')
        return db_name

    # Return None
    return None


def setup_sql_table(db_name):
    raise Exception('wtf is this shit')
    # Define Table Name
    table_name = input('Please specify the name for your table => ')
    # Create Table
    mydb = mysql.connector.connect(host="localhost",
                                   user=input('Username => '),
                                   passwd=input('Password => '),
                                   database=input('Database => '))
    mycursor = mydb.cursor()
    mycursor.execute('''

    '''.format(table_name))

    # Logging
    print('Table -{}- set up successfully'.format(table_name))

    # End
    return None


def program_setup():
    # Run Setup
    resp_setup = input('Do you want to run setup to install packages & create a database? ')
    if resp_setup == 'yes' or resp_setup == 'Yes':

        # Verify & Install Dependencies
        resp_pkgs = input('Do you want to check for and install dependencies? ')
        if resp_pkgs == 'yes' or resp_pkgs == 'Yes':
            setup_dependencies()

        # Create Database
        resp_db = input('Do you want to set up a database? ')
        if resp_db == 'yes' or resp_db == 'Yes':
            db_name = setup_database()
        else:
            db_name = input('Please input the name of your database => ')

        # Create Table
        resp_table = input('Do you want to automatically create the table? ')
        if resp_table == 'yes' or resp_table == 'Yes':
            setup_sql_table(db_name)

        # Logging
        print('\n **** Setup complete.  Have fun!!!!!  ****')

    # Logging
    print('\nProceeding to connect to mysql and run program')


def instantiate_connection_to_db(user):

    # Try Connecting
    print('Instantiating connection to database => {}'.format(database))
    mydb = mysql.connector.connect(
        host="localhost",
        user=user,
        passwd=input('Password => '),
        database=input('Database => '))
    print('Connection established\n')

    # Return Connection Object
    return mydb
