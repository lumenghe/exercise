from dataclasses import dataclass


@dataclass
class FileReader:
    _file: str

    def generator_word(self):
        with open(self._file) as file:
            for line in file:
                for word in line.strip().split(" "):
                    yield word


class EnumerateHehe:
    def __init__(self, generator):
        self.number = -1
        self.generator = generator

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return (self.number, self.generator.__next__())


class GeneratorCycle:
    def __init__(self, mylist):
        self.mylist = mylist
        self.number = -1

    def create_generator(self):
        self.number += 1
        yield self.mylist[self.number]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.create_generator().__next__()
        except:
            self.number = 0
            return self.mylist[self.number]


class NewZipGenerator:
    def __init__(self, enumerate_1, enumerate_2):
        self.cycle_1 = GeneratorCycle(list(enumerate_1))
        self.cycle_2 = GeneratorCycle(list(enumerate_2))
        self.loop = False

    def __iter__(self):
        return self

    def __next__(self):
        ret = (self.cycle_1.__next__(), self.cycle_2.__next__())
        if ret[0][0] == 0 and ret[1][0] == 0 and self.loop:
            raise StopIteration
        else:
            self.loop = True
            return ret


if __name__ == "__main__":
    file_reader = FileReader("reading.txt")
    for index, word in enumerate(file_reader.generator_word()):
        print(index, word)

    for index, word in EnumerateHehe(file_reader.generator_word()):
        print(index, word)

    file_reader_backup = FileReader("reading.txt")
    for x in NewZipGenerator(
        EnumerateHehe(file_reader.generator_word()),
        EnumerateHehe(file_reader_backup.generator_word()),
    ):
        print(x)
