# 📄 File Find and Replace Utility (Python)

## 📌 Project Overview

This project is a simple Python application that demonstrates the fundamentals of **File Input/Output**, **String Manipulation**, and **Exception Handling**.

The program reads the contents of a text file, searches for a user-specified word, replaces it with another word, and saves the updated content back to the same file. It also handles common file-related errors gracefully to prevent the program from crashing.

---

## 🚀 Features

* Read data from a text file.
* Display the current file contents.
* Find a specific word entered by the user.
* Replace the word with a new word.
* Save the modified content back to the file.
* Notify the user if the word is not found.
* Handle common file-related exceptions gracefully.

---

## 🛠 Technologies Used

* Python 3
* File Handling
* String Manipulation
* Exception Handling

---

## 📚 Concepts Covered

### File Handling

* `open()`
* `read()`
* `write()`
* `with` statement
* File modes (`r`, `w`)

### String Operations

* `replace()`
* Membership operator (`in`)

### Exception Handling

* `try`
* `except`
* `FileNotFoundError`
* `PermissionError`
* Generic `Exception`

---

## 📂 Project Structure

```text
File-Find-and-Replace/
│
├── main.py
├── sample.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Place your text file (for example, `sample.txt`) in the project folder.
3. Run the program:

```bash
python main.py
```

4. Enter:

   * File name
   * Word to find
   * Replacement word

5. The updated content will be saved automatically.

---

## 📥 Sample Input

File (`sample.txt`)

```text
Python is easy to learn.
Python is powerful.
I love Python.
```

User Input

```text
Enter file name:
sample.txt

Enter word to find:
Python

Enter replacement word:
Java
```

---

## 📤 Sample Output

```text
Word replaced successfully!
```

Updated File

```text
Java is easy to learn.
Java is powerful.
I love Java.
```

---

## ⚠️ Exception Handling

The program handles the following situations:

* File does not exist.
* Permission denied while accessing the file.
* Any unexpected runtime errors.

This ensures the program continues gracefully instead of terminating unexpectedly.

---

## 🎯 Learning Outcomes

By completing this project, you will gain hands-on experience with:

* Reading data from files.
* Writing data back to files.
* Performing string replacement operations.
* Handling exceptions using `try` and `except`.
* Building a simple real-world console application.

---

## 🔮 Possible Future Enhancements

* Replace only the first occurrence of a word.
* Display the total number of replacements made.
* Perform case-insensitive word replacement.
* Create a backup of the original file before modifying it.
* Allow multiple find-and-replace operations in a single run.
* Support replacing entire phrases instead of just single words.
* Provide a simple graphical user interface using Tkinter.

---

## 👩‍💻 Author

**Ayushi Srivastava**

Built as a practice project to strengthen Python fundamentals in:

* File Handling
* String Manipulation
* Exception Handling
