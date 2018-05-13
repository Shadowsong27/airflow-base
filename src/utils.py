def output_object(target_class):
    def to_object_f(func):
        def func_wrapper(self, *args, **kwargs):
            data = func(self, *args, **kwargs)
            response = []
            for item in data:
                response.append(target_class(*item))

            return response
        return func_wrapper
    return to_object_f
