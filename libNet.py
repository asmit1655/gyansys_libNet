import datetime

class LibraryItem:
    """
    A base blueprint for a generic item in the library.
    """
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def get_details(self):
        """
        Gets a formatted string of the item's details.
        """
        availability = "Available" if not self.is_borrowed else "Borrowed"
        return f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Status: {availability}"

class Book(LibraryItem):
    """Represents a physical book. It's a LibraryItem, but with a page count."""
    def __init__(self, item_id, title, author, page_count):
        super().__init__(item_id, title, author)
        self.page_count = page_count 

    def get_page_count(self):
        return self.page_count

    def get_details(self):
        availability = "Available" if not self.is_borrowed else "Borrowed"
        return (f"[Book] ID: {self.item_id}, Title: {self.title}, Author: {self.author}, "
                f"Pages: {self.page_count}, Status: {availability}")

class Audiobook(LibraryItem):
    """Represents an audiobook. It's a LibraryItem, but with a duration."""
    def __init__(self, item_id, title, author, duration_minutes):
        super().__init__(item_id, title, author)
        self.duration_minutes = duration_minutes 

    def play(self):
        """A special action only audiobooks can do."""
        print(f"Playing '{self.title}'...")

    def get_duration(self):
        """Converts minutes into an hours and minutes format."""
        hours, minutes = divmod(self.duration_minutes, 60)
        return f"{hours}h {minutes}m"
        
    def get_details(self):
        availability = "Available" if not self.is_borrowed else "Borrowed"
        return (f"[Audiobook] ID: {self.item_id}, Title: {self.title}, Author: {self.author}, "
                f"Duration: {self.get_duration()}, Status: {availability}")

class EMagazine(LibraryItem):
    """Represents an e-magazine. It's a LibraryItem, but with an issue number."""
    def __init__(self, item_id, title, publisher, issue_number):
        # For magazines, 'author' can be thought of as the publisher.
        super().__init__(item_id, title, publisher)
        self.issue_number = issue_number
        self.is_archived = False

    def archive_issue(self):
        """A special action for e-magazines."""
        self.is_archived = True
        print(f"EMagazine '{self.title}' Issue {self.issue_number} has been archived.")

    def get_details(self):
        availability = "Available" if not self.is_borrowed else "Borrowed"
        return (f"[E-Magazine] ID: {self.item_id}, Title: {self.title}, Publisher: {self.author}, "
                f"Issue: {self.issue_number}, Status: {availability}")

# --- Library Management System ---
class LibraNet:
    """
    This class manages the whole library.
    """
    FINE_PER_DAY = 10.0 # in rupees

    def __init__(self):

        self._items = {}  # Stores all items: {item_id: LibraryItem object}
        self._borrowed_records = {} # Stores due dates: {item_id: due_date}

    def add_item(self, item):
        """Adds a new book, audiobook, or e-magazine to the library."""
        # We use the item's id as the key in our dictionary.
        self._items[item.item_id] = item
        print(f"Added '{item.title}' to the library.")

    def borrow_item(self, item_id, duration_days):
        """Handles borrowing an item from the library."""
        # First, check if the item exists.
        if item_id not in self._items:
            print(f"Error: No item found with ID: {item_id}")
            return

        item = self._items[item_id]

        # Second, check if it's already borrowed.
        if item.is_borrowed:
            print(f"Error: '{item.title}' is already borrowed.")
            return

        # If everything is okay, we can borrow it.
        item.is_borrowed = True
        
        # Calculate the due date.
        borrow_duration = datetime.timedelta(days=duration_days)
        due_date = datetime.date.today() + borrow_duration
        
        # Record the due date.
        self._borrowed_records[item_id] = due_date
        print(f"'{item.title}' has been borrowed. It is due on {due_date.strftime('%Y-%m-%d')}.")

    def return_item(self, item_id):
        """Handles returning an item to the library."""
        # Check if the item exists.
        if item_id not in self._items:
            print(f"Error: No item found with ID: {item_id}")
            return
            
        item = self._items[item_id]

        # Check if it was actually borrowed.
        if not item.is_borrowed:
            print(f"Error: '{item.title}' is not currently borrowed.")
            return

        # Calculate any fines.
        due_date = self._borrowed_records[item_id]
        today = datetime.date.today()
        if today > due_date:
            days_overdue = (today - due_date).days
            fine = days_overdue * self.FINE_PER_DAY
            print(f"A fine of ₹{fine:.2f} is due for the late return of '{item.title}'.")

        # Mark the item as available again.
        item.is_borrowed = False
        # Remove the borrowing record.
        del self._borrowed_records[item_id]
        print(f"'{item.title}' has been successfully returned.")
        
    def list_all_items(self):
        """Prints details of all items in the library."""
        print("\n--- LibraNet Catalog ---")
        for item in self._items.values():
            print(item.get_details())
        print("------------------------")

# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Create a new library instance.
    libra_net = LibraNet()

    # 2. Create some items and add them to the library.
    print("--- Populating the Library ---")
    book1 = Book(101, "Spider-Man: Into the Spider-Verse", "Marvel Comics", 145)
    book2 = Book(105, "Death Note Vol. 1", "Tsugumi Ohba & Takeshi Obata", 195)
    audiobook1 = Audiobook(204, "Attack on Titan Vol. 1 (Manga Audio Edition)", "Hajime Isayama", 240)
    emagazine1 = EMagazine(301, "National Geographic", "Nat Geo Society", 245)
    
    libra_net.add_item(book1)
    libra_net.add_item(book2)
    libra_net.add_item(audiobook1)
    libra_net.add_item(emagazine1)
    print("-" * 30)
    
    # 3. List all the items to see their current status.
    libra_net.list_all_items()
    
    # 4. Let's borrow an item.
    print("\n--- Simulating Borrowing ---")
    libra_net.borrow_item(105, 14) # Borrow "Death Note Vol.1" for 14 days.
    libra_net.borrow_item(204, 30) # Borrow "Attack on Titan Vol. 1" for 30 days.
    print("-" * 30)
    
    # 5. List all items again to see the updated status.
    libra_net.list_all_items()

    # 6. Try to borrow an item that is already checked out.
    print("\n--- Testing an Error Case ---")
    libra_net.borrow_item(105, 5) # Try to borrow "Death Note Vol.1" again.
    print("-" * 30)

    # 7. Return an item.
    print("\n--- Simulating a Return ---")
    libra_net.return_item(105) # Return "Death Note Vol.1"
    print("-" * 30)