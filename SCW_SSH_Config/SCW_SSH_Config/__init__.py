"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import SCW_SSH_Config.views
