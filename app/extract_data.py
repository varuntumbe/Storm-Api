import os


#defining a class to extract data

class Extract_data(object):

    def __init__(self):
        self.storm_data=list()
        self.filename= os.path.abspath('stormdata/storms.csv')
        self.store_data()
        self.trim_data()

    def store_data(self):
        with open(self.filename) as fobj:
            temp_list=fobj.readlines()
        self.storm_data=[data.split(',')[1:] for data in temp_list ]

    def trim_data(self):
        del self.storm_data[0]
        for data in self.storm_data:
            del data[12]
            del data[11]
            del data[9]
            del data[8]
            del data[4]
            del data[3]
            del data[2]
        for i in range(len(self.storm_data)):
            temp_list=list()
            for j in range(len(self.storm_data[i])):
                field=self.storm_data[i][j].strip('"')
                if j in [1,5]:
                    field=int(field)
                elif j in [2,3]:
                    field=float(field)
                temp_list.append(field)
            self.storm_data[i]=temp_list

    def view_data(self):
        for i in range(10):
            print(self.storm_data[i])

    def get_data(self):
        return self.storm_data

if __name__ == "__main__":
    dataobj=Extract_data()
    dataobj.view_data()