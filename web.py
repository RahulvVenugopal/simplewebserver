from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<title>Revenue of companies</title>
<body>
<center>
 <table border="4" cellspacing="10" cellpadding="6">
<caption><h2>Top five Revenue Generating Software Companies</h2></caption>
<tr>
<th>S.NO</th>
<th>Company</th>
<th>Revenue</th>
</tr>
<td>1</td>
<td>Microsoft </td>
<td> 65 Billion </td>
</tr>
<tr>
<td>2</td>
<td> Oracle </td>
<td> 29.6 Billion </td>
</tr>
</tr>
<td>3</td>
<td> IBM </td>
<td> 29.1 Billion </td>
</tr>
</tr>
<td>4</td>
<td> SAP </td>
<td> 6.4 Billion </td>
</tr>
</tr>
<td>5</td>
<td> Symantec </td>
<td> 5.6 Billion </td>
</tr>
</center>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()