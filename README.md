A simple Python-based expense tracking application that allows users to record and analyze their monthly expenses by category. 
Take a picture and upload it for it to be parsed, then see your data!

*Features

Create and manage monthly expense data (YYYY-MM format)

Add expenses with categories and amounts

Calculate total expenses by category for a given month

Automatically creates monthly records if they don’t exist

*Project Structure

User → Manages user data and monthly records

MonthlyData → Stores expenses for a specific month

Expense → Represents a single expense (amount + category)

Category → Enum or class representing expense categories
