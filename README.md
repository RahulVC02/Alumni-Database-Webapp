# DBMS Assignment 3 - Alumni Database Webapp

## Made with Flask and MySQL

G1 already populated the database with dummy/imaginary values into it in the Assignment 2 submission. The dump file was also submitted in the Assignment 2.


## Setup (G1 and G2)

1. Install Python 3.6.5 or above

2. Install MySQL 5.7 or above

3. Install the required packages for python: 

    ```bash
    pip install flask
    pip install flask-mysql
    pip install flask-session
    pip install pymysql
    pip install cryptography
    ```

    Run the above commands in the terminal in order to install the required packages.

4. Create a database named `alumni` in MySQL

    In order to do this, run the 'database_dump' file in the 'Dump Files' directory in your SQL Workbench. This will create the database and populate it with the required tables and data. 

5. Create a database named `users` in MySQL

    In order to do this, run the 'users_database_dump' file in the 'Dump Files' directory in your SQL Workbench. This will create the database and populate it with the required tables and data.

6. Create a new user 'student' in your MYSQL Workbench.
    
    In order to do this, do the following:
    
    - Login in to MYSQL Workbench using your root user.
    - Click on the 'Administration' tab. ![Administration Tab](/Photos_Readme/Tut-1.png)
    - Click on the 'Users and Privileges' option.
    - Click on the 'Add Account' button.
    - Enter the following details keeping the rest of the fields as default:
        - Login Name: `student`
        - Password: `Pass@1234`

    - Click on the 'Apply' button. ![Tut-2](/Photos_Readme/Tut-2.png)

    - Click on 'Administrative Roles' and then click on 'Revoke All Privileges'. ![Tut-3](/Photos_Readme/Tut-3.png) 

    - Click on 'Schmema Privileges' and then click on 'Revoke All Privileges'. ![Tut-4](/Photos_Readme/Tut-4.png)

    - Go to your home tab in Workbench and then add a new connection by clicking here: ![Tut-5](/Photos_Readme/Tut-5.png) 

    - Here Enter the following:
        - Connection Name: `student`
        - Username: `student`
    
    - Click on 'Test Connection' and then enter the password `Pass@1234` when prompted. Then click on 'OK'.

7. Repeat the entire above point for a new user 'employee' in your MYSQL Workbench with the following details:
    - Login Name: `employee`
    - Connection Name: `employee`
    - Username: `employee`
    - Password: `Pass@5678`

8. Grant Permissions to the 'student' role. 

    In order to do this, run the 'student_role_permissions' file in the 'Dump Files' directory in your SQL Workbench. This will grant the required permissions to the 'student' role.

9. Grant Permissions to the 'employee' role. 

    In order to do this, run the 'employee_role_permissions' file in the 'Dump Files' directory in your SQL Workbench. This will grant the required permissions to the 'employee' role.

10. Now we need the update the credentials in the 'credentials. yaml' file.

    Here in 'mysql_password1' field, enter the password of your root user in MySQL. In 'mysql_password2' and 'mysql_password3' fields, enter the passwords of the 'student' and 'employee' users respectively which we decided above.

    Make sure you have the following credentials in the 'credentials.yaml' file:

    ```yaml
    mysql_host: 'localhost'
    mysql_user1: 'root'
    mysql_user2: 'student'
    mysql_user3: 'employee'

    mysql_password1: 'Your SQL Root Password'
    mysql_password2: 'Pass@1234'
    mysql_password3: 'Pass@5678'

    mysql_db: 'alumni'
    login_db: 'users'
    ```


## Running the Webapp

Now that we have setup the database and the credentails, we can run the webapp.

1. Open the terminal and navigate to the directory where the 'web_app.py' file is located.

2. Run the following command in the terminal:

    ```bash
    python web_app.py
    ```
    or 
    ```bash
    python3 web_app.py
    ```
    depending on your python version.

    Or you can simply click on the 'Run' button in your IDE for the 'web_app.py' file.

3. Open your browser and go to the URL that is displayed in the terminal, like this:

    ```bash
    http://127.0.0.1:4999
    ```
    
This will open the home page of the webapp.

### Welcome Screen
 ![Welcome Screen](/Photos_Readme/Welcome.png)
### Tables
1. Admin
 ![Admin tables](/Photos_Readme/admin_tables.png)
2. Employee
 ![Employee tables](/Photos_Readme/employee_tables.png)
4. Student
 ![Student tables](/Photos_Readme/Students_tables.png)
### Operations
1. Insert
    Before ![Insert Before](/Photos_Readme/Insert_1.png)
    After ![Insert After](/Photos_Readme/Insert_2.png)
2. Update
    Before ![Update Before](/Photos_Readme/Update_1.png)
    After ![Update After](/Photos_Readme/Update_2.png)
3. Delete
    Before ![Delete Before](/Photos_Readme/d1.png)
    After ![Delete After](/Photos_Readme/d2.png)
4. Rename
    Before ![Rename Before](/Photos_Readme/Rename_1.png)
    After ![Rename After](/Photos_Readme/Rename_2.png)
5. Where
    Where is being implemeted in the above examples.
## Work Distribution

Rahul Chembakasseril
1) Worked on the backend implementation of routes and integration of Flask with MySQL.
2) Helped setup basic frontend wireframe to provide proof of concept.

Kanishk Singhal
1) 
2) 

Inderjeet Singh Bhullar
1) 
2)

Kalash Kankaria
1)
2)

Joy Makwana
1) 
2)

Medhansh Singh
1) Developed Front-end using HTML, CSS and Tailwind CSS.
2) Tested the webapp to check if it supports dynamic operations.
3) Documented the testing output in the ReadMe.MD file.

Nokzendi Aier
1)
2)

Bhavesh Jain
1)
2)

Harshvardhan Vala
1)
2)

Dhairya Shah
1) Worked on the frontend of the WebApp using tailwind. 
2) Testing views, clicked screenshots of successful executions, and documented them in readme.
