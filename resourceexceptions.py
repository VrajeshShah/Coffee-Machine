class RecipeNotFound(Exception):
    pass

class ResourceError(Exception):
    def __init__(self, msg,resource):
        self.message=msg
        self.resourceName=resource

    def __str__(self):
        if self.message:
            return '{0}'.format(self.message)
        else:
            return 'ResourceError has been raised'

class NotEnoughSupplyError(Exception):
    def __init__(self, msg,resource):
        self.message=msg
        self.resourceName=resource

    def __str__(self):
        if self.message:
            return '{0}'.format(self.message)
        else:
            return 'NotEnoughSupplyError has been raised'