import sqlite3
con=sqlite3.connect('/home/synnefo/athul/files/python/database/Library.db')
try: 
    con.execute('create table book(id int,name text,author text,price int)')
except:
    pass

while True:
    print('''
        1.Book Add
        2.Search Book
        3.Update Book
        4.Delete Book''')
    choice=int(input("Enter your choice: "))
    if choice==1:
        n=int(input("enter number of books added:")) 
        for i in range(1,n+1):
            id=int(input("Enter book id: "))
            name = input("Enter book title: ")
            author = input("Enter book author: ")
            price = int(input("Enter publishing price: "))

            con.execute("insert into book values(?,?, ?, ?)", (id,name, author, price))
            con.commit()
            print(" Books added successfully!")


    elif choice ==2:
        search = input("Enter book id to search: ")
        data=con.execute("select * from book where id = (?)", (search,))
        id=data.fetchone()
        if id:
            print('Book found')
            print(id)
        else:
            print('Not found')
    elif choice==3:
        update=int(input("enter book id to update :"))
        new_price=int(input("enter new price :"))
        con.execute('update book set price=(?) where id=(?)',(new_price,update,))
        print("book updated")
        con.commit()
        
  
    elif choice ==4:
        book_id = int(input("Enter book id to delete: "))
        data=con.execute("select * from book where id = (?)", (book_id,))
        data2=data.fetchone()
        if data2:
            con.execute('delete from book where id=(?)',(data2[0],))
            print('deleted')
        else:
            print('Not found')

        con.commit()
        

    
        
        
        
        
    
    
        