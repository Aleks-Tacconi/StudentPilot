from abc import ABCMeta, abstractmethod

class Page(metaclass=ABCMeta):
    @abstractmethod
    def render(self) -> None: ...

