#!/usr/bin/env python
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

#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello world!')

import jinja2
import webapp2


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #this is where you reference your HTML file
        template = env.get_template('index.html')
        self.response.out.write(template.render())
    def post(self):
        results_template = env.get_template('results.html')
        # The variables that are sent to results.html are those
        # that contain the input values from the main.html form with
        # names like noun1, activity, etc.
        template_variables = {
            'name':self.request.get("name"),
            'year':self.request.get("year"),
            'score':self.request.get("score"),
        }
        self.response.out.write(results_template.render(template_variables))


# creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
    ('/', MainHandler)], debug=True)
