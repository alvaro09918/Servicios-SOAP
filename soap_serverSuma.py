from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
def SumaDosNumeros(numero1,numero2):
    return numero1+numero2
dispatcher=SoapDispatcher(
    "servicio-soap",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"suma":int},
    args={"numero1":int,"numero2":int},
)
server=HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP DOS iniciado en http://localhost:8000/")
server.serve_forever()