from flask import Flask,request,render_template,jsonify,session,url_for

app = Flask(__name__)
users = []
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user_data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "password": request.form['password'],
            "confirm_password": request.form['confirm password'],
            "email": request.form['email'],
            "phone": request.form['phone'],
        }
        if user_data['password'] != user_data['confirm_password']:
            return "Password incorrect, Error:400";
        if any(user['email']==user_data['email'] for user in users):
            return "email already exits";
        if any(user['phone']==user_data['phone'] for user in users):
            return "phone already exits";

        #save data in db
        users.append(user_data)
    return render_template('signup.html')

@app.route('/api/users',methods = ['GET'])
def get_users():
    return jsonify(users)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    #validate credential
        user = next((i for i in users if i['email']=='email' and i['password']=='password'),None)

        if user:
            session['user']=user
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credential', 400

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html',users=users)

if __name__ == '__main__':
    app.run(debug=True)
