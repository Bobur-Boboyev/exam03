from datetime import datetime

class Book():

    def __init__(self, id: int, title: str, author: str, pages: int):
        
        if id > 0:
            self.id = id
        else:
            raise ValueError("ID musbat son bo'lishi kerak!")
        
        if title:
            self.title = title
        else:
            raise ValueError("Title bo'sh bo'lmasligi kerak!")
        
        if author:
            self.author = author
        else:
            raise ValueError("Author bo'sh bo'lmasligi kerak!")
        
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError("Pages 0 dan katta bo'lishi kerak!")
        
        self.is_borrowed: bool = False
        self.borrower: str|None = None
        self.borrow_history: list[tuple[str, datetime]] = []
        self.archived: bool = False
    

    def borrow(self, user: str) -> None:
        if self.archived == True:
            raise RuntimeError
        if self.is_borrowed == True:
            raise RuntimeError
        
        self.is_borrowed = True
        self.borrower = user
        self.borrow_history.append((user, datetime.now()))


    def return_book(self)  -> None:
        if self.is_borrowed == False:
            raise RuntimeError()
        self.borrower = None
        self.is_borrowed = False


    def change_title(self, new_title: str) -> None:
        if self.archived == True:
            raise RuntimeError()
        self.title = new_title


    def archive(self) -> None:
        if self.is_borrowed == True:
            raise RuntimeError()
        self.archived = True


    def info(self) -> dict:
        status = "archived" if self.archived == True else ("borrowed" if self.is_borrowed == True else "available")

        info = {
            "id": self.id,
            "title": self.title, 
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history)
            }
        
        return info


    def __str__(self):
        return f"<Book {self.title}>"


    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', borrowed={self.is_borrowed})"


    def __eq__(self, other):
        return self.id == other.id


    def __len__(self):
        return self.pages
    

    def __bool__(self):
        return not self.archived



        