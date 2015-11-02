#!/usr/bin/env python

import argparse
m_user = 'MONGOUSER'
m_pass = 'MONGOPASS'
m_role = 'MONGOROLE'
m_db = 'MONGODB'
parser = argparse.ArgumentParser(description='Creating mongodb commands')

parser.add_argument("-a", "--action", action="store", dest="action", help="{create, tobecontinued}")
parser.add_argument("-u", "--user", action="store", dest="username", help="user")
parser.add_argument("-p", "--pass", action="store", dest="password", help="pass")
parser.add_argument("-r", "--role",action="store", dest="role", help="{read, readWrite, root}")
parser.add_argument("-d", "--db", action="store", dest="database", help="db name")

def adduser():
	print "db.createUser({user: \""+args.username+"\", pwd: \""+args.password+"\", roles: [ { role: \""+args.role+"\", db: \""+args.database+"\"} ] } )"


args = parser.parse_args()

if args.action == 'create':
	adduser()
