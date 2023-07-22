import os
import datetime

class LMS:
    """"This class is use to keep records of Library.
        it has total 4 modules which is :-
        1. Display Bool
        2. Issue Books
        3. Return Books
        4. Add Books """
    
    # Creating a Constracter
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        ID = 1001
        with open(self.list_of_books) as lbk:
            content = lbk.readlines()
        for line in content:
            self.books_dict.update({str(ID):{"Books_title":line.replace("\n",""),
            "Lender_name":"", "Issue_Date":"", "Status":"Available"}})
            ID = ID+1
    def display_books(self):
        print("------------------List of Books------------------")
        print("Books ID","\t","Title")
        print("-------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("Books_title"), "- [",value.get("Status"),"]")
    
    def Issue_Books(self):
        books_id = input("Enter Books ID:- ")
        current_date = datetime.datetime.now().strftime("%y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This Book is already issued to {self.books_dict[books_id]['Lender_name']} on {self.books_dict[books_id]['Issue_Date']}")
                return self.Issue_Books()
            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter Your Name:- ")
                self.books_dict[books_id]['Lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issues"
                print("Books Issued Successfully !!! \n")
            else:
                print("Book ID Not Found !!!")
                return self.Issue_Books()
    
    def Add_Book(self):
        new_books = input("Enter books title: ")
        if new_books == "":
            return self.Add_Book()
        elif len(new_books) > 25:
            print("Books title legth is too long !!! The title should be of 20 Chars")
            return self.Add_Book()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'Books_title':new_books,'Lender_name':"",
                                                                         'Issue_date':"",'Status':'Available'}})
                print(f"This Book '{new_books}' has been added successfully !!!")
    
    def return_book(self):
        book_id = input("Enter Book ID:- ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"] == "Available":
                print("This Book is already available in library. Please check your Book ID.")
                return self.return_book()
            elif not self.books_dict[book_id]["Status"] == "Available":
                self.books_dict[book_id]["Lender_name"] == ""
                self.books_dict[book_id]["Issue_date"] == ""
                self.books_dict[book_id]["Status"] == "Available"
                print("Successfully Updated !!! \n")
try:
    myLMS = LMS("list_of_books.txt","Python's Library")
    press_key_list = {"D":"Display Books",
                      "I":"Issus Books",
                      "A":"Add Books",
                      "R":"Return Books",
                      "Q":"Quit Opration"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n------------------Welcome To {myLMS.library_name} Library Management System------------------")
        for key,value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press Key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Books")
            myLMS.Issue_Books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Books")
            myLMS.Add_Book()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books")
            myLMS.display_books()
        elif key_press=="r":
            print("\nCurrent Selection : Return Books")
            myLMS.Return_book()
        elif key_press=="q":
            break
        else:
            continue
except Exception as e:
        print("Somethin went wrrong. Please Check your Input !!!")