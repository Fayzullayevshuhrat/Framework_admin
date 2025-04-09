from webob import Request, Response
from parse import parse


class FrameWorkApp:
    def __init__(self):  # to'g'ri constructor
        self.routes = dict()

    def __call__(self, environ, start_response):  # to'g'ri __call__ metodi
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, request):
        res = Response()

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, res)
                return res

            parsed = parse(path, request.path)
            if parsed is not None:
                handler(request, res, **parsed.named)
                return res

        res.status_code = 404
        res.text = "Sahifa topilmadi !!!"
        return res

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper
