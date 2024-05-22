# This function greets the user and welcome them
def greeting():
  print("Hello, welcome to the Book Nook!")
greeting()

# These lines of code declare a variable and then uses it in a print statement
book1 = "Pride & Prejudice"
print(f"Are you into fiction? Read {book1}!")

book2 = "Harry Potter"
print(f"Or do you like fantasy? Give {book2} a try!")

# These lines of code create a named constant variable then uses it in a print statement
rbook = 2 
print(f"The amount of book recommendations I have is {rbook}")

# These lines of code creates an if else statement and then uses it in a print statement
read_books = 4
if read_books < 2:
  print("You need to read more books!")
else: 
  print("You are a bookworm!")

# These lines of code create a list of books and then uses each item in a print statement
book_list = ["Pride & Prejudice", "Harry Potter", "Lyrical Ballads", "American Prometheus"]
print(f"Book List: {book_list}")
zero_book = book_list[0]
print(f"Fiction Book: {zero_book}")
second_book = book_list[1]
print(f"Fantasy Book: {second_book}")
third_book = book_list[2]
print(f"Poetry Book: {third_book}")
fourth_book = book_list[3]
print(f"Nonfiction Book: {fourth_book}")

# These lines of code creates a tuple of authors and uses one item in a print statement
authors_tuple = ("Jane Austen", "J.K. Rowling", "Wordsworth & Coleridge", "Kai Bird")
print(f"Authors: {authors_tuple}")
a_author = authors_tuple[0]
print(f"Author of Little Women: {a_author}")