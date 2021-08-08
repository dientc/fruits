class XAUDReader:
    def __init__(self) -> None:
        pass

    def read(self, filename: str) -> list:
        fruits = []
        file = open(filename, 'r')
        count = 0
        
        while True:
            count += 1
        
            # Get next line from file
            line = file.readline()
        
            # if line is empty
            # end of file is reached
            if not line:
                break

            element = line.rstrip().split("\t")
            fruits.append(element)
            # print("Line{}: {}".format(count, line.strip()))
        
        file.close()

        return fruits