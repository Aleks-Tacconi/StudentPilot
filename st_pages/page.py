from abc import ABCMeta, abstractmethod


class Page(metaclass=ABCMeta):
    def render(self) -> None: ...
