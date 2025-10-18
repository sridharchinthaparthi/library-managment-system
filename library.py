books = []
members = []
issued_books = []

def show_menu():
    print("\n" + "=" * 40)
    print("  LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. Show All Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Calculate Fine")
    print("9. Library Statistics")
    print("10. Exit")
    print("=" * 40)

def add_book():
    print("\nAdd New Book")
    bid = input("Book ID: ")
    title = input("Book Title: ")
    author = input("Author Name: ")
    copies = int(input("Number of Copies: "))
    
    book = {
        "id": bid,
        "title": title.title(),
        "author": author.title(),
        "copies": copies,
        "available": copies
    }
    books.append(book)
    print(f"Book '{title}' added successfully!")

def show_books():
    if len(books) == 0:
        print("\nNo books in library!")
        return
    
    print("\n" + "=" * 70)
    print("ALL BOOKS")
    print("=" * 70)
    for b in books:
        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']}")
        print(f"Total: {b['copies']} | Available: {b['available']}")
        print("-" * 70)

def search_book(search_term="", depth=0):
    if search_term == "":
        search_term = input("\nEnter book title or author name: ").lower()
    
    found = []
    for b in books:
        if search_term in b['title'].lower() or search_term in b['author'].lower():
            found.append(b)
    
    if len(found) > 0:
        print(f"\nFound {len(found)} book(s):")
        for book in found:
            print(f"- {book['title']} by {book['author']} (ID: {book['id']})")
        return found
    else:
        if depth < 2:
            print("No books found. Try another search?")
            new_search = input("Enter search term (or press Enter to skip): ").lower()
            if new_search != "":
                return search_book(new_search, depth + 1)
        print("No matching books found.")
        return []

def add_member():
    print("\nAdd New Member")
    mid = input("Member ID: ")
    name = input("Member Name: ")
    phone = input("Phone Number: ")
    
    member = {
        "id": mid,
        "name": name.title(),
        "phone": phone,
        "books_issued": 0
    }
    members.append(member)
    print(f"Member '{name}' added successfully!")

def show_members():
    if len(members) == 0:
        print("\nNo members registered!")
        return
    
    print("\n" + "=" * 60)
    print("ALL MEMBERS")
    print("=" * 60)
    for m in members:
        print(f"ID: {m['id']} | Name: {m['name']} | Phone: {m['phone']}")
        print(f"Books Issued: {m['books_issued']}")
        print("-" * 60)

def find_book(book_id):
    for b in books:
        if b['id'] == book_id:
            return b
    return None

def find_member(member_id):
    for m in members:
        if m['id'] == member_id:
            return m
    return None

def issue_book():
    print("\nIssue Book")
    mid = input("Member ID: ")
    bid = input("Book ID: ")
    
    member = find_member(mid)
    book = find_book(bid)
    
    if member == None:
        print("Member not found!")
        return
    
    if book == None:
        print("Book not found!")
        return
    
    if book['available'] <= 0:
        print("Book not available!")
        return
    
    if member['books_issued'] >= 3:
        print("Member has already issued 3 books!")
        return
    
    days = int(input("Issue for how many days? "))
    
    issue_record = {
        "member_id": mid,
        "member_name": member['name'],
        "book_id": bid,
        "book_title": book['title'],
        "days_allowed": days
    }
    
    issued_books.append(issue_record)
    book['available'] -= 1
    member['books_issued'] += 1
    
    print(f"\nBook '{book['title']}' issued to {member['name']} for {days} days.")

def return_book():
    print("\nReturn Book")
    mid = input("Member ID: ")
    bid = input("Book ID: ")
    days_taken = int(input("How many days book was kept? "))
    
    record_found = None
    for idx, rec in enumerate(issued_books):
        if rec['member_id'] == mid and rec['book_id'] == bid:
            record_found = idx
            break
    
    if record_found == None:
        print("No such issue record found!")
        return
    
    issue_rec = issued_books[record_found]
    allowed = issue_rec['days_allowed']
    
    if days_taken > allowed:
        extra_days = days_taken - allowed
        fine = calculate_fine_recursive(extra_days)
        print(f"\nBook returned late by {extra_days} days.")
        print(f"Fine Amount: ${fine:.2f}")
    else:
        print("\nBook returned on time. No fine!")
    
    book = find_book(bid)
    member = find_member(mid)
    
    book['available'] += 1
    member['books_issued'] -= 1
    
    issued_books.pop(record_found)
    print(f"Book '{issue_rec['book_title']}' returned successfully!")

def calculate_fine_recursive(days, rate=2):
    if days <= 0:
        return 0
    return rate + calculate_fine_recursive(days - 1, rate)

def calculate_fine_menu():
    print("\nCalculate Fine")
    late_days = int(input("Enter number of late days: "))
    
    if late_days <= 0:
        print("No fine!")
        return
    
    fine = calculate_fine_recursive(late_days)
    print(f"Total Fine for {late_days} days: ${fine:.2f}")

def count_books_recursive(book_list, index=0):
    if index >= len(book_list):
        return 0
    return book_list[index]['copies'] + count_books_recursive(book_list, index + 1)

def library_stats():
    print("\n" + "=" * 50)
    print("LIBRARY STATISTICS")
    print("=" * 50)
    
    total_books = count_books_recursive(books)
    print(f"Total Books in Library: {total_books}")
    print(f"Total Unique Titles: {len(books)}")
    print(f"Total Members: {len(members)}")
    print(f"Books Currently Issued: {len(issued_books)}")
    
    available_count = 0
    for b in books:
        available_count += b['available']
    print(f"Books Available: {available_count}")
    
    if len(issued_books) > 0:
        print("\nCurrently Issued Books:")
        for issue in issued_books:
            print(f"  - {issue['book_title']} issued to {issue['member_name']}")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            add_member()
        elif choice == "5":
            show_members()
        elif choice == "6":
            issue_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            calculate_fine_menu()
        elif choice == "9":
            library_stats()
        elif choice == "10":
            print("\nThank you for using Library Management System!")
            break
        else:
            print("\nInvalid choice! Try again.")

main()