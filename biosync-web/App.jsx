import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { Plus, CheckCircle, Target, Loader, TrendingUp, XCircle, Trash2, Zap } from 'lucide-react';

// --- Configuration and API Utility ---
const API_BASE_URL = 'http://localhost:8000/api/v1'; // Assumes Django runs on localhost:8000
const MOCK_TOKEN = 'mock-auth-token'; // Replace with actual token handling (e.g., from local storage or context)
const headers = {
  'Content-Type': 'application/json',
  // NOTE: For a real DRF app, you'd need the Authorization header:
  // 'Authorization': `Token ${MOCK_TOKEN}` 
  // We omit it for simplicity in this frontend only file, but the structure is ready.
};

/**
 * Utility for API interaction (fetch wrapper with basic error handling)
 * @param {string} endpoint - The API path (e.g., goals)
 * @param {object} options - Fetch options (method, body, headers)
 */
const apiFetch = async (endpoint, options = {}) => {
  const url = `${API_BASE_URL}/${endpoint}`;
  try {
    const response = await fetch(url, { ...options, headers: headers });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ detail: 'Unknown API error' }));
      throw new Error(errorData.detail || `Request failed with status ${response.status}`);
    }
    // Handle 204 No Content
    if (response.status === 204) {
      return null;
    }
    return response.json();
  } catch (error) {
    console.error(`API Error on ${endpoint}:`, error.message);
    throw error;
  }
};

const goalApi = {
  fetchGoals: () => apiFetch('goals/'),
  createGoal: (data) => apiFetch('goals/', {
    method: 'POST',
    body: JSON.stringify(data),
  }),
  updateGoal: (id, data) => apiFetch(`goals/${id}/`, {
    method: 'PUT',
    body: JSON.stringify(data),
  }),
  deleteGoal: (id) => apiFetch(`goals/${id}/`, {
    method: 'DELETE',
  }),
};
// --- End API Utility ---


// --- Components (GoalCard, ProgressBar, NewGoalForm - same as before, but linked to new handlers) ---

/**
 * Utility function to generate a unique ID (kept for new local goals)
 */
const generateId = () => Math.random().toString(36).substring(2, 9);

/**
 * Progress Bar Component
 */
const ProgressBar = ({ current, target, status }) => {
  const percentage = Math.min(100, (current / target) * 100);
  let color = 'bg-indigo-500';
  let indicator = 'bg-indigo-700';

  if (status === 'COMPLETED') { // Changed status keys to match Django model (uppercase)
    color = 'bg-green-500';
    indicator = 'bg-green-700';
  } else if (status === 'STUCK') {
    color = 'bg-red-500';
    indicator = 'bg-red-700';
  }

  return (
    <div className="w-full bg-gray-200 rounded-full h-2.5 shadow-inner">
      <div
        className={`h-2.5 rounded-full transition-all duration-500 ${indicator} ${percentage === 100 ? 'animate-pulse' : ''}`}
        style={{ width: `${percentage}%` }}
        aria-valuenow={current}
        aria-valuemin="0"
        aria-valuemax={target}
      ></div>
    </div>
  );
};

/**
 * Goal Card Component
 */
