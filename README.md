# 📊 Project: Personal Finance Manager (Python CLI)
### 📌 Overview
This project is a functional milestone in my Data Science journey, transitioning from Python Basics to Structured Logic and OOP Preparation. It is a terminal-based tool designed to manage user accounts and financial transactions with high resilience.

### 🐍 Python Core Concepts Applied
* Data Structures
* Nested Dictionaries: Storing complex user profiles (Age, Balance) within a primary details dictionary.
* Key-Value Mapping: Efficient retrieval and updating of specific user records.

### Control Flow & Logic
* Match-Case (Python 3.10+): Modern, readable menu navigation.
* In-place Operators: Using += and -= for streamlined balance updates.
* Guard Clauses: Implementing early return statements to handle missing data gracefully.

### Input Sanitization
* .lower(): Standardizing string input for case-insensitive matching.
* .strip(): Removing accidental whitespace to prevent "KeyNotFound" errors.

### 🛡️ Exception Handling & Robustness
* Try-Except Blocks
* ValueError Handling: Validating numeric inputs for Age and Amount to prevent program crashes.
* Scope Management: Ensuring variables are safely defined before performing arithmetic operations.

### Crash-Proof Execution
* Preventing NameError by using return guards in error-prone functions.
* Protecting the "Happy Path" by validating account existence before processing debits.

### 🏗️ Transitioning to OOP (Object-Oriented Programming)
* Modular Design
* Encapsulating logic into distinct functions (add_user, add_expense, delete_entry).
* Preparing the codebase for a full refactor into a User class and a Bank class.

### State Management
* Practicing how to maintain a global state (the details dictionary) which acts as the precursor to Class Attributes.

## 🚀 Key Features
* CRUD Operations: Create, Read, Update, and Delete user entries.
* Transaction Engine: Process credit and debit with real-time balance calculations.
* Fault Tolerance: Designed to handle "bad" user input without exiting the application.

## 📈 Future Roadmap (v2.0)
* JSON Persistence: Integrating the json module to save data to local files.
* OOP Refactor: Converting functional logic into a full Class-based system.
* Analytics: Adding basic statistics (Total Revenue, Average Balance) using Excel-inspired math.
