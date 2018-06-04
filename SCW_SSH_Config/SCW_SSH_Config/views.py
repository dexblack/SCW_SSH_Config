"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash
from SCW_SSH_Config import app
from SCW_SSH_Config.forms.sshcfg import SshCfgForm

app.config['SECRET_KEY'] = 'C&bE1ui%zplNbHmR0&P5*0tDf!i9sP'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/config', methods=['GET', 'POST'])
def config():
    """Renders the configuration page."""
    form = SshCfgForm(request.form)
    if request.method == 'POST':
        port = form['port']
        ssh_root = form['ssh_root']
        ssh_private_key = form['ssh_private_key']
        form.render()
        flash('SshCfgForm POST')

    return render_template(
        'config.html',
        title="SSH Configuration",
        year=datetime.now().year,
        message='Your SSH configuration page.',
        form=form
    )
