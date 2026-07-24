class Passenger:
    def __init__(self):
        self.Passenger_id=0
        self.Passenger_name=""
        self.Age=0
        self.Gender=""
        self.Mobile_number=0
    def accept_passenger_details(self):
        self.Passenger_id=int(input("Enter the passenger id:"))
        self.Passenger_name=input("Enter your name:")
        self.Age=int(input("Enter your age:"))
        self.Gender=input("Enter your gender:")
        self.Mobile_number=int(input("Enter your mobile number:"))
    def display_passenger_details(self):
        print("------PASSENGER DETAILS------")
        print(f"Passenger_id:{self.Passenger_id}")
        print(f"Passenger_name:{self.Passenger_name}")
        print(f"Age:{self.Age}")
        print(f"Gender:{self.Gender}")
        print(f"mobile number:{self.Mobile_number}")
class Train:
    trainid=[]
    def __init__(self,train_number,train_name,source_station,destination_station,total_seats,available_seats,fare_perticket):
        self.trainno=train_number
        self.trainname=train_name
        self.sourcestation=source_station
        self.destinationstation=destination_station
        self.totalseats=total_seats
        self.availableseats=available_seats
        self.fareperticket=fare_perticket
        Train.trainid.append(self.trainno)
    def display_train_details(self):
        print("------available trains----------")
        print(f"train_no:{self.trainno},train_name:{self.trainname}")
        print(f"source_station:{self.sourcestation},destination_station:{self.destinationstation}")
        print(f"total_no_of_seats:{self.totalseats}")
        print (f"available_seats:{self.availableseats}")
        print(f"fare_per_ticket:{self.fareperticket}")
        print(self.trainid)
    def check_seat_availability(self,seats):
        return(self.availableseats>=seats)
    def update_available_seats_after_booking(self,seats):
        self.availableseats-=seats
    def update_available_seats_after_cancellation(self,seats):
        self.availableseats+=seats
class Ticket():
    def __init__(self,passenger,train,seats):
        self.Passenger=passenger
        self.train=train
        self.noofbookedseats=seats
        self.totalfare=seats*train.fareperticket
        self.status="booked"
        self.ticket_no=""
    def book_ticket(self):
        self.ticket_no=self.Passenger.Passenger_name +str(self.Passenger.Passenger_id)
    def cancel_ticket(self):
        self.status="cancelled"
        self.train.update_available_seats_after_cancellation(self.noofbookedseats)
        print("CANCELLATION CONFIRMATION")
    def display_ticket_information(self):
        print(f"ticket number:{self.ticket_no}")
        print(f"passenger name:{self.Passenger.Passenger_name}")
        print(f"age:{self.Passenger.Age}")
        print(f"gender:{self.Passenger.Gender}")
        print(f"train number:{self.train.trainno}")
        print(f"tain name:{self.train.trainname}")
        print(f"seat booked:{self.noofbookedseats}")
        print(f"total fare:{self.totalfare}")
        print(f"status:{self.status}")
train1=Train(16545,"kerala express","thiruvananthapuram","kozhikode",1500,500,1600)
train2=Train(14576,"vande bharat","kaniyakumari","mumbai",1500,750,3600)
train3=Train(14754,"chennai express","salem","chennai",750,500,2550)
train4=Train(14775,"ernad express","manglore","thiruvananathapuram",1500,750,2900)
train5=Train(14572,"indore express","delhi","jammu&kashmir",1500,500,3000)
trains=[train1,train2,train3,train4,train5]
ticket1=None
while True:
    print("-----------RAILWAY RESERVATION SYSTEM------------")
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.check seat availability")
    print("4.display ticket details")
    print("5.exit")
    choice=input("enter your choice:")
    if choice=="1":
        P=Passenger()
        P.accept_passenger_details()
        for t in trains:
            t.display_train_details()
        number=int(input("enter the train number for reservation:"))
        select_train=None
        for t in trains:
            if t.trainno ==number  :
                select_train=t
                break
        if select_train:
                seats=int(input("enter the number of seats:"))
                if select_train.check_seat_availability(seats):
                    select_train.update_available_seats_after_booking(seats)
                    ticket1=Ticket(P,select_train,seats)
                    ticket1.book_ticket()
                    print("booking confirmation")
                    ticket1.display_ticket_information()
                else:
                    print("seats not available") 
        else:
            print("invalid number")          
    elif choice=="2":
        if ticket1:
            ticket1.cancel_ticket()
        else:
            print("no ticket found")
    elif choice=="3":
        for t in trains:
            t.display_train_details()
    elif choice=="4": 
        if ticket1:
            ticket1.display_ticket_information()
        else:
            print("no ticket booked")
    elif choice=="5":
        print("thank you")
    else:
        print("try again")
    





    
        
        
        
        
        
        
        
        