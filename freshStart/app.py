from flask import Flask,render_template, flash, request
import pandas as pd 
from flask_wtf import FlaskForm, Form
from wtforms import  StringField, IntegerField, FormField, SubmitField, validators, FieldList
from wtforms.form import BaseForm
import os

DEBUG = True
app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config.from_object(Config)    
df = pd.read_csv('data.csv',index_col=0)
def form_from_fields(fields):
    def create_form(prefix='', **kwargs):
        form = BaseForm(fields, prefix=prefix)
        form.process(**kwargs)
        return form
    return create_form

class MyForm(FlaskForm):
	fielders = FormField(
		form_from_fields(
			[(str(name),StringField(str(name))) for name in df.columns]
			)
		)
	submit = SubmitField()


@app.route('/', methods=['GET','POST'])
def index():
	user= {'username':'Tumas'}
	form = MyForm()
	#print(form.fielders)
	if request.method == 'POST':
		result = request.form
		newrow = {}
		print('\n',len(df.columns),'\n')
		for key, value in result.items():
			print(key, '\t', value)
			if key != "submit":
				key = key[9:]#purge fielders
				print(key)
				newrow[key] = value
		print('\n','ours ',str(len(newrow)),'\n')

		print(pd.Series(newrow))

		df.loc[len(df)] = pd.Series(newrow)
		print(df)
		df.to_csv('data.csv')
	return render_template('base.html',title='Home',	
	 user=user, data=(df.columns), form=form)

if __name__== '__main__':
	app.run()	