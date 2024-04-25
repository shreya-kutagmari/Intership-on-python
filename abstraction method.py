from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_content(self):pass

class Document(Printable):
        def print_content(self):
            print("print_content")

document=Document()
document.print_content()