from flask import Flask, render_template, request, session
from server import ordering_system
from server import staff

app = Flask(__name__)
# def get_session_order():
#     if 'order' not in session:
#         session['order'] = 

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route("/staff", methods=["GET", "POST"])
def staff1():
    return render_template('staff.html')



'''
    Add a main to the order...
'''
@app.route('/menu', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        '''
        At this point, since the sides page is different, there will be errors every time a side is ordered
        So only ordering the main is satisfied.
        '''
        # Check for any errors...
        # If errors exist, print them out.
        errors = ordering_system.parse(request.form)
        if type (errors) != str:
            return render_template('menu.html', form = request.form, errors = errors)
        else:
            return render_template('order_confirmed.html', confirm = errors)
        
        return render_template('menu.html', form = request.form)
    return render_template('menu.html')

@app.route('/menu/sides', methods=['GET', 'POST'])
def sides():
    if request.method == 'POST':

        return render_template('sides.html', form = request.form)
    return render_template('sides.html')

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    return render_template('summary.html')

@app.route('/checkstate', methods=['GET', 'POST'])
def checkstate():
    if request.method == 'POST':
        orderid = int(request.form["orderid"])
        orderstate = ordering_system.checkStatus(orderid)
        return render_template('checkstate.html', orderid = orderid, orderstate = orderstate)
    return render_template('checkstate.html')
