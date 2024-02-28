from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
def CadenaPalindromo(cadena):
    aux=""
    for i in reversed (cadena):
        aux=aux+i
    if(cadena==aux):
        return True
    else:
        return False
dispatcher=SoapDispatcher(
    "servicio-soap",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"palindromo":bool},
    args={"cadena":str,},
)
server=HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP DOS iniciado en http://localhost:8000/")
server.serve_forever()