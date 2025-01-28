import sqlite3
con=sqlite3.connect('/home/synnefo/athul/files/python/database/Library.db')
try: 
    con.execute('create table book(id int,name text,author text,price int)')
except:
    pass
          
        
        
        
            
        
        
    
    
        