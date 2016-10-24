class NextRedirectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'next' in request.GET:
            redirect = request.GET['next']
            request.session['next'] = redirect
        response = self.get_response(request)
        return response
