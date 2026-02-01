import { useExpenses } from './hooks/useExpenses';
import ExpenseForm from './components/ExpenseForm';
import ExpenseList from './components/ExpenseList';
import FilterBar from './components/FilterBar';
import './App.css'
import './index.css'

function App() {
  const { expenses, loading, error, totalAmount, setFilters, refresh } = useExpenses();

  return (
    <div className="min-h-screen bg-gray-100 py-10 px-4">
      <div className="max-w-5xl mx-auto">
        {/* Header with Live Total */}
        <header className="mb-8 flex flex-col md:flex-row md:items-end justify-between gap-4">
          <div>
            <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">SpendWise</h1>
            <p className="text-gray-500">Personal Expense Tracker</p>
          </div>
          <div className="bg-white p-4 rounded-xl shadow-sm border-l-4 border-green-500 min-w-[200px]">
            <span className="text-xs font-bold text-gray-400 uppercase block">Total Expenses</span>
            <span className="text-3xl font-mono font-bold text-gray-800">
              ₹{totalAmount.toLocaleString(undefined, { minimumFractionDigits: 2 })}
            </span>
          </div>
        </header>

        <main className="grid lg:grid-cols-12 gap-8">
          {/* Form Section */}
          <div className="lg:col-span-4">
            <h2 className="text-lg font-bold text-gray-700 mb-4">Record New Expense</h2>
            <ExpenseForm onRefresh={refresh} />
          </div>

          {/* Table Section */}
          <div className="lg:col-span-8">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-lg font-bold text-gray-700">Transaction History</h2>
              <FilterBar onFilterChange={setFilters} />
            </div>

            {error && (
              <div className="mb-4 p-4 bg-red-50 border-l-4 border-red-500 text-red-700 text-sm">
                {error}
              </div>
            )}

            <ExpenseList expenses={expenses} isLoading={loading} />
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;