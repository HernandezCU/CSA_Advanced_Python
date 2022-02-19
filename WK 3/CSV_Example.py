import csv


"""
Opens the CSV File and stores all the data in an array
Removes the header from the CSV File
Converts String ID to Ints
"""
def import_data():
    data = []
    with open('JBUDB.csv') as db_data:
        in_data = csv.reader(db_data, delimiter=',')
        for r in in_data:
            data.append(r)

        del data[0]

        for x in data:
            x[0]=int(x[0])

    return data


def find_by_id(data, id: int):
    for i in data:
        if i[0] == id:
            return i
        else:
            pass

    return None



def find_by_firstname(data, firstname: str):
    x = []
    for i in data:
        if i[1] == id:
            x.append(i)
        else:
            pass

    if x == []:
        return None
    else:
        return x


def find_by_lastname(data, lastname: str):
    x = []
    for i in data:
        if i[2] == id:
            x.append(i)
        else:
            pass

    if x == []:
        return None
    else:
        return x


def find_by_email(data, email: str):
    for i in data:
        if i[3] == id:
            return i
        else:
            pass

    return None


def find_by_position(data, position: str):
    x = []
    for i in data:
        if i[4] == id:
            x.append(i)
        else:
            pass

    if x == []:
        return None
    else:
        return x


def find_by_department(data, department: str):
    x = []
    for i in data:
        if i[5] == id:
            x.append(i)
        else:
            pass

    if x == []:
        return None
    else:
        return x


def create_file(data: any, filename: str):

    if ".csv" in filename.lower():
        pass

    elif "." in filename.lower():
        filename = filename.lower().replace(".", "")

    if ".csv" not in filename.lower():
        filename = filename.lower()+".csv"


    try:
        file = open(filename, "x")
        for i in data:
            file.write(str(i[0]) + "," + i[1] + "," + i[2]+ "," + i[3]+ "," + i[4]+ "," + i[5] + "\n")
    except:
        file = open(filename, "w")
        for i in data:
            file.write(str(i[0]) + "," + i[1] + "," + i[2] + "," + i[3] + "," + i[4] + "," + i[5] + "\n")


if __name__ == '__main__':
    print(import_data())
    # create_file(import_data(), "test.pdf")