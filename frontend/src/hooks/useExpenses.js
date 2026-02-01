import { useState, useEffect, useMemo } from 'react';
import { expenseService } from '../services/api';

export const useExpenses = () => {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({ category: '', sort: 'date_desc' });

  const fetchExpenses = async () => {
    try {
      setLoading(true);
      const response = await expenseService.getExpenses(filters.category, filters.sort);
      setExpenses(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load expenses. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchExpenses();
  }, [filters]);

  // Derived state for the "Total" requirement
  const totalAmount = useMemo(() => {
    return expenses.reduce((sum, exp) => sum + parseFloat(exp.amount), 0);
  }, [expenses]);

  return { expenses, loading, error, totalAmount, setFilters, refresh: fetchExpenses };
};