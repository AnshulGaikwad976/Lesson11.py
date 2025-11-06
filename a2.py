class library:
    def __init__(self,books_list):
        self.books = books_list
        self.lended_books = {}

    def display_books(self):
        print("\n available books:") 
        for book in self.books:
            print(f"{book}")
        print(book)

    def lend_book(self , book_name ,user):
        if book_name in self.books:
            if book_name not in self.lended_books:
                self.lended_books [book_name] = user
                print(f"\n '{book_name}' has been lend to {user}")
            else:
                print(f"\n sorry '{book_name} is already lent to {self.lended_books[book_name]}.")
        else:
            print("\n this book is not available in the liabrary")  

    def add_books(self , book_name):
                self.books.append(book_name)
                print(f"\n'{book_name}' has been added to the library ")
    def return_book(self , book_name ):
         if book_name in self.lended_books:
              del self.lended_books[book_name]
              print(f"\n '{book_name}' has been returned to the library")  
         else:
              print("\n this book was not lent from the library") 

my_library = library(["harry potter" ,"python basics" , "data structures" , "rich and poor dad"])  

while True:
   print("\n====== library menu ======") 
   print("1. Display books")
   print("2. lend a book")
   print("3. return a book ")
   print("4. add a book ")
   print("5. exit")

   choice = input("Enter your choice(1-5):")

   if choice == '1':
      my_library.display_books()
   elif choice == '2' :
        book = input("Enter the name of the book u want to borrow ") 
        user = input("Enter your name:")
        my_library.lend_book(book,user)
   elif choice == '3':
        book = input("Enter the name of the book u want to return:")
        my_library.return_book(book)
   elif choice == '4':
        book = input("Enter the name of the book u want to add:")
        my_library.add_books(book)
   elif choice == '5':
        print("\n exiting library system thank you!")
        break
   else:
        print("\n Invalid choice1 Please enter the number between 1-5")

        