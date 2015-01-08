def delete_logging_method_decorator(func):
    def wrapper(self, *argv, **kwargv):
        self.debug('Object %s %s was deleted.' % (
        	self.get_object().__class__.__name__, self.get_object().pk))
        self.info('Object %s %s was deleted.' % (
            self.get_object().__class__.__name__, self.get_object().pk))
        return func(self, *argv, **kwargv)
    return wrapper


def update_logging_method_decorator(func):
    def wrapper(self, *argv, **kwargv):
        self.debug('Object %s %s was updated.' % (
        	self.get_object().__class__.__name__, self.get_object().pk))
        self.info('Object %s %s was updated.' % (
            self.get_object().__class__.__name__, self.get_object().pk))
        return func(self, *argv, **kwargv)
    return wrapper


def create_logging_method_decorator(func):
    def wrapper(self, *argv, **kwargv):
        self.debug('Object %s %s was created.' % (
        	self.object.__class__.__name__, self.object.id))
        self.info('Object %s %s was created.' % (
            self.object.__class__.__name__, self.object.id))
        return func(self, *argv, **kwargv)
    return wrapper