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


# coding: utf-8

import cgi
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write("""
                                <html>
                                  <head>
                                    <title>
                                      入力画面
                                    </title>
                                  <head>
                                  <body>
                                  <body bgcolor=#fceded>
                                  <p>
                                    文字を2つ入力してください
                                    <br>
                                    2つの文字を混ぜます
                                  </p>
                                  <p>
                                    <form action="/result" method="post">
                                      word1: <input name="word1" type="text" />
                                      <br>
                                      word2: <input name="word2" type="text" />
                                      <br>
                                      <input type="submit" value="Try!">
                                    </form>
                                  </p>
                                  </body>
                                </html>
                                """)


class ResultPage(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write("""
                                <html>
                                  <head>
                                    <title>
                                      表示画面
                                    </title>
                                  <head>
                                  <body>
                                  <body bgcolor=#fceded>
                                  <p>
                                    結果は
                                  <br>
                                  <FONT size="5" color=#ff952b>
                                """)
        word1 = self.request.get("word1")
        word2 = self.request.get("word2")

        word3 = "".join(["".join(j) for i in zip(word1,word2) for j in i])
        word3 +=word1[len(word2):]
        word3 +=word2[len(word1):]

        self.response.out.write(cgi.escape(word3))
        self.response.out.write("""</FONT>
                                  <br>
                                  です。
                                  </p>
                                  <p>
                                  <br>
                                     文字を2つ入力してください
                                    <form action="/result" method="post">
                                      word1: <input name="word1" type="text" />
                                      <br>
                                      word2: <input name="word2" type="text" />
                                      <br>
                                      <input type="submit" value="Try again!">
                                    </form>
                                  </p>
                                  </body>
                                </html>
                                """
                                )

app = webapp2.WSGIApplication([("/", MainPage),
                               ("/result", ResultPage)],
                              debug=True)