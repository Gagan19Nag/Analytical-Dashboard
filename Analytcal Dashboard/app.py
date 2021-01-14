from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import psycopg2
import ast

app = Flask(__name__)

conn = psycopg2.connect(database="postgres", user="postgres", password="nitk", host="127.0.0.1", port="5432")
cur = conn.cursor()

sales_exe = ''
pqr = ''
name = ''
designation = ''


@app.route('/', methods =["GET", "POST"])
def gfg():
    global sales_exe
    global pqr
    global name
    global designation
    r = ''
    if request.method == "POST":
       first_name = request.form.get("fname")
       last_name = request.form.get("lname")
       cur.execute("SELECT user_name, user_id, password  from protected.user_auth where user_name = '" + first_name + "'")
       rows = cur.fetchall()
       name = first_name
       print(name)
       if rows[0][2] == last_name:
           sales_exe = "('" + name + "')"
           designation = 'Sales Executive';
           cur.execute("SELECT superviser_name, subordinate_name, superviser_role_id from rbac.supervisor_subordinate_relation_ship_view where superviser_name = '" + first_name + "'")
           rows = cur.fetchall()
           print(rows)
           if len(rows) != 0:
                r = rows[0][2]
                if r == 'r5':
                    cur.execute("SELECT user_name from rbac.users")
                    rows = cur.fetchall()
                    pqr = "("
                    print(rows)
                    for i in rows:
                        abc = ''.join(i[-1])
                        pqr = pqr + "'" + abc + "',"
                    sales_exe = pqr[:-1]
                    sales_exe = sales_exe + ")"
                    print(sales_exe)
                else:
                    pqr = "("
                    for i in rows:
                        abc = ''.join(i[-2])
                        pqr = pqr + "'" +abc + "',"
                    sales_exe = pqr[:-1]
                    sales_exe = sales_exe + ")"

                cur.execute("select role from rbac.role where role_id = '" + r + "'")
                rows = cur.fetchall()
                print(rows)
                d = rows[0]
                designation = d[0]

           return redirect(url_for('SalesRepView'))
       else:
            message = 'You have entered wrong User ID or Password'
            context = {'message' : message}
            return render_template("add.html", **context)
    return render_template("add.html")


@app.route('/SalesRep',  methods =["GET", "POST"])
def SalesRepView():

    cur.execute(
    "SELECT location, total_sale_amount  from sales_anl.sales_by_location where sales_representative in" + sales_exe )
    rows = cur.fetchall()
    listToStr = ' '.join(map(str, rows))
    listToStr = listToStr.replace('(', '[')
    listToStr = listToStr.replace(')', '],')
    listToStr = listToStr.replace("'", '"')
    listToStr = listToStr[:-1]

    listToStr = "[['Location', 'Total Sale Amount']," + listToStr + "]"
    StrTolist = ast.literal_eval(listToStr)

    cur.execute(
        "SELECT month, total_sale_amount  from sales_anl.srv_total_sales_by_month where sales_representative in" + sales_exe)
    rows = cur.fetchall()
    listToStr1 = ' '.join(map(str, rows))
    listToStr1 = listToStr1.replace('(', '[')
    listToStr1 = listToStr1.replace(')', '],')
    listToStr1 = listToStr1.replace("'", '"')
    listToStr1 = listToStr1[:-1]
    listToStr1 = "[['Month', 'Total Sales' ]," + listToStr1 + "]"
    #StrTolist1 = ast.literal_eval(listToStr1)

    print(listToStr1)

    cur.execute(
        "SELECT customer, total_sale_amount  from sales_anl.srv_top_customers where sales_representative in" + sales_exe)
    rows = cur.fetchall()

    listToStr2 = ' '.join(map(str, rows))
    listToStr2 = listToStr2.replace('(', '[')
    listToStr2 = listToStr2.replace(')', '],')
    listToStr2 = listToStr2.replace("'", '"')
    listToStr2 = listToStr2[:-1]
    listToStr2 = "[" + listToStr2 + "]"
    #StrTolist2 = ast.literal_eval(listToStr2)

    cur.execute(
        "SELECT sales_representative, location, region, customer, order_date, item , quantity, price, total_sales  from sales_raw.sales_raw_table where sales_representative in" + sales_exe)
    rows = cur.fetchall()
    listToStr3 = ' '.join(map(str, rows))
    listToStr3 = listToStr3.replace('(', '[')
    listToStr3 = listToStr3.replace(')', '],')
    listToStr3 = listToStr3.replace("'", '"')
    listToStr3 = listToStr3[:-1]
    listToStr3 = "[" + listToStr3 + "]"
    #StrTolist3 = ast.literal_eval(listToStr3)

    cur.execute("SELECT subordinate_name, superviser_name  from rbac.hirerachy_view")
    rows = cur.fetchall()

    listToStr2 = ' '.join(map(str, rows))
    listToStr2 = listToStr2.replace('(', '[')
    listToStr2 = listToStr2.replace(')', '],')
    listToStr2 = listToStr2.replace("'", '"')
    listToStr2 = listToStr2[:-1]
    listToStr2 = "[" + listToStr2 + "]"

    hirerachy = listToStr2

    print(name)
    print(designation)
    print(hirerachy)
    print(StrTolist)
    print(listToStr1)
    print(listToStr2)
    #print(listToStr3)

    context = {'values' : StrTolist, 'barchartvalues' : listToStr1, 'tablevalues' : listToStr2 , 'rawtablevalue' : listToStr3,  'name' : name, 'designation' : designation, 'hirerachy' : hirerachy  }
    return render_template("SalesRepresentativeView.html", **context)

if __name__ == '__main__':
    app.run(debug = True)

