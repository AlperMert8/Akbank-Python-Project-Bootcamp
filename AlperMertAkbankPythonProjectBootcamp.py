# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:17:20 2024

@author: LENOVO
"""
import os
class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            self.file = open(self.file_name, "a+")
        self.file = open(self.file_name, "r+")
    
    def __del__(self):
        self.file.close()
        
    def list_books(self):
        self.file.seek(0)
        lines = self.file.readlines()
        if not lines:
            print("There are no books in the file!")
            return
        for line in lines:
            information = line.strip().split(',')
            print(f"Book Name: {information[0]}, Author: {information[1]}")
    
    
    def add_book(self, title, author, release_year, page_number):
         information = f"{title},{author},{release_year},{page_number}\n"
         self.file.write(information)
         
    def remove_book(self, title):
          self.file.seek(0)
          lines = self.file.readlines()
          self.file.seek(0)
          self.file.truncate()
          for line in lines:
            if title not in line:
                self.file.write(line)
          if not any(title in line for line in lines):
              print(f"{title} named book does not exist in file")

lib = Library()
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    
    
    choice = input("Please enter a number(1,2,3) to make operations: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        title = input("Title of the Book: ")
        author = input("Author of the Book: ")
        release_year = input("Release Year of the Book: ")
        page_number = input("Page Number of the Book: ")
        lib.add_book(title, author, release_year, page_number)
    elif choice == "3":
        title = input("Please enter the book name you want to delete: ")
        lib.remove_book(title)
    else:
        print("Exiting!")
        break