#!/usr/bin/env python

from http.server import CGIHTTPRequestHandler, HTTPServer
from argparse import *

class Handler(CGIHTTPRequestHandler):
	cgi_directories = ["/cgi-bin"]

DEFAULT_IP="127.0.0.1"
PORT = 1267
PROG_NAME = "NIASRA Status Monitoring Service - CollectD Web"
PROG_DESC = "This is a python script to interpret all RRD files that are created by collectd"
PROG_EPILOG = ""

def main():
	parser = ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_EPILOG)
	parser.add_argument('-i', '--ipToDeploy', type=str, help="The IP to which the server should be deployed to, default is localhost 127.0.0.1", default=DEFAULT_IP)
	parser.add_argument('-p', '--port', type=int, help="The PORT to which the server should be deployed to, default is 1267", default=PORT)
	args = parser.parse_args()
	httpd = HTTPServer((args.ipToDeploy, args.port), Handler)
	print("Collectd-web server running at http://{}:{}/".format(args.ipToDeploy, args.port))
	httpd.serve_forever()

if __name__ == "__main__":
	main()
