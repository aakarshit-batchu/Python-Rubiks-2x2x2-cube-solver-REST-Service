#!/usr/local/bin/python2.7
#/******** AUTHOR: NAGA SAI AAKARSHIT BATCHU ********/
from __future__ import print_function
import falcon
import socket
from wsgiref import simple_server
import argparse
import json
import logging
import os
import atexit

parser = argparse.ArgumentParser(description='Manage server with required input parameters')
parser.add_argument('-p','--port',dest='port',help='Port on which Server Should Start Running',required=True)
parser.add_argument('-l','--log',dest='log_dir',help='Python REST Service Log Directory',required=True)
args = parser.parse_args()
port = int(args.port)
log_dir = args.log_dir

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',datefmt="%Y-%m-%d %H:%M:%S",filename=log_dir + "/restservice-rubiks2x2x2.log")

logger = logging.getLogger(__name__)


class TwobyTwobyTwo(object):
        def on_post(self , req , resp):
		try:
	                json_body = json.loads(req.stream.read())
	                scrambled_pattern = str(json_body["pattern"])
	                logger.info("Received Pattern : " + scrambled_pattern)
			solution, solve_error = solve(scrambled_pattern)
			if solve_error == "nil":
				logger.info("Success")
				response_message = {"Solution":solution,"Result":"success"}
				response_json = json.dumps(response_message)
				resp.body = response_json
			else:
				logger.info("Failed")
				response_message = {"Solution":"","Result":"failed"}
				response_json = json.dumps(response_message)
				resp.body  = response_json
		except Exception as err:
			logger.info("Failed")
			logger.exception(err)
			response_message = {"Solution":"","Result":"failed"}
			response_json = json.dumps(response_message)
			resp.body = response_json


def solve(a):
	try:
		o = ''.join
	        d = [{o((' ', x)[x in a[12] + a[19] + a[22]] for x in a): []}, {' ' * 4 + (a[12] * 2 + ' ' * 4 + a[19] * 2) * 2 + a[22] * 4: []}]
	        for h in [0, 1] * 6:
	                for (s, x) in d[h].items():
	                        for y in range(12):
	                                d[h][s] = x + [y - [1, -1, 1, 3][h * y % 4]]
	                                if s in d[1 - h]:
                                                out  = o('RUF'[x / 4] + " 2'"[x % 4] for x in d[0][s] + d[1][s][::-1])
                                                logger.info("Solution: " + out)
                                                return out,"nil"
	                                s = o(s[ord(c) - 97] for c in 'acahabcdnpbfegefhugiovjgqkciljdeklflmmmnnvoopxphrqdjrrbsstttuuqsviwwwkxx'[(y / 4)::3])
	except Exception as err:
		logger.info("Failed")
		logger.exception(err)
		return "nil",err


app = falcon.API()

two = TwobyTwobyTwo()
app.add_route('/two', two)

if __name__ == '__main__':
        logger.info("Service Running on port: " + str(port))
        httpd = simple_server.make_server(socket.gethostbyname(socket.gethostname()), port, app)
        httpd.serve_forever()

#/******** AUTHOR: NAGA SAI AAKARSHIT BATCHU ********/
