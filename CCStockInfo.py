#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CCStockInfo.py
#  
#  Copyright 2017 youhua deng (deng you hua | CC) <ccworld1000@gmail.com>
#  https://github.com/ccworld1000/CCStockInfo
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
import requests

def getContent (url) :
	try :
		r = requests.get (url)
		r.encoding = r.apparent_encoding
		content = r.text
		
		return content
	except Exception, e:
		print e.message
		return ""

def parseStockCode (url) :
	try :
		html = getContent (url)
		
		aList = re.findall(r'<li><a target="_blank" .*?</a></li>', html)
		
		#print aList
		print "aList len = " + str(len (aList))
		
		count = 0
		useCount = 0
		match = re.compile(r'(s[zh]\d+).html">(.*)\((\d+)\)')
		
		for a in aList :
			#print str(count)

			if a.find ('(') >= 0 :
				#print str(useCount)
				#print a

				res = match.findall(a)
				#print res
				
				t = res[0]
				print str(useCount) + " " + "%s\t\t\t%s\t\t\t%s" % t

				useCount = useCount + 1
				
			count = count + 1
		
	except Exception, e: 
		print e.message


