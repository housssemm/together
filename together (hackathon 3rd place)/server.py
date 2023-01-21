import socketserver
from http.server import BaseHTTPRequestHandler,SimpleHTTPRequestHandler


def some_function():
    print ("some_function got called")

def donators():
    f = open("donors","r")
    lines = f.readlines()
    print(lines)
    f.close()
    return lines

def new_donation(donor,donations,stat="PUB"):
    f = open("donations","r")
    last_don=f.readlines()[-1].split(",")[0]
    f.close()
    g = open("donations","a")
    k = str(int(str(last_don))+1)+","
    for i in donations: k+=str(i)+"-"
    k+="{}\n".format(stat)
    g.write(k)
    #print(lines)
    g.close()
    print(k)


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("?req=accepted"):
            
            g=self.path.index("?req")
            t=self.path[:g]
            
            
            print(self.path)
            print(g)
            print(t)
            
            
            some_function()
            #s=donators()
            #print(s)
            L=[23,15,22]
            new_donation("G",L)
        elif self.path.endswith("?payment"):

            g=self.path.index("?pay")
            t=self.path[:g]
            t.split("+")
            new_donation(t[0],t[1].split("-"))



            self.send_response(302)
            self.send_header('Location','http://localhost:5000/payments/payment.html')
            self.end_headers()





        else:
        # self.path = 'index.html'
            self.send_response(302)
            self.send_header('Location','http://localhost:5000')
            self.end_headers()
        #self.send_response(200)



httpd = socketserver.TCPServer(("localhost", 8082), MyHandler)
httpd.serve_forever()