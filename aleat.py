import webapp

class urlaleat(webapp.webApp):
    def process(self, parsedREquest):
        import random
        numero = random.randint(1,100000)
        return ("200 OK", "<html><body><a href= '"+ str(numero)+"'>Dame más</a></body></html>")

if __name__ == "__main__":
    testWebApp = urlaleat("localhost", 1234)
