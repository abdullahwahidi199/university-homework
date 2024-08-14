class Hotel():
    def __init__(self,name,rooms):
        self.name=name
        self.available_rooms=[rooms]



    def check(self,room_num):
        if room_num in self.available_rooms:
            print("this room is available")
        else:
            print("sorry this room is already taken!")

    def book(self,room_num):
        if room_num in self.available_rooms:
            self.available_rooms.remove(room_num)

            print("enjoy!!")
        else:
            print("sorry, this room is not available!")



hotel=Hotel("Wahidi luxury hotel",[101,102,108])
hotel.book(105)




