import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ExpenseList() {
  const [expenses, setExpenses] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const token = localStorage.getItem('token');

        const res = await axios.get('http://127.0.0.1:8000/expenses', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        setExpenses(res.data);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch expenses. Make sure you are logged in.');
      }
    };

    fetchExpenses();
  }, []);
  return ( //ADDED
    <div className="text-2xl text-center text-green-600 mt-20">Register Page</div>
  );
  return (
    <div>
      <h2>My Expenses</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {expenses.length === 0 && !error && <p>No expenses found.</p>}
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            <strong>{expense.vendor}</strong> — ${expense.amount} on {expense.date} <br />
            Category: {expense.category || 'N/A'}
          </li>
        ))}
      </ul>
    </div>
  );

  
  
}

export default ExpenseList;
