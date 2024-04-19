from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(300), nullable=False)
    text = db.Column(db.text, nullable=False)

def __repr__(self):
            return f'<Contact {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def load_index():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/contact', methods=['POST', 'GET'])
def load_contact():
    button_python = request.form.get('button_python_2')
    return render_template('load_contact', button_python_2=button_python)

@app.route('/contact.html')
def create():
    return render_template('/contact.html')
    
@app.route('/index.html')
def create_index():
    return render_template('/index.html')

@app.route('/thank_you.html')
def create_thanks():
    return render_template('/thank_you.html')

@app.route('/')
def index():
    Contacts = Contact.query.order_by(Contact.id).all()
    return render_template('index.html', Contacts=Contacts)

@app.route('/contact/<int:id>')
def contact(id):
    def contact_save():
        @app.route('/index', methods=['GET','POST'])
        def contact_create():
            if request.method == 'POST':
                title =  request.form['title']
                subtitle =  request.form['subtitle']
                email =  request.form['email']

                contact = Contact(title=title, subtitle=subtitle, email=email)

                db.session.add(contact)
                db.session.commit()
                return redirect('/')
            else:
                return render_template('index.html')

    return render_template('contact.html', Contact=Contact)

if __name__ == "__main__":
    app.run(debug=True)