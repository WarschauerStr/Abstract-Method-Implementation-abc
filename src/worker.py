from abc import ABC, abstractmethod


# Complete the class Worker

class Worker(ABC):

    def __init__(self, name: str):
        self._name = name  # privete attribute

    @abstractmethod
    def work(self):
        print(f"\n\n{self._name} starts working:")
        # abstract method, to be implemented by subclasses

    @abstractmethod
    def take_break(self, minutes):
        print(f"\n\n{self._name} takes {minutes} minutes break:")
        # abstract method, to be implemented by subclasses


# Complete this class, so that it would work properly ->
# implement the missing methods

class Programmer(Worker):
    def __init__(self, name: str, language: str):
        super().__init__(name)
        self.language = language

    def work(self):
        print(f"{self._name} is coding in {self.language}")

    def take_break(self, minutes: int):
        print(f"{self._name} takes a {minutes}-minute break.")


# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music

class Janitor(Worker):
    def __init__(self, name: str, tool: str):
        super().__init__(name)
        self.tool = tool

    def work(self):
        print(f"{self._name} is cleaning with {self.tool}")

    def take_break(self, minutes: int):
        print(
            f"{self._name} listens to music for {minutes} minutes "
            "during the break."
        )