const GoalCard = ({ goal, onUpdateProgress, onDelete, isUpdating }) => {
  const { id, title, target_value: target, target_unit: unit, current_value: current = 0, status, goal_type: type } = goal; // Mapped keys to Django model field names
  const percentage = Math.round(Math.min(100, (current / target) * 100));

  const statusMap = {
    'IN_PROGRESS': { icon: Loader, text: 'In Progress', color: 'text-indigo-600 bg-indigo-100' },
    'COMPLETED': { icon: CheckCircle, text: 'Completed', color: 'text-green-600 bg-green-100' },
    'STUCK': { icon: XCircle, text: 'Stuck', color: 'text-red-600 bg-red-100' },
    'NOT_STARTED': { icon: Zap, text: 'Not Started', color: 'text-gray-600 bg-gray-100' },
  };

  const currentStatus = status || 'NOT_STARTED'; // Default to NOT_STARTED if status is null/undefined
  const StatusIcon = statusMap[currentStatus]?.icon || Zap;

  const handleProgressChange = (increment) => {
    let newCurrent = current + increment;
    if (newCurrent < 0) newCurrent = 0;

    let newStatus = currentStatus;
    if (newCurrent >= target) {
      newCurrent = target;
      newStatus = 'COMPLETED';
    } else if (newCurrent > 0) {
      newStatus = 'IN_PROGRESS';
    } else if (newCurrent === 0) {
      newStatus = 'NOT_STARTED';
    }

    // Call the parent handler which now calls the API
    onUpdateProgress(id, newCurrent, newStatus);
  };

  const disabled = isUpdating === id;

  return (
    <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100 flex flex-col justify-between">
      {disabled && (
        <div className="absolute inset-0 bg-white bg-opacity-80 flex items-center justify-center z-10 rounded-xl">
          <Loader className="w-6 h-6 animate-spin text-indigo-600" />
        </div>
      )}
      <div>
        <div className={`text-sm font-semibold mb-2 inline-flex items-center px-3 py-1 rounded-full ${statusMap[currentStatus]?.color || 'bg-gray-100 text-gray-600'}`}>
          <StatusIcon className="w-4 h-4 mr-1" />
          {statusMap[currentStatus]?.text || 'Loading'}
        </div>
        <h3 className="text-xl font-bold text-gray-800 mb-3">{title}</h3>
        <p className="text-sm text-indigo-500 font-medium mb-4">{type}</p>
      </div>

      <div>
        <div className="flex justify-between items-end mb-1">
          <span className="text-2xl font-extrabold text-gray-900">
            {current} <span className="text-base font-medium text-gray-500">/{target} {unit}</span>
          </span>
          <span className="text-lg font-bold text-gray-700">{percentage}%</span>
        </div>

        <ProgressBar current={current} target={target} status={currentStatus} />

        <div className="mt-5 flex space-x-3">
          <button
            onClick={() => handleProgressChange(unit === '%' ? 5 : 1)}
            className="flex-1 px-4 py-2 bg-indigo-600 text-white text-sm font-semibold rounded-lg hover:bg-indigo-700 transition-colors shadow-md hover:shadow-lg disabled:opacity-50"
            disabled={percentage >= 100 || disabled}
          >
            + {unit === '%' ? '5' : '1'} {unit}
          </button>
          <button
            onClick={() => handleProgressChange(unit === '%' ? -5 : -1)}
            className="flex-1 px-4 py-2 bg-gray-200 text-gray-800 text-sm font-semibold rounded-lg hover:bg-gray-300 transition-colors shadow-md hover:shadow-lg disabled:opacity-50"
            disabled={current <= 0 || disabled}
          >
            - {unit === '%' ? '5' : '1'} {unit}
          </button>
          <button
            onClick={() => onDelete(id)}
            className="p-2 bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors disabled:opacity-50"
            aria-label={`Delete goal: ${title}`}
            disabled={disabled}
          >
            <Trash2 className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

/**
 * New Goal Form Component
 */
const NewGoalForm = ({ onAddGoal, onClose }) => {
  const [title, setTitle] = useState('');
  const [target, setTarget] = useState('');
  const [unit, setUnit] = useState('Km');
  const [type, setType] = useState('Fitness');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title.trim() || !target || Number(target) <= 0 || !unit.trim()) {
      setError('Please provide a title, a positive target value, and a unit.');
      return;
    }

    const newGoalData = {
      title: title.trim(),
      target_value: Number(target),
      target_unit: unit.trim(),
      goal_type: type,
      // Default values required by the Django model
      description: `New goal: ${title}`,
      start_date: new Date().toISOString().split('T')[0], // YYYY-MM-DD format
      target_date: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0], // 30 days from now
      status: 'NOT_STARTED',
      current_value: 0, // This is a new field we assume the backend model now supports
    };

    setIsLoading(true);
    setError('');
    try {
      await onAddGoal(newGoalData);
      onClose();
    } catch (err) {
      setError(`Failed to create goal: ${err.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-2xl border border-indigo-200">
      <h3 className="text-2xl font-bold text-indigo-800 mb-6">Create New Goal</h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        {error && <p className="text-red-500 text-sm">{error}</p>}
        <div>
          <label htmlFor="title" className="block text-sm font-medium text-gray-700">Goal Title</label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g., Run 10K distance"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            required
            disabled={isLoading}
          />
        </div>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label htmlFor="target" className="block text-sm font-medium text-gray-700">Target Value</label>
            <input
              id="target"
              type="number"
              value={target}
              onChange={(e) => setTarget(e.target.value)}
              placeholder="e.g., 10"
              min="1"
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              required
              disabled={isLoading}
            />
          </div>
          <div>
            <label htmlFor="unit" className="block text-sm font-medium text-gray-700">Unit</label>
            <input
              id="unit"
              type="text"
              value={unit}
              onChange={(e) => setUnit(e.target.value)}
              placeholder="e.g., Km, Books, Hours"
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              required
              disabled={isLoading}
            />
          </div>
        </div>
        <div>
          <label htmlFor="type" className="block text-sm font-medium text-gray-700">Goal Type</label>
          <select
            id="type"
            value={type}
            onChange={(e) => setType(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 bg-white rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            disabled={isLoading}
          >
            <option>Fitness</option>
            <option>Learning</option>
            <option>Health</option>
            <option>Work</option>
            <option>Finance</option>
            <option>Other</option>
          </select>
        </div>
        <div className="flex justify-end space-x-3 pt-2">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-sm font-semibold text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
            disabled={isLoading}
          >
            Cancel
          </button>
          <button
            type="submit"
            className="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors shadow-md flex items-center"
            disabled={isLoading}
          >
            {isLoading && <Loader className="w-4 h-4 animate-spin mr-2" />}
            {isLoading ? 'Adding...' : 'Add Goal'}
          </button>
        </div>
      </form>
    </div>
  );
};


// --- Main Application Component ---

const App = () => {
  const [goals, setGoals] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [error, setError] = useState(null);
  const [isUpdating, setIsUpdating] = useState(null); // Tracks the ID of the goal currently being updated

  const fetchGoals = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await goalApi.fetchGoals();
      setGoals(data || []); // API response is expected to be an array of goals
    } catch (err) {
      setError(`Failed to fetch goals: ${err.message}`);
      setGoals([]);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    // Initial data fetch
    fetchGoals();
  }, [fetchGoals]);


  // --- Statistics ---
  const stats = useMemo(() => {
    const totalGoals = goals.length;
    const completedGoals = goals.filter(g => g.status === 'COMPLETED').length;
    const stuckGoals = goals.filter(g => g.status === 'STUCK').length;

    const overallProgress = goals.reduce((acc, goal) => {
      const current = goal.current_value || 0;
      const target = goal.target_value || 1;
      const percentage = Math.min(100, (current / target) * 100);
      return acc + percentage;
    }, 0) / (totalGoals || 1);

    return {
      totalGoals,
      completedGoals,
      stuckGoals,
      overallProgress: overallProgress.toFixed(1),
    };
  }, [goals]);


  // --- Handlers ---
  const handleAddGoal = async (newGoalData) => {
    try {
      const createdGoal = await goalApi.createGoal(newGoalData);
      setGoals(prevGoals => [createdGoal, ...prevGoals]);
      return createdGoal;
    } catch (err) {
      setError(`Failed to add goal: ${err.message}`);
      throw err;
    }
  };

  const handleUpdateProgress = async (id, newCurrent, newStatus) => {
    setIsUpdating(id);
    setError(null);
    try {
      const updateData = {
        current_value: newCurrent,
        status: newStatus,
        // The PUT endpoint usually requires all required fields, we send back the rest of the existing goal data
        // For a PATCH endpoint, we would only send current_value and status. We assume PUT is required here.
        ...goals.find(g => g.id === id)
      };
      
      const updatedGoal = await goalApi.updateGoal(id, updateData);
      
      // Update local state with the confirmed data from the server
      setGoals(prevGoals =>
        prevGoals.map(goal =>
          goal.id === id ? updatedGoal : goal
        )
      );
    } catch (err) {
      setError(`Failed to update progress for goal ${id}: ${err.message}`);
      // Re-fetch to revert local changes if API fails
      fetchGoals();
    } finally {
      setIsUpdating(null);
    }
  };

  const handleDeleteGoal = async (id) => {
    if (window.confirm("Are you sure you want to delete this goal?")) {
        setIsUpdating(id);
        setError(null);
        try {
            await goalApi.deleteGoal(id);
            setGoals(prevGoals => prevGoals.filter(goal => goal.id !== id));
        } catch (err) {
            setError(`Failed to delete goal: ${err.message}`);
        } finally {
            setIsUpdating(null);
        }
    }
  }

  // Helper for rendering stat cards
  const StatCard = ({ title, value, icon: Icon, color }) => (
    <div className={`p-5 rounded-xl shadow-md ${color} text-white flex items-center justify-between transition-transform duration-300 hover:scale-[1.02]`}>
      <div>
        <p className="text-lg font-semibold">{title}</p>
        <p className="text-3xl font-extrabold mt-1">{value}</p>
      </div>
      <Icon className="w-8 h-8 opacity-70" />
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <script src="https://cdn.tailwindcss.com"></script>
      <style>{`
        /* Custom scrollbar for better aesthetics */
        ::-webkit-scrollbar {
          width: 8px;
        }
        ::-webkit-scrollbar-track {
          background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
          background: #888;
          border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
          background: #555;
        }
      `}</style>
      <header className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <h1 className="text-3xl font-extrabold text-indigo-700 flex items-center">
            <TrendingUp className="w-8 h-8 mr-2" />
            BioSync Progress Tracker
          </h1>
          <button
            onClick={() => setIsFormVisible(true)}
            className="px-4 py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-lg hover:bg-indigo-700 transition-colors flex items-center space-x-1"
          >
            <Plus className="w-5 h-5" />
            <span className="hidden sm:inline">Add New Goal</span>
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {error && (
            <div className="mb-6 p-4 bg-red-100 border border-red-300 text-red-700 rounded-xl font-medium flex items-center">
                <XCircle className="w-5 h-5 mr-2" />
                {error}
            </div>
        )}
        
        {/* Statistics Section */}
        <section className="mb-10">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Dashboard Overview</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <StatCard
              title="Overall Progress"
              value={`${stats.overallProgress}%`}
              icon={Target}
              color="bg-gradient-to-br from-indigo-500 to-purple-600"
            />
            <StatCard
              title="Total Goals"
              value={stats.totalGoals}
              icon={CheckCircle}
              color="bg-gradient-to-br from-blue-500 to-indigo-600"
            />
            <StatCard
              title="Completed Goals"
              value={stats.completedGoals}
              icon={CheckCircle}
              color="bg-gradient-to-br from-green-500 to-teal-600"
            />
            <StatCard
              title="Stuck Goals"
              value={stats.stuckGoals}
              icon={XCircle}
              color="bg-gradient-to-br from-red-500 to-pink-600"
            />
          </div>
        </section>

        {/* Goals List Section */}
        <section>
          <h2 className="text-2xl font-bold text-gray-800 mb-6">My Current Goals ({stats.totalGoals})</h2>
          {isLoading && goals.length === 0 ? (
            <div className="flex items-center justify-center p-12 bg-white rounded-xl shadow-inner">
                <Loader className="w-6 h-6 animate-spin text-indigo-600 mr-3" />
                <span className="text-lg text-gray-600">Loading goals from API...</span>
            </div>
          ) : goals.length === 0 ? (
            <div className="text-center p-12 bg-white rounded-xl shadow-inner border border-dashed border-gray-300">
              <p className="text-gray-500 text-lg">You have no active goals. Click "Add New Goal" to start tracking!</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {goals.map(goal => (
                <GoalCard
                  key={goal.id}
                  goal={goal}
                  onUpdateProgress={handleUpdateProgress}
                  onDelete={handleDeleteGoal}
                  isUpdating={isUpdating}
                />
              ))}
            </div>
          )}
        </section>
      </main>

      {/* Modal for New Goal Form */}
      {isFormVisible && (
        <div className="fixed inset-0 bg-gray-900 bg-opacity-70 flex items-center justify-center p-4 z-50">
          <div className="max-w-lg w-full transform transition-all duration-300 scale-100 opacity-100">
            <NewGoalForm
              onAddGoal={handleAddGoal}
              onClose={() => setIsFormVisible(false)}
            />
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 text-center text-gray-500 text-sm">
          &copy; {new Date().getFullYear()} BioSync. Progress tracking dashboard.
      </footer>
    </div>
  );
};

export default App;
