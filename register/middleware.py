class NextRedirectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'next' in request.GET:
            request.session['next'] = request.GET['next']
        response = self.get_response(request)
        return response
