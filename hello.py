#!/usr/bin/env python
import sys

def app(env, start_response):
    # /?a=1&a=2&b=3
    result=""
    for line in env["QUERY_STRING"].split("&"):
        result = result+line+"\n"
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [result]
