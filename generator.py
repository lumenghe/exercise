from dataclasses import dataclass


@dataclass
class FileReader:
    _file: str

    def head(self):
        next = None
        with open(self._file) as file:
            for line in reversed(file.readlines()):
                for letter in reversed(line.strip().split(" ")):
                    new = NewObject(letter)
                    new.next = next
                    next = new
        return next


@dataclass
class NewObject:
    value: str
    _next: None

    def __init__(self, value: str):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self._next


if __name__ == "__main__":
    file_reader = FileReader("reading.txt")
    current = file_reader.head()
    while current.next:
        print(current.value)
        current = current.next
