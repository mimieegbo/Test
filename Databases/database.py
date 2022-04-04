class Database:
    def __init__(self, url):
        self.url = url

    def createTable(self, name, datatype):
        url = self.url
        table_url = url + '/' + name
        file = open(table_url, 'w+')
        file.write('datatype = ' + datatype)
        file.close()

        return Table(table_url, datatype)


class Table:
    def __init__(self, table_url):
        self.url = table_url

    def __str__(self):
        i = self.url.rindex('/')
        name = self.url[i+1:]

        return 'Table Object'

    def f_three_lines(self):
        file = open(self.url, 'r')
        three_lines = []

        for i in range(3):
            three_lines.append(file.readline())

        return three_lines
