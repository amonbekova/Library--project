import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Ҷадвали китобҳо
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        isbn TEXT UNIQUE,
                        quantity INTEGER DEFAULT 1)''')
    
    # Ҷадвали хонандагон
    cursor.execute('''CREATE TABLE IF NOT EXISTS readers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fullname TEXT NOT NULL,
                        phone TEXT)''')
    
    # Ҷадвали додани китобҳо
    cursor.execute('''CREATE TABLE IF NOT EXISTS issues (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book_id INTEGER,
                        reader_id INTEGER,
                        issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        return_date TEXT,
                        status TEXT DEFAULT 'Issued',
                        FOREIGN KEY(book_id) REFERENCES books(id),
                        FOREIGN KEY(reader_id) REFERENCES readers(id))''')
    
    conn.commit()
    conn.close()

init_db()
def add_book_to_db(title, author, isbn, qty):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO books (title, author, isbn, quantity) VALUES (?, ?, ?, ?)", 
                       (title, author, isbn, qty))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def fetch_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows
import tkinter as tk
from tkinter import messagebox, ttk


