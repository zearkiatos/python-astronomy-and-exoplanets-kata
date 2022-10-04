import pandas

def read_data(path:str, attributes: list)-> list:
    data_dictionary = []
    file = open(path)
    file.readline().split(",")
    line = file.readline()

    while (len(line) > 0):
        data = line.split(",")
        row = {}
        for attribute in attributes:
            row[attribute["name"]] = data[attribute["position"]]
        data_dictionary.append(row)
        line = file.readline()
    file.close()

    return data_dictionary
