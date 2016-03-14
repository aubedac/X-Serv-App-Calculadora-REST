#!/usr/bin/python

import webapp
import sys

class rest_calc(webapp.webApp):

    def parse(self, request):
        method = request.split(' ', 2)[0]
        opertype = request.split(' ', 2)[1]
        body = request.split('\r\n\r\n')[1];

        return (method, opertype, body)

    def process(self, parsedRequest):
        method, opertype, body = parsedRequest

        if method == "PUT":
            httpCode = "200 OK"
            operand1 = body.split(' ', 2)[0]
            sign = body.split(' ', 2)[1]
            operand2 = body.split(' ', 2)[2]

            if sign == "+":
                self.result = str(int(operand1) + int(operand2))
                htmlBody = "<html><body><h1> " + operand1 + " + " + operand2 + " = " \
                            + self.result + " </h1></body></html>"
            elif sign == "-":
                self.result = str(int(operand1) - int(operand2))
                htmlBody = "<html><body><h1> " + operand1 + " - " + operand2 + " = " \
                            + self.result + " </h1></body></html>"
            elif sign == "*":
                self.result = str(int(operand1) * int(operand2))
                htmlBody = "<html><body><h1> " + operand1 + " * " + operand2 + " = " \
                            + self.result + " </h1></body></html>"
            elif sign == "/":
                self.result = str(int(operand1) / int(operand2))
                htmlBody = "<html><body><h1> " + operand1 + " / " + operand2 + " = " \
                            + self.result + " </h1></body></html>"

        elif method == "GET":
                httpCode = "200 OK"
                htmlBody = "<html><body><h1> " + 'Previous solution: '+ self.result + " </h1></html></body>"

        else:
            httpCode = "405 Method not allowed"
            htmlBody = "<html><body><h1> " 'Only PUT or GET allowed.' " </h1></html></body>"

        return (httpCode, htmlBody)

if __name__ == '__main__':
    try:
        calc = rest_calc("localhost", 1234)
    except KeyboardInterrupt:
        print "Closing..."
        sys.exit()
