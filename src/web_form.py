#!/usr/bin/env python3

from wtforms import (Form, StringField, SubmitField, validators)


class SearchForm(Form):
    origin = StringField('origin')
    destination = StringField('destination')
    submit = SubmitField('submit')
