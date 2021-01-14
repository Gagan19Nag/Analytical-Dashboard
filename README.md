# Analytical-Dashboard

## Applications/ Softwares/ Packages needed to run code	<br />
1. For Database we have used PostgreSQL Version 13.1 <br />
2. Python 3.9 <br />
3. Python IDE - PyCharm<br />
4. flask - Flask is a popular Python web framework used for developing web applications.<br />
5. psycopg2  - Psycopg is the most popular PostgreSQL database adapter for the Python programming language<br />


### Steps to Install PostgreSQL <br />
Step 1) Go to https://www.postgresql.org/download and select operating system<br/>
Step 2) You are given two options<br/>
-------- Interactive Installer by EnterpriseDB and Graphical Installer by BigSQL 
--------Select Interactive Installer by EnterpriseDB<br />
Step 3) You will be prompted to desired PostgreSQL version and operating system. <br />
------- Select the latest PostgreSQL version and OS as per your environment<br />
--------click the Download Button and Download will begin<br />
Step 4) Once you Download PostgreSQL, open the downloaded exe and Click next on the install welcome screen.<br />
Step 5) On the next screen, Change the Installation directory if required, else leave it to default and click Next<br />
Step 6) On the next screen, Choose the components you want to install in your system, uncheck Stack Builder and click Next<br />
Step 7) On the next screen, You may change the data location if required, else leave it to defaut and click next <br />
Step 8) On the next screen, Enter super user password. Make a note of it, this is required in future click Next.<br />
Step 9) On the next screen, Leave the port number default, Click Next.<br />
Step 10) On the next screen, Check the pre-installation summary: Click Next<br />
Step 11) Once install is complete you will see the Stack Builder prompt, Uncheck that option. click Finish<br />
Step 12) To launch PostgreSQL go to Start Menu and search pgAdmin 4


### Steps to Install Python 3.9<br />
Step 1) Go to https://www.python.org/downloads/ and click on Download Python 3.9.1 select x86-64 executable installer for 64bit system or x86 executable installer for 32bit system<br />
Step 2) Run the Python Installer once downloaded. <br />
Step 3) Select Add Python 3.7 to PATH checkboxes.<br />
Step 4) Select Install Now – the recommended installation options.(this will install pip and IDEL too)<br />
Step 5) Once the installation complete window shows click on finish<br />
Step 6) Verify Python Was Installed On Windows<br />
--------Navigate to the directory in which Python was installed on the system<br />
--------Double-click python.exe.<br />
--------Output should show python version<br />
Step 7) Verify Pip Was Installed<br />
--------Open the Start menu and type “cmd.”<br />
--------Select the Command Prompt application.<br />
--------Enter pip -V in the console. If Pip was installed successfully, you should see pip version<br />


### Steps to Install PyCharm<br />
Step 1) Go to https://www.jetbrains.com/pycharm/download/ and Click the DOWNLOAD link under the Professional Section.<br />
Step 2) Once the download is complete, run the exe for install PyCharm. The setup wizard should have started. Click Next.<br />
Step 3) On the next screen, Change the installation path if required. Click Next.<br />
Step 4) On the next screen, you can create a desktop shortcut if you want and click on Next.<br />
Step 5) Choose the start menu folder. Keep selected JetBrains and click on Install.<br />
Step 7) Once installation finished, you should receive a message screen that PyCharm is installed. click “Finish”.<br />


### Steps to Install flask framework<br />
Step 1) Open the Start menu and type “cmd.”<br />
--------Select the Command Prompt application.	<br />
Step 2) type "pip install flask"<br />


### Steps to Install psycopg2 framework<br />
Step 1) Open the Start menu and type “cmd.”<br />
--------Select the Command Prompt application.	<br />
Step 2) type "pip install psycopg2"<br />


## After Installing the above Applications/ Softwares/ Packages, to run the code we need to follow below steps<br />

#### For Database : <br />
Step 1) Download the PIS Project Folder from GitHub<br />
Step 2) Go to Database Queries and Tables folder under PIS Project<br />
Step 3) Open PgAdmin application<br />
Step 4) Under database, right click on database option go to create and click on create schema and create protected, sales_raw, sales_anl and rbac schemas<br />
Step 5) Navigate to sales_raw schema under database and right click on it and go to create table and enter table name as sales_raw_table<br />
Step 6) Navigate to sales_raw_table under sales_raw schema and right click on it and select import/export option <br />
Step 7) On the new screen, select import option and choose path for file where sales_raw_table is preset i.e PIS Project/Database Queries and Tables/sales_raw/sales_raw_table<br />
Step 8) Select format as csv and header Yes leave rest option as it is and click Ok<br />
Step 9) Open Query tool and copy paste the queries present in PIS Project/Database Queries and Tables/sales_anl and execute them<br />
Step 10) Navigate to rbac schema under database and right click on it and go to create table and create tables role, role_hierarchy, permission, permission_role_assignment, users, user_role_assignment<br />
Step 11) Navigate to above created tables under rbac schema and right click on it and select import/export option <br />
Step 12) On the new screen, select import option and choose path for file where above tables is preset i.e PIS Project/Database Queries and Tables/rbac/tables<br />
Step 13) Select format as csv and header Yes leave rest option as it is and click Ok<br />
Step 14) Open Query tool and copy paste the queries present in PIS Project/Database Queries and Tables/rbac/view and execute them<br />
Step 15) Navigate to protected schema under database and right click on it and go to create table and enter table name as user_auth <br />
Step 16) Navigate to user_auth table under protected schema and right click on it and select import/export option <br />
Step 17) On the new screen, select import option and choose path for file where sales_raw_table is preset i.e PIS Project/Database Queries and Tables/protected/user_auth<br />
Step 18) Select format as csv and header Yes leave rest option as it is and click Ok<br />


#### For Server :<br />
Step 1) Download the PIS Project Folder from GitHub<br />
Step 2) Open pycharm application<br />
Step 3) Go to File under file select Open and choose path to folder PIS Project/Analytical Dashboard<br />
Step 4) Click on Ok <br />
Step 5) Once project is opened click on run <br />

## Dependencies :
1. Database server should be running when we are running flask code.<br />

