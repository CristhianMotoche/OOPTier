class AttributeInitType(type):
    def __call__(self, *args, **kwargs):
        """ Create a new instance. """

        # First, create the object in the normal default way.
        obj = type.__call__(self, *args)

        # Additionally, set attributes on the new object.
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # Return the new object.
        return obj
