#!/usr/bin/python3

import random
import webapp


class urlAleatorias(webapp.webApp):

    def process(self, parsedRequest):
        link = str(random.randrange(1000000000))
        return ("200 OK", "<html><body><h1>Hola</h1>" +
                "<a href='" + link + "'>Dame direccion aleatoria</a>" +
                "</body></html>" + "\r\n")


if __name__ == "__main__":
    url = urlAleatorias("localhost", 8000)
