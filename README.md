# 📚 LibraNet - Python Library Management System  

LibraNet is a simple **object-oriented library management system** built in Python.  
It supports managing **Books**, **Audiobooks**, and **E-Magazines**, with borrowing, returning, due dates, and fines.  

---

## 🚀 Features  
- Add items (`Book`, `Audiobook`, `EMagazine`) to the library.  
- Borrow items with **due date tracking**.  
- Return items and calculate **fines for overdue returns**.  
- Track **availability status** of items.  
- Special behaviors:  
  - **Audiobook** → can be *played*.  
  - **EMagazine** → can be *archived*.  

---

## 🛠 Classes Overview  

### 🔹 `LibraryItem` (Base Class)  
- Attributes: `item_id`, `title`, `author`, `is_borrowed`.  
- Method: `get_details()`.  

### 🔹 `Book(LibraryItem)`  
- Extra attribute: `page_count`.  
- Extended details for page count.  

### 🔹 `Audiobook(LibraryItem)`  
- Extra attribute: `duration_minutes`.  
- Methods:  
  - `play()` → play audiobook.  
  - `get_duration()` → convert minutes to `h:m`.  

### 🔹 `EMagazine(LibraryItem)`  
- Extra attribute: `issue_number`.  
- Methods:  
  - `archive_issue()` → archive magazine.  

### 🔹 `LibraNet` (Library Manager)  
- Manages all items & borrowing records.  
- Methods:  
  - `add_item(item)`  
  - `borrow_item(item_id, duration_days)`  
  - `return_item(item_id)`  
  - `list_all_items()`  

---

## 📖 Example Usage  

```python
from library import Book, Audiobook, EMagazine, LibraNet

# 1. Create library
libra_net = LibraNet()

# 2. Add items
book1 = Book(101, "Spider-Man: Into the Spider-Verse", "Marvel Comics", 145)
audiobook1 = Audiobook(204, "Attack on Titan Vol. 1 (Manga Audio Edition)", "Hajime Isayama", 240)
emagazine1 = EMagazine(301, "National Geographic", "Nat Geo Society", 245)

libra_net.add_item(book1)
libra_net.add_item(audiobook1)
libra_net.add_item(emagazine1)

# 3. Borrow and return
libra_net.borrow_item(101, 14)   # Borrow book for 14 days
libra_net.return_item(101)       # Return it
