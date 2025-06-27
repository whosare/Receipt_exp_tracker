import axios from 'axios';

const API = axios.create({ //instance of the axios client
    baseURL : 'http://localhost:8000', //allows us to specify our endpoint without typing full url
});
export const registerUser = (userData) => API.post('/register', userData); //post request sent with user register to /register
export const loginUser = (credentials) => API.post('/login', credentials);  //post request sending login cred to /login

export const uploadReceipt = (formData, token) =>
  API.post('/upload', formData, {
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' },
  }); //post request to /upload using formData object (file)

  export const fetchExpenses = (token) =>
  API.get('/expenses', {
    headers: { Authorization: `Bearer ${token}` },
  }); //GET request to /expenses 

export const deleteExpense = (id, token) =>
  API.delete(`/expense/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
  });

export default API;