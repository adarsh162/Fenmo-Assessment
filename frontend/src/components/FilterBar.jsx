import React from 'react';

const FilterBar = ({ onFilterChange }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    onFilterChange((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div className="flex gap-4">
      <select 
        name="category"
        onChange={handleChange}
        className="border p-2 rounded text-sm bg-white shadow-sm"
      >
        <option value="">All Categories</option>
        <option value="Food">Food</option>
        <option value="Rent">Rent</option>
        <option value="Transport">Transport</option>
        <option value="Entertainment">Entertainment</option>
        <option value="Sports">Sports</option>
        <option value="Movies">Movies</option>
      </select>

      <select 
        name="sort"
        onChange={handleChange}
        className="border p-2 rounded text-sm bg-white shadow-sm"
      >
        <option value="date_desc">Newest First</option>
        <option value="date_asc">Oldest First</option>
      </select>
    </div>
  );
};

export default FilterBar;