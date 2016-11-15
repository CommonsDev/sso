from django.utils.decorators import method_decorator


def class_decorator(decorator):
    """
    Decorate the `dispatch` method of a class based view.
    source: https://gist.github.com/peterbe/2913338
    """
    def inner(cls):
        orig_dispatch = cls.dispatch

        @method_decorator(decorator)
        def new_dispatch(self, request, *args, **kwargs):
            return orig_dispatch(self, request, *args, **kwargs)
        cls.dispatch = new_dispatch
        return cls

    return inner
