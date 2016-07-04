#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import os
import webapp2
import jinja2
import logging
import json
import urllib
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
    	fp = urllib.urlopen("http://fantasy-transit.appspot.com/net?format=json")
    	stations = json.load(fp)
        values = {#ここでリストを辞書にして渡したい…どう渡せばよいのか…
            'station': stations
        }
        self.render('main.html', values)

    def post(self):
        from_station = self.request.get('station1')
        to_station = self.request.get('station2')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
