from websocket import *
class WebSocket2(WebSocket): receive = WebSocket.recv
