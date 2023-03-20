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
    * Before ![Insert Before](/Photos_Readme/Insert_1.png)
    * After ![Insert After](/Photos_Readme/Insert_2.png)
2. Update
    * Before ![Update Before](/Photos_Readme/Update_1.png)
    * After ![Update After](/Photos_Readme/Update_2.png)
3. Delete
    * Before ![Delete Before](/Photos_Readme/d1.png)
    * After ![Delete After](/Photos_Readme/d2.png)
4. Rename
    * Before ![Rename Before](/Photos_Readme/Rename_1.png)
    * After ![Rename After](/Photos_Readme/Rename_2.png)
5. Where
    * Where is being implemented in the above examples.
### Views

1) Alumni Details 
![image](https://user-images.githubusercontent.com/76472249/226408985-b8e5df26-9cc3-47b2-8509-0e8d888ca370.png)
2) Alumni Education
![image](https://user-images.githubusercontent.com/76472249/226409015-4c16934c-c92b-416f-822b-40bf26b16be6.png)
3) Alumni Achievements
![image](https://user-images.githubusercontent.com/76472249/226409040-94d52a05-016c-4f4b-94f9-4d1446ab4fb3.png)
4) Alumni Extra-curriculars
![image](https://user-images.githubusercontent.com/76472249/226409061-f02b4e2b-31ac-42f2-95ec-d869c76df777.png)
5) Alumni Projects
![image](https://user-images.githubusercontent.com/76472249/226409089-a5206f00-6a11-40b4-ae67-4b25193de9bd.png)
6) Alumni Work Experience
![image](https://user-images.githubusercontent.com/76472249/226409125-7cc5b3fb-58b9-4e4a-9107-3d0ae4a579f7.png)
7) Instructors
![image](https://user-images.githubusercontent.com/76472249/226409151-9573aef8-5196-47c1-8d3d-6f5148fd5710.png)
8) Faculty Advisors
![image](https://user-images.githubusercontent.com/76472249/226409180-0eea18f9-391b-4c50-9b9c-4aab22f76c31.png)

#### Insert operation is not allowed in Views because its not a table of the database. Below is the error shown after inserting in one of the Views.
![image](https://user-images.githubusercontent.com/76472249/226409501-394f0788-fe46-4bd1-8820-ce1af6c9763b.png)
![image](https://user-images.githubusercontent.com/76472249/226409545-3c4f46c9-8e50-48c8-9b19-abcb5039f26f.png)

#### Only specific actions can be performed when logged in as different users based on the privileges granted to that user.

1) Only Insert and Delete actions can be performed by an employee.
![Employee Actions](/Photos_Readme/employee_table_views.png)

1) A student is only allowed to view the tables available to it and not make any changes.
![Student Actions](/Photos_Readme/student_table_views.png)

## Work Distribution

Rahul Chembakasseril
1) Worked on developing the backend using Flask, MySQLdb from scratch. Set up the backend integration pipeline and query processing functionality through the multiple backend routes.
2) Developed basic wireframe for the frontend (proof of concept) and integrated those pages with the backend.

Kanishk Singhal
1) Worked with flask and html to add routes to various webpage.
2) Setup login and authentication feature from scratch which identifies various roles of users.
3) Setup connection to different databases in the webapp using appropriate libraries so that different roles can access database from their account(admin, students and employees).
4)  Used tailwindCSS to modify the frontend of the project.

Inderjeet Singh Bhullar
1) Worked on developing the web application using Flask and Integrating our database  in the web app using MySQL.
2) Worked on developing the final rendered HTML pages for the web application.
3) Contributed to the Front-end development of these HTML pages using CSS, Bootstrap and Tailwind in order to make it look user-friendly. 
4) Worked on creating the Navigation bar for the web application that makes it easier for the users to navigate.
5) Helped in developing the ‘student’ and ‘employee’ roles for our database and granting them the desired permissions and privileges along with contributing to the Readme file.

Kalash Kankaria
1) Contributed to the Front-end with styling and also with the addition of a navigation bar in our web app.
2) Worked on the roles/ users and their privileges, i.e., admin, student, and employee
3) Created various views and granted their privileges based on logical reasoning that should be provided to a student as a role/ user
4) Helped with the development of the backend of our Web app and integrating our MySQL database.

Bhavesh Jain
1) Worked on flask integration with MySQL.
2) Worked on designing backend routes.
3) Worked on combined work of G1&G2.

Joy Makwana
1) Worked on the Front-end using HTML, CSS and Tailwind.
2) Documented the screenshots of the execution in the ReadMe.MD file.
3) Worked on the combined work of G1&G2

Medhansh Singh
1) Developed Front-end using HTML, CSS and Tailwind CSS.
2) Setup the required connections to fully test our database and the webapp.
3) Tested the webapp to check if it supports dynamic operations.
4) Documented the testing output with snapshots in the ReadMe.MD file.

Nokzendi Aier
1) Worked on the front-end with HTML, CSS and Tailwind CSS.
2) Setup the required connections to fully test our database and the webapp.
3) Tested the webapp, views, and dynamic operations. 
4) Helped in debugging errors found during testing.
5) Documented the testing output and snapshots.
6) Contributed documentation to the ReadMe.MD file.

Harshvardhan Vala
1) Worked on the front-end with tailwindCSS and HTML.
2) Setup the required connections to fully test our database and the webapp.
3) Tested the webapp, dynamic operations, and documenting the screenshots of successfull operations readme.

Dhairya Shah
1) Worked on the frontend of the WebApp using tailwind. 
2) Setup the required connections to fully test our database and the webapp.
3) Tested the webapp, views, and dynamic operations. 
4) Testing views, clicked screenshots of successful executions, and documented them in readme.
