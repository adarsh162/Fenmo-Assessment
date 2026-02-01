import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_URL,
});

export const expenseService = {
  getExpenses: (category = '', sort = 'date_desc') => {
    const params = new URLSearchParams();
    if (category) params.append('category', category);
    if (sort) params.append('sort', sort);
    return api.get(`/expenses/?${params.toString()}`);
  },

  createExpense: (expenseData) => {
    return api.post('/expenses/', expenseData);
  }
};