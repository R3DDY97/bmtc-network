#!/usr/bin/env python3

from wtforms import (Form, StringField, SubmitField)


class SearchForm(Form):
    origin = StringField('origin')
    destination = StringField('destination')
    submit = SubmitField('submit')


class BstopForm(Form):
    bstop = StringField('bstop')
    submit = SubmitField('submit')


class RouteForm(Form):
    route = StringField('route')
    submit = SubmitField('submit')


class KstopForm(Form):
    kia_stop = StringField('kia_stop')
    submit = SubmitField('submit')


class KrouteForm(Form):
    kia_route = StringField('kia_route')
    submit = SubmitField('submit')
