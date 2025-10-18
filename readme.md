# Library Management System 📖

A Python-based library management system with book tracking, member management, and automated fine calculation using functions and recursion.

<div align="center">

### Don't want to clone? No problem! Run it instantly:

[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-green?style=for-the-badge&logo=github)](https://codespaces.new/sridharchinthaparthi/library-managment-system)

**Perfect for:**
- 📱 Mobile browsing - Test from your phone!
- ⚡ Quick exploration - No setup required
- 🧪 Experimentation - Fork and modify

</div>

## Features

- **Book Management**
  - Add new books with multiple copies
  - View all books with availability status
  - Search books by title or author (with recursive retry)
  - Track available vs issued copies

- **Member Management**
  - Register new library members
  - View all registered members
  - Track number of books issued per member
  - Limit of 3 books per member

- **Issue & Return System**
  - Issue books to members with due date
  - Return books with automatic fine calculation
  - Track all issued books
  - Automatic inventory update

- **Fine Calculation**
  - Recursive fine calculation (₹2 per day)
  - Late return penalty system
  - Standalone fine calculator

- **Statistics & Reports**
  - Total books count (using recursion)
  - Available vs issued books
  - Currently issued book list
  - Member statistics

## Technologies Used

- Python 3.10
- Functions (modular programming)
- Recursive functions
- Dictionary and List data structures
- Menu-driven interface

## Skills Demonstrated

This project showcases proficiency in:

**From Previous Projects:**
- Variables, data types, and operators
- Lists and dictionaries
- Loops and conditional statements
- String manipulation
- Input/output operations

**New Concepts:**
- **Functions**: Modular code organization with multiple functions
- **Function Parameters**: Passing data between functions
- **Return Values**: Functions returning processed data
- **Recursion**: 
  - `calculate_fine_recursive()` - calculates fine recursively
  - `count_books_recursive()` - counts total books using recursion
  - `search_book()` - recursive retry mechanism
- **Helper Functions**: `find_book()`, `find_member()` for code reusability
- **Default Parameters**: Functions with optional parameters
- **Menu-Driven Programming**: User interaction through function calls

## Installation

```bash
git clone https://github.com/sridharchinthaparthi/library-management-system.git
cd library-management-system
```

## Usage

Run the program:

```bash
python library.py
```

### Main Menu Options:

1. **Add Book** - Add new books to the library
2. **Show All Books** - Display complete book inventory
3. **Search Book** - Find books by title or author
4. **Add Member** - Register new library members
5. **Show All Members** - View all registered members
6. **Issue Book** - Issue a book to a member
7. **Return Book** - Return a book and calculate fine if late
8. **Calculate Fine** - Check fine for late days
9. **Library Statistics** - View library analytics
10. **Exit** - Close the application

## Example Usage

```
========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 2

No books in library!

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 1

Add New Book
Book ID: 1
Book Title: The Hidden Admirer
Author Name: Chinthaparthi Sridhar
Number of Copies: 10
Book 'The Hidden Admirer' added successfully!

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 5

No members registered!

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 4

Add New Member
Member ID: 1
Member Name: sri
Phone Number: 7032238926
Member 'sri' added successfully!

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 6

Issue Book
Member ID: 1
Book ID: 1
Issue for how many days? 10

Book 'The Hidden Admirer' issued to Sri for 10 days.

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 7

Return Book
Member ID: 1
Book ID: 1
How many days book was kept? 2

Book returned on time. No fine!
Book 'The Hidden Admirer' returned successfully!

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 9

==================================================
LIBRARY STATISTICS
==================================================
Total Books in Library: 10
Total Unique Titles: 1
Total Members: 1
Books Currently Issued: 0
Books Available: 10

========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Show All Books
3. Search Book
4. Add Member
5. Show All Members
6. Issue Book
7. Return Book
8. Calculate Fine
9. Library Statistics
10. Exit
========================================

Enter your choice: 10

Thank you for using Library Management System!.
```

## Fine Calculation

- **Rate**: ₹2 per day for late returns
- **Calculation Method**: Recursive function
- **Example**: 5 days late = ₹10 fine

## Code Structure

```
library.py
├── Global Variables (books, members, issued_books)
├── show_menu() - Display menu
├── add_book() - Add new book
├── show_books() - List all books
├── search_book() - Recursive search
├── add_member() - Register member
├── show_members() - List members
├── find_book() - Helper function
├── find_member() - Helper function
├── issue_book() - Issue book to member
├── return_book() - Process book return
├── calculate_fine_recursive() - Recursive fine calculation
├── calculate_fine_menu() - Fine calculator interface
├── count_books_recursive() - Recursive counting
├── library_stats() - Display statistics
└── main() - Main program loop
```

## Learning Objectives

This project demonstrates:
- Breaking complex problems into smaller functions
- Using recursion for calculations and counting
- Managing related data with multiple data structures
- Creating reusable helper functions
- Building menu-driven applications
- Implementing business logic (issue/return workflow)

## Limitations

- No data persistence (data lost after closing)
- No date tracking (uses day count instead)
- Basic validation
- In-memory storage only

## Future Enhancements

- Add file storage for data persistence
- Implement date-based tracking
- Add book reservation system
- Generate detailed reports
- Email notifications for due dates
- Advanced search filters

## Author

**Sridhar Chinthaparthi**

GitHub: [@sridharchinthaparthi](https://github.com/sridharchinthaparthi)

## License

This project is open source and available under the MIT License.

---


*Built with Python to practice functions and recursion concepts.*
