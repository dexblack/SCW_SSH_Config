from errno import ENOENT, EACCES, EPERM
from string import Template
from os import path
from wtforms import Form, StringField, SubmitField, IntegerField
from wtforms import validators

class SshCfgForm(Form):
    """SSH Configuration Form."""

    port = IntegerField('Port', validators=[validators.required()], default="9023")
    ssh_root = StringField('SSH Directory', validators=[validators.required()])
    ssh_private_key = StringField('SSH Private Key File Name', validators=[validators.required()])
    configuration = ""

    def render(self):
        """Generate the configuration file from the template."""
        template_file_name = "ssh_config.template.txt"
        template_file = path.join(path.dirname(__file__), template_file_name)
        self.configuration = ""

        try:
            with open(template_file) as f:
                content = Template(f.read())
                self.configuration = content.substitute(
                    {
                        'port0': self.port.data,
                        'port1': str(int(self.port.data) + 1),
                        'ssh_root': self.ssh_root.data,
                        'ssh_private_key': self.ssh_private_key.data
                        }
                    )
                # print(self.configuration)

        except IOError as err:
            if err.errno == ENOENT:
                print("File not found: " + template_file)
            elif err.errno in (EACCES, EPERM):
                print("You are not allowed to read " + template_file)
            else:
                raise
