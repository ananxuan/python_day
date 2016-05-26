#!/usr/bin/env python3
__author__ = 'DSOWASP'
import  configparser
cp = configparser.ConfigParser()

cp.add_section("mysqld")
cp.set("mysqld","user",value="mysql")
cp.set("mysqld","group",value="mysql")
cp["DEFAULT"]["user"] = "nobody"

cp["client"] = {"log":"/var/log/mysqld.log"}
# cp.setdefault("host",default="127.0.0.1")
with open("cp.cnf",'w') as f:
    cp.write(f)