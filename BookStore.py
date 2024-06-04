import numpy as np
import json
import matplotlib.pyplot as plt


print("                             BookStore   A Library Management System                                   ")
print("By Sokol N ")
print("")
print("                                     Hello from BookStore 📚             ")

Stdorteach = input("Are you Student or Teacher (Student/Teacher)")

#Student's  List below

borrowed_books1 = []
return_book1 = []
borrowed_books2 = []
return_book2 = []

#Teacher's  List below

borrowed_bookst1 = []
return_bookt1 = []
borrowed_bookst2 = []
return_bookt2 = []

teacherbk = {}
books = {}

try:
    with open("newdata.json", "r") as json_file:
        data = json.load(json_file)
        books.update(data.get("books", {}))
        borrowed_books1 = data.get("borrowed_books1", [])
        return_book1 = data.get("return_book1", [])
        borrowed_books2 = data.get("borrowed_books2", [])
        return_book2 = data.get("return_book2", [])
        teacherbk.update(data.get("teacherbk", {}))
        borrowed_bookst1 = data.get("borrowed_bookst1", [])
        return_bookt1 = data.get("return_bookt1", [])
        borrowed_bookst2= data.get("borrowed_bookst2", [])
        return_bookt2 = data.get("return_bookt2", [])
except FileNotFoundError:
                pass

if Stdorteach.lower() == 'student':

    Username = input("Enter Your Username: ")
    Password = input("Enter Your Password: ")
    userid_dict = {"sokol":1,"user2":2}
    username_list = ["sokol","user2"]
    password_list = ["sokol@abcd","user2@abcd"]
    
  
    if Username in username_list and Password in password_list:
        print("Hello 👋🏻",Username,"!" )
        
        
        run = True
        while run:
            print("Select the below option  ")
# Asking the user to select an option using input statement
            print("""
            1. View Book Catalogue 
            2. Borrowing a Book
            3. Returning a Book
            4. View Popular Books
            5. End Program
            """)
            response = int(input("Enter option Number (1/2/3/4/5): "))
            
            filename = "newdata.json"
            data = None
            if response ==1:
                
                Library ={    
                    "B001": "Pride & Prejudice",
                    "B002": "Crime & Punishment",
                    "B003": "One Hundred Years of Solitude",
                    "B004": "Annihilation",
                    "B005": "Blindsight",
                    "B006": "Alien: Echo",
                    "B007": "The Luminous Dead",
                    "B008": "The Girl with All the Gifts",
                    "B009": "The Ocean at the End of the Lane",
                    "B010": "Coraline",
                    "B011": "The Graveyard Book",
                    "B012": "Miss Peregrine's Home for Peculiar Children",
                    "B013": "The Maze Runner",
                    "B014": "Ender's Game",
                    "B015": "The Hunger Games",
                    "B016": "A Wrinkle in Time",
                    "B017": "The Give",
                    "B018": "1984",
                    "B019": "Into Thin Air",
                    "B020": "The Boys in the Boat"
                }
                print("The Book Catalogue in BookStore!")
                for book_id, book_name in Library.items():
                    print(f"Book ID: {book_id} - Book Name: {book_name}")
                





    
            elif response == 2:

                num_entries = int(input("Enter number of books to be borrowed: "))
                for i in range(num_entries):
                    value_id = input("Enter ID of Book: ")
                    studentid = int(input("Enter the student ID: "))
                    Nameofbk = input("Enter Name of Book To be Borrowed: ")
                    search = value_id.upper()
                    if search in books and books[search] == True:
                        if studentid in userid_dict.values():
                            if studentid == 1:
                                borrowed_books1.append(search)
                                books[search] = False
                                print("The book was successfully borrowed")
                                print(search,Nameofbk,"is borrowed by",Username)
                       
                            if studentid == 2:
                                borrowed_books2.append(search)
                                books[search] = False
                                print("The book was successfully borrowed")
                                print(search,Nameofbk,"is borrowed by",Username)
                        else:
                             print("Invaild Student ID, Try again")

                    else:
                        print("The book was not found or already borrowed")
                    with open("newdata.json", "w") as json_file:
                        json.dump(
                            {
                                "books": books,
                                "borrowed_books1": borrowed_books1,
                                "return_book1": return_book1,
                                "borrowed_books2": borrowed_books2,
                                "return_book2": return_book2,
                            },
                            json_file,
                            indent=4,
                        )



            elif response == 3:
                num_entries = int(input("Enter number of books to be Returned: "))
                for i in range(num_entries):
                    value_id = input("Enter ID of Book: ")
                    search = value_id.upper()
                    studentid = int(input("Enter the student ID: "))
                    Nameofbk = input("Enter Name of Book To be Returned: ")
                    

                    if search in books and books [search] == False:
                        if studentid in userid_dict.values():
                            if studentid == 1: 
                                if search in borrowed_books1:
                                    books[search] = True
                                    return_book1.append(search)
                                    borrowed_books1.remove(search)
                                    print("The book was successfully Returned")
                                    print(search,Nameofbk,"is Returned by",Username)
                       
                            if studentid == 2: 
                                if search in borrowed_books2:
                                     
                                    borrowed_books2.remove(search)
                                    return_book2.append(search)
                                    books[search] = True
                                    print("The book was successfully Returned")
                                    print(search,Nameofbk,"is Returned by",Username)
                        
                        else:
                            print("Invaild Student ID, Try again")
                        with open("newdata.json", "w") as json_file:
                            json.dump(
                                {
                                    "books": books,
                                    "borrowed_books1": borrowed_books1,
                                    "return_book1": return_book1,
                                    "borrowed_books2": borrowed_books2,
                                    "return_book2": return_book2,
                                    "teacherbk": teacherbk,
                                    "borrowed_bookst1": borrowed_bookst1,
                                    "return_bookt1": return_bookt1,
                                    "borrowed_bookst2": borrowed_bookst2,
                                    "return_bookt2": return_bookt2,
                                },
                                json_file,
                                indent=4,
                            )      

                    else:
                        print("The book was not borrowed or Not found! ")
            

            elif response == 4:
                x = [
                "Pride & Prejudice",
                "1984",
                "Crime & Punishment",
                "One Hundred Years of Solitude",
                "Into Thin Air",
                "The Boys in the Boat",
                ]

                y = [25,34,63,85,53,34]
                plt.bar(x,y, color = "#6C0345", width=0.5, edgecolor="#F7C566" ,lw=2)
                plt.title("Popular Books loved by users of BookStore!")
                plt.xlabel("Book Name")
                plt.ylabel("Votes")
                plt.show()
            elif response == 5:
                print("Thanks for using BookStore!")
                break
            

                run = False
    else:
         print("Please re-enter your credentials correctly. The password or username you provided is invalid.")






 
elif Stdorteach.lower() == 'teacher':


    Usernamet = input("Enter Your Username:")
    Passwordt = input("Enter Your Password:")
    username_teach = ["Prof Bohra","Prof JD"]
    password_teach = ["2.o@abcd","lifeofjd"]
    if Usernamet in username_teach and Passwordt in password_teach:

        print("Hello 👋🏻",Usernamet,"!" )

        
        try:
            with open("newdata.json", "r") as json_file:
                data = json.load(json_file)
                books.update(data.get("books", {}))
                borrowed_books1 = data.get("borrowed_books1", [])
                return_book1 = data.get("return_book1", [])
                borrowed_books2 = data.get("borrowed_books2", [])
                return_book2 = data.get("return_book2", [])
                teacherbk.update(data.get("teacherbk", {}))
                borrowed_bookst1 = data.get("borrowed_bookst1", [])
                return_bookt1 = data.get("return_bookt1", [])
                borrowed_bookst2= data.get("borrowed_bookst2", [])
                return_bookt2 = data.get("return_bookt2", [])
        except FileNotFoundError:
                pass
        runt = True
        while runt:

            print("Select the below option  ")
        
            print("""
            1. View Reference Book Catalogue 
            2. Borrowing a Book
            3. Returning a Book
            4. View Popular Reference materials
            5. End Program
            """)
            responset = int(input("Enter option Number (1/2/3/4/5): "))
            teacherid_dict = {"Prof Bohra":1,"Prof JD":2}
            
            
            if responset == 1:
                    guide = {
                        'B001': 'Early Childhood Education',
                        'B002': 'The Psychology of Prejudice',
                        'B003': 'Dictionaries',
                        'B004': 'Encyclopedias',
                        'B005': 'Mind-Map 10-12',
                        'B006': 'R. D. Sharma Maths',
                        'B007': "T.S. Grewal'S Double Entry Book Keeping",
                        'B008': 'Sandeep Business Studies',
                        'B009': 'CBSE Question Bank',
                        'B010': 'Introductory Macroeconomics',
                        'B011': 'Computer Science With Python',
                        'B012': 'Oswaal Books - Science',
                        'B013': 'NCERT Books',
                        'B014': 'Past Papers - CBSE',
                        'B015': 'AI Class 10 Kips'
                    }
                    print("The Book Catalogue in BookStore!")
                    for book_id, book_name in guide.items():
                        print(f"Book ID: {book_id} - Book Name: {book_name}")

            elif responset == 2:

                    num_entries = int(input("Enter number of books to be borrowed: "))
                    for i in range(num_entries):
                        value_id = input("Enter ID of Book: ")
                        Nameofbk = input("Enter Name of Book To be Borrowed")
                        teacher_idinput = int(input("Enter Teacher ID:"))
                        #not done here ck
                        search = value_id.upper()
                        if search in teacherbk and teacherbk[search] == True:
                            if teacher_idinput in teacherid_dict.values():
                                if teacher_idinput == 1:
                                    borrowed_bookst1.append(search)
                                    teacherbk[search] = False
                                    print("The book was successfully borrowed")
                                    print(search,Nameofbk,"is borrowed by",Usernamet)
                                elif teacher_idinput == 2:
                                    borrowed_bookst2.append(search)
                                    teacherbk[search] = False
                                    print("The book was successfully borrowed")
                                    print(search,Nameofbk,"is borrowed by",Usernamet)
                                else:
                                    print("Invaild Teacher ID, Try again")
                        
                        else:
                            print("The book was not found or already borrowed")
                        with open("newdata.json", "w") as json_file:
                            json.dump(
                                {
                                    "books": books,
                                    "borrowed_books1": borrowed_books1,
                                    "return_book1": return_book1,
                                    "borrowed_books2": borrowed_books2,
                                    "return_book2": return_book2,
                                    "teacherbk": teacherbk,
                                    "borrowed_bookst1": borrowed_bookst1,
                                    "return_bookt1": return_bookt1,
                                    "borrowed_bookst2": borrowed_bookst2,
                                    "return_bookt2": return_bookt2,
                                },
                                json_file,
                                indent=4,
                            )


            elif responset == 3:
                    num_entries = int(input("Enter number of books to be Returned: "))
                    for i in range(num_entries):
                        value_id = input("Enter ID of Book: ")
                        Nameofbk = input("Enter Name of Book To be Returned:")
                        teacher_idinput = int(input("Enter Teacher ID:"))
                        search = value_id.upper()
                        if search in teacherbk and teacherbk [search] == False:
                            if teacher_idinput in teacherid_dict.values():
                                if teacher_idinput == 1:
                                    borrowed_bookst1.remove(search)
                                    return_bookt1.append(search)
                                    teacherbk[search] = True
                                    print("The book was successfully Returned")
                                    print(search,Nameofbk,"is Returned by",Usernamet)
                                elif teacher_idinput == 2:
                                    borrowed_bookst2.remove(search)
                                    return_bookt2.append(search)
                                    teacherbk[search] = True
                                    print("The book was successfully Returned")
                                    print(search,Nameofbk,"is Returned by",Usernamet)
                                else:
                                    print("Invaild Teacher ID, Try again")
                                with open("newdata.json", "w") as json_file:
                                        
                                        json.dump(
                                            {
                                                "books": books,
                                                "borrowed_books1": borrowed_books1,
                                                "return_book1": return_book1,
                                                "borrowed_books2": borrowed_books2,
                                                "return_book2": return_book2,
                                                "teacherbk": teacherbk,
                                                "borrowed_bookst1": borrowed_bookst1,
                                                "return_bookt1": return_bookt1,
                                                "borrowed_bookst2": borrowed_bookst2,
                                                "return_bookt2": return_bookt2,
                                            },
                                            json_file,
                                            indent=4,
                                        )

                        else:
                            print("The Book was already borrowed by other users or  Borrow Books to return  ")

            elif responset == 4:
                    x = ["Psychology of Prejudice",
                    " Maths",
                    "T.S.Human resources",  
                    "Sandeep Grag",
                    "CBSE Question Bank",
                    "Macroeconomics ",
                    "CSC & IP-Python"]

                    y = [38,70,78,68,39,47,57]
                    plt.bar(x,y, color = "#6C0345", width=0.5, edgecolor="#F7C566" ,lw=2)
                    plt.title("Popular Books loved by users of BookStore!")
                    plt.xlabel("Book Name")
                    plt.ylabel("Votes")
                    plt.show()

            elif responset == 5:
                    print("Thanks for using BookStore!")
                    break
                

                    run = False
    else:
        print("Please re-enter your credentials correctly. The password or username you provided is invalid.")