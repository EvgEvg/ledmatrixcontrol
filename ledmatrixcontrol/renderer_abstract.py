import abc

""" Just enforce certain methods """
class rendererAbstract:
    __metaclass__ = abc.ABCMeta

    """ Main required method """
    @abc.abstractmethod
    def render(self, matrix):
        raise NotImplementedError()
