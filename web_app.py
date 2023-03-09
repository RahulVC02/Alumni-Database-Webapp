from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('credentials.yaml'), Loader=yaml.FullLoader)
# print(db)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']



mysql = MySQL(app)




@app.route('/', methods=['POST'])
def home_post():
    # Fetch form data
    # userDetails = request.form
    # name = userDetails['name']
    # email = userDetails['email']
    # cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
    # mysql.connection.commit()
    # cur.close()


    return redirect('/tables')
    

@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')


@app.route('/tables', methods =['GET'])
def tables():
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()
    cursor.close()
    # mysql.connection.close()

    table_names=[]

    for i in range(len(tables)):
        row =[]
        row.append(i+1)
        row.append(tables[i][0])
        table_names.append(row)

    # print(table_names)

    
    return render_template('display_tables.html',table_data=table_names)



@app.route('/tables', methods =['POST'])
def tables_post():
    x = request.form
    print(x)








@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True, port=4999)