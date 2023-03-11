from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import MySQLdb.cursors

app = Flask(__name__)

db = yaml.load(open('credentials.yaml'), Loader=yaml.FullLoader)
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
    table_names=[]

    for i in range(len(tables)):
        row =[]
        row.append(i+1)
        row.append(tables[i][0])
        table_names.append(row)
    
    return render_template('display_tables.html',table_data=table_names)



@app.route('/tables', methods =['POST'])
def tables_post():
    x = request.form

    button_pressed=None
    table_name = x['tableName']
    
    if(x.get('entries')==None):
        button_pressed='schema'
    else:
        button_pressed='entries'
       
    table_name_string = str(table_name)
    table_name_string = table_name_string.encode('utf-8').decode('utf-8')
    table_name_string = str(table_name_string)



    
    if(button_pressed=='entries'):

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM {table_name_string}")
        mysql.connection.commit()
        table_data = cur.fetchall()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s and TABLE_NAME=%s", ("alumni", table_name_string,))
        table_column_names_tuples = cursor.fetchall()
        TABLE_COLUMN_NAMES =[]

        for dict in table_column_names_tuples:
            x = dict['COLUMN_NAME']
            TABLE_COLUMN_NAMES.append(x)
        
        cur.close()

        return render_template('display_entries.html', userDetails=table_data, table_name=table_name_string, table_col_names=TABLE_COLUMN_NAMES, EntriesOrSchema="Entries",
                               display_edit_buttons="YES",display_edit_fields="NO")
        
    else:

        cur = mysql.connection.cursor()
        cur.execute(f"SHOW COLUMNS FROM {table_name_string}")
        mysql.connection.commit()
        table_data = cur.fetchall()
        TABLE_COLUMN_NAMES = ["Field","Type","Null","Key","Default","Extra"]
        cur.close()

        return render_template('display_entries.html', userDetails=table_data, table_col_names=TABLE_COLUMN_NAMES, table_name=table_name_string, EntriesOrSchema="Schema",
                               display_edit_buttons="NO",display_edit_fields="NO")




@app.route('/tables/edit', methods =['POST'])

def tables_edit():
    x = request.form
    pressed=None
    table_name=None


    ##which button was pressed    
    if(x.get('insert')==None):
        if(x.get('update')==None):
            if(x.get('delete')==None):
                pressed='rename'
            else:
                pressed='delete'
        else:
            pressed='update'
    else:
        pressed='insert'
    

    #finding column names
    table_name = x[pressed]
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s and TABLE_NAME=%s", ("alumni", table_name,))
    table_column_names_tuples = cursor.fetchall()
    TABLE_COLUMN_NAMES =[]

    for dict in table_column_names_tuples:
        y = dict['COLUMN_NAME']
        TABLE_COLUMN_NAMES.append(y)
    

    #finding table
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    mysql.connection.commit()
    table_data = cur.fetchall()    

    
    if(pressed=='insert'):
        return render_template('display_entries.html', userDetails=table_data, table_col_names=TABLE_COLUMN_NAMES, table_name=table_name, EntriesOrSchema="Insert",
                               display_edit_buttons="NO",display_edit_fields="YES", op='insert')
    elif(pressed=='update'):
        return render_template('display_entries.html', userDetails=table_data, table_col_names=TABLE_COLUMN_NAMES, table_name=table_name, EntriesOrSchema="Update",
                               display_edit_buttons="NO",display_edit_fields="YES", op='update')
    else:
        return








@app.route('/tables/edit/insert', methods =['POST'])

def edit_insert():
    x = request.form
    print(x)
    table_name = x['table_name']


    ##Table Before Insertion
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    mysql.connection.commit()
    table_data_before = cur.fetchall()



    #getting column names
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s and TABLE_NAME=%s", ("alumni", table_name,))
    table_column_names_tuples = cursor.fetchall()
    TABLE_COLUMN_NAMES =[]

    for dict in table_column_names_tuples:
        y = dict['COLUMN_NAME']
        TABLE_COLUMN_NAMES.append(y)

    #filling new values
    NEW_VALUES =[]
    for col in TABLE_COLUMN_NAMES:
        NEW_VALUES.append(x[col])
    

    #making the query
    query = "INSERT INTO "+ table_name+"(" + ", ".join(TABLE_COLUMN_NAMES) + ") VALUES (" + ", ".join(["%s" for _ in range(len(TABLE_COLUMN_NAMES))]) + ")"
    
    #executing query
    cur = mysql.connection.cursor()
    cur.execute(query,NEW_VALUES)
    mysql.connection.commit()


    #table after query execution
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    mysql.connection.commit()
    table_data_after = cur.fetchall()

    
    return render_template('tables_before_after.html', table_before=table_data_before, table_after=table_data_after,table_name=table_name,
                           table_col_names=TABLE_COLUMN_NAMES)




@app.route('/tables/edit/update', methods =['POST'])

def edit_update():
    x = request.form
    table_name = x['table_name']
    condition = x['condition']


    ##Table Before Insertion
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    mysql.connection.commit()
    table_data_before = cur.fetchall()



    #getting column names
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s and TABLE_NAME=%s", ("alumni", table_name,))
    table_column_names_tuples = cursor.fetchall()
    TABLE_COLUMN_NAMES =[]

    for dict in table_column_names_tuples:
        y = dict['COLUMN_NAME']
        TABLE_COLUMN_NAMES.append(y)


    #filling new values

    NEW_VALUES =[]
    for i in range(len(TABLE_COLUMN_NAMES)):
        if(x[TABLE_COLUMN_NAMES[i]]==""):
            TABLE_COLUMN_NAMES[i]= "remove"
        else:
            NEW_VALUES.append(x[TABLE_COLUMN_NAMES[i]])
    

    #changing column names depending on participation of fields
    NEW_COLUMN_NAMES =[]
    for name in TABLE_COLUMN_NAMES:
        if(name!="remove"):
            NEW_COLUMN_NAMES.append(name)

    #statement clauses
    strings=[]
    for i in range(len(NEW_COLUMN_NAMES)):
        y = NEW_COLUMN_NAMES[i]+"="+NEW_VALUES[i]
        strings.append(y)
    
    
    #making query
    query = "UPDATE "+table_name+" SET "  + ", ".join(strings) + " WHERE " + condition
    
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()


    #table after query execution
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    mysql.connection.commit()
    table_data_after = cur.fetchall()

    
    return render_template('tables_before_after.html', table_before=table_data_before, table_after=table_data_after,table_name=table_name,
                           table_col_names=TABLE_COLUMN_NAMES)
    




if __name__ == '__main__':
    app.run(debug=True, port=4999)