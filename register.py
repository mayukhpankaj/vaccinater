from flask import Flask, render_template, redirect , url_for 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email





app = Flask(__name__)

app.config['SECRET_KEY'] = 'xyz'  #CSRF token



class searchform(FlaskForm):

    pincode = StringField('search',validators=[DataRequired()])

    phone = IntegerField('phone',validators=[DataRequired(),Length(max=10)])

    email = StringField('email',validators=[DataRequired(),Email()])

    submit = SubmitField('Register')



@app.route('/', methods=['POST','GET'])

def register():

    form = searchform()


    if form.validate_on_submit():

        print('submit clicked')

        global usr_input

        user_input = form.text.data
        usr_input = user_input
        print(user_input)


        #return redirect(url_for('result'))   #redirecting to results page  
 
    return render_template('index.html',form=form)



if __name__=='__main__':
     app.run(debug=True)    
