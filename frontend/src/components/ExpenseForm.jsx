import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { expenseService } from '../api/expense';

const ExpenseForm = ({ onRefresh }) => {
  const [formData, setFormData] = useState({
    amount: '', category: '', description: '', expense_date: '',
  });
  const [submitting, setSubmitting] = useState(false);
  // Generate request_id on mount
  const [requestId, setRequestId] = useState(uuidv4());

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await expenseService.createExpense({ ...formData, request_id: requestId });
      // Reset form and generate NEW request ID for next entry
      setFormData({ amount: '', category: '', description: '', expense_date: '' });
      setRequestId(uuidv4());
      onRefresh(); 
    } catch (err) {
      if (err.response && err.response.status === 422) {
        // Handle Pydantic Validation Errors
        const validationErrors = {};
        err.response.data.detail.forEach((error) => {
          // Map the field name (loc[1]) to the error message
          const fieldName = error.loc[1];
          validationErrors[fieldName] = error.msg;
        });
        alert("Validation error: " + JSON.stringify(validationErrors, null, 2));
      } else {
        // Handle Network or 500 Errors
        alert('Something went wrong. Please try again later.');
      }
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-white shadow rounded-lg space-y-4">
      <div className="grid grid-cols-2 gap-4">
        <input 
          type="number" step="0.01" required placeholder="Amount"
          value={formData.amount}
          onChange={(e) => setFormData({...formData, amount: e.target.value})}
          className="border p-2 rounded"
        />
        <select 
          required value={formData.category}
          onChange={(e) => setFormData({...formData, category: e.target.value})}
          className="border p-2 rounded"
        >
          <option value="">Category</option>
          <option value="Food">Food</option>
          <option value="Rent">Rent</option>
          <option value="Sports">Sports</option>
          <option value="Movies">Movies</option>
          <option value="Vehicle">Vehicle</option>
          <option value="Transport">Transport</option>
          <option value="Entertainment">Entertainment</option>
        </select>
      </div>
      <input 
        type="text" placeholder="Description"
        value={formData.description}
        onChange={(e) => setFormData({...formData, description: e.target.value})}
        className="border p-2 w-full rounded"
      />
      <input 
        type="date" required
        value={formData.expense_date}
        onChange={(e) => setFormData({...formData, expense_date: e.target.value})}
        className="border p-2 w-full rounded"
      />
      <button 
        disabled={submitting}
        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
      >
        {submitting ? 'Adding...' : 'Add Expense'}
      </button>
    </form>
  );
};

export default ExpenseForm;