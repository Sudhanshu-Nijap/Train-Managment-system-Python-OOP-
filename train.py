import requests
class IRCTC:
    def __init__(self):
        self.menu()
    def menu(self):
        print("""How would you like to proceed?
1. Enter 1 to check live train status.
2. Enter 2 to check train information
3. Enter 3 to check train schedule
4. Enter any key to exit""")
        user_input = input("-->")

        if user_input=='1':
            self.train_info()
        elif user_input=='2':
            pass #fare
        elif user_input == '3':
            self.train_schedule()
        else:
            exit()
    def train_info(self):
        train_no = int(input("Enter the train number: "))
        self.fetch_data_info(train_no)
        print("")
        self.menu()
    def fetch_data_info(self,train_no):
        data1=requests.get("https://indianrailapi.com/api/v2/TrainInformation/apikey"
                           "/bb89dd4cde5bd8e1ac6e12f000b4fea1/TrainNumber/{}".format(train_no))
        data1=data1.json()

        print("Train Name:",data1['TrainName'])
        print("Source Code:",data1['Source']['Code'])
        print("Source Arrival:",data1['Source']['Arrival'])

        print("Destination Code:", data1['Destination']['Code'])
        print("Destination Arrival:", data1['Destination']['Arrival'])
    def train_schedule(self):
        train_no=int(input("Enter the train number: "))
        self.fetch_data_schedule(train_no)
        print("")
        self.menu()
    def fetch_data_schedule(self,train_no):
        data2=requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/"
                          "bb89dd4cde5bd8e1ac6e12f000b4fea1/TrainNumber/{}".format(train_no))
        data2=data2.json()
        for i in data2['Route']:
            print(i['StationName'],"|",i['ArrivalTime'],'|',i['DepartureTime'],i['Distance'],"kms")

train=IRCTC()




