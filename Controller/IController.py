def overrides(interface):
    """
    Function override annotation.
    Corollary to @abc.abstractmethod where the override is not of an
    abstractmethod.
    Reference: https://stackoverflow.com/a/8313042

    :param interface: Parent class of which the method is overwritten.
    :return: Return the method only if it is truly override, raise
     AssertionError if not.
    """
    def overrider(method):
        assert method.__name__ in dir(interface), \
            f"The method '{method.__name__}' does not overwrite any method of class '{interface.__name__}'."
        return method
    return overrider

class IController:
    def nextScene(self):
        raise NotImplemented("This class not should be instantiate.")