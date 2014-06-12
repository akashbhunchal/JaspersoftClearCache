from properties import *

html_string_1 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Rebuild Cache</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">Rebuild Cache</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>%s</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=j_password_pseudo</td>
	<td>%s</td>
</tr>
<tr>
	<td>type</td>
	<td>id=j_username</td>
	<td>%s</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=submitButton</td>
	<td>60000</td>
</tr>
'''

html_string_2='''</tbody></table>
</body>
</html>'''
import csv

f = open('./urls.csv','r')
reader = csv.reader(f)
new_html = html_string_1 % (JASPERSOFT_LOGIN_URL, JASPERSOFT_PASSWORD, JASPERSOFT_USERNAME)
for row in reader:
	if len(row) <2:
		continue
	else:
		new_html += '''<tr>
							<td>open</td>
							<td>%s</td>
							<td></td>
						</tr>
						<tr>
							<td>pause</td>
							<td>%s</td>
							<td></td>
						</tr>''' % (row[0],row[1])
		
new_html += html_string_2
f = open('./build_cache.html','w')
f.write(new_html)

html_string_3 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="http://ec2-54-204-72-221.compute-1.amazonaws.com/jasperserver-pro/flow.html?_flowId=designerCacheFlow" />
<title>New Test</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">New Test</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>%s</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=j_password_pseudo</td>
	<td>%s</td>
</tr>
<tr>
	<td>type</td>
	<td>id=j_username</td>
	<td>%s</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=submitButton</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>%sflow.html?_flowId=designerCacheFlow</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>id=clearAllCache</td>
	<td></td>
</tr>
<tr>
	<td>pause</td>
	<td>10000</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>/jasperserver-pro/flow.html?_flowId=designerCacheFlow</td>
	<td></td>
</tr>
</tbody></table>
</body>
</html>'''

f = open('./clear_cache_script.html','w')
f.write(html_string_3 % (JASPERSOFT_LOGIN_URL, JASPERSOFT_ADMIN_PASSWORD, JASPERSOFT_ADMIN_USERNAME, JASPERSOFT_SERVER_CONTEXT))
f.close()
