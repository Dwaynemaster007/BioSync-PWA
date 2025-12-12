import React, { useState, useMemo, useEffect } from 'react';
import { Plus, CheckCircle, Target, Loader, TrendingUp, XCircle, Trash2 } from 'lucide-react';

/**
 * Utility function to generate a unique ID
 */
const generateId = () => Math.random().toString(36).substring(2, 9);

// Initial set of sample goals for demonstration
const initialGoals = [
  { id: generateId(), name: "Complete Weekly Cardio Goal", current: 45, target: 60, unit: "Mins", status: 'in-progress', type: 'Fitness' },
  { id: generateId(), name: "Read 'Deep Work' Book", current: 150, target: 300, unit: "Pages", status: 'in-progress', type: 'Learning' },
  { id: generateId(), name: "Drink 8 Glasses of Water Daily (Avg)", current: 85, target: 100, unit: "%", status: 'completed', type: 'Health' },
  { id: generateId(), name: "Finish Project Alpha Report", current: 75, target: 100, unit: "%", status: 'stuck', type: 'Work' },
];

/**
 * Progress Bar Component
 */
const ProgressBar = ({ current, target, status }) => {
  const percentage = Math.min(100, (current / target) * 100);
  let color = 'bg-indigo-500';
  let indicator = 'bg-indigo-700';

  if (status === 'completed') {
    color = 'bg-green-500';
    indicator = 'bg-green-700';
  } else if (status === 'stuck') {
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
const GoalCard = ({ goal, onUpdateProgress, onDelete }) => {
  const { id, name, current, target, unit, status, type } = goal;
  const percentage = Math.round(Math.min(100, (current / target) * 100));

  const statusMap = {
    'in-progress': { icon: Loader, text: 'In Progress', color: 'text-indigo-600 bg-indigo-100' },
    'completed': { icon: CheckCircle, text: 'Completed', color: 'text-green-600 bg-green-100' },
    'stuck': { icon: XCircle, text: 'Stuck', color: 'text-red-600 bg-red-100' },
  };

  const StatusIcon = statusMap[status].icon;

  const handleProgressChange = (increment) => {
    let newCurrent = current + increment;
    if (newCurrent < 0) newCurrent = 0;

    let newStatus = status;
    if (newCurrent >= target) {
      newCurrent = target;
      newStatus = 'completed';
    } else if (newCurrent > 0 && newStatus === 'completed') {
        newStatus = 'in-progress';
    } else if (newCurrent > 0 && newStatus === 'stuck') {
        newStatus = 'in-progress';
    } else if (newCurrent === 0) {
        newStatus = 'stuck';
    }


    onUpdateProgress(id, newCurrent, newStatus);
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100 flex flex-col justify-between">
      <div>
        <div className={`text-sm font-semibold mb-2 inline-flex items-center px-3 py-1 rounded-full ${statusMap[status].color}`}>
          <StatusIcon className="w-4 h-4 mr-1" />
          {statusMap[status].text}
        </div>
        <h3 className="text-xl font-bold text-gray-800 mb-3">{name}</h3>
        <p className="text-sm text-indigo-500 font-medium mb-4">{type}</p>
      </div>

      <div>
        <div className="flex justify-between items-end mb-1">
          <span className="text-2xl font-extrabold text-gray-900">
            {current} <span className="text-base font-medium text-gray-500">/{target} {unit}</span>
          </span>
          <span className="text-lg font-bold text-gray-700">{percentage}%</span>
        </div>

        <ProgressBar current={current} target={target} status={status} />

        <div className="mt-5 flex space-x-3">
          <button
            onClick={() => handleProgressChange(unit === '%' ? 5 : 1)}
            className="flex-1 px-4 py-2 bg-indigo-600 text-white text-sm font-semibold rounded-lg hover:bg-indigo-700 transition-colors shadow-md hover:shadow-lg disabled:opacity-50"
            disabled={percentage >= 100}
          >
            + {unit === '%' ? '5' : '1'} {unit}
          </button>
          <button
            onClick={() => handleProgressChange(unit === '%' ? -5 : -1)}
            className="flex-1 px-4 py-2 bg-gray-200 text-gray-800 text-sm font-semibold rounded-lg hover:bg-gray-300 transition-colors shadow-md hover:shadow-lg"
          >
            - {unit === '%' ? '5' : '1'} {unit}
          </button>
          <button
            onClick={() => onDelete(id)}
            className="p-2 bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors"
            aria-label={`Delete goal: ${name}`}
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
  const [name, setName] = useState('');
  const [target, setTarget] = useState('');
  const [unit, setUnit] = useState('Unit');
  const [type, setType] = useState('Fitness');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name.trim() || !target || target <= 0) {
      setError('Please provide a name and a positive target value.');
      return;
    }

    const newGoal = {
      id: generateId(),
      name: name.trim(),
      current: 0,
      target: Number(target),
      unit: unit,
      status: 'stuck', // Starts at 0, so 'stuck' or 'in-progress' can be used. Using 'stuck' for 0 progress.
      type: type,
    };

    onAddGoal(newGoal);
    onClose();
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-2xl border border-indigo-200">
      <h3 className="text-2xl font-bold text-indigo-800 mb-6">Create New Goal</h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        {error && <p className="text-red-500 text-sm">{error}</p>}
        <div>
          <label htmlFor="name" className="block text-sm font-medium text-gray-700">Goal Name</label>
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g., Run 10K distance"
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            required
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
          >
            Cancel
          </button>
          <button
            type="submit"
            className="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors shadow-md"
          >
            Add Goal
          </button>
        </div>
      </form>
    </div>
  );
};

/**
 * Main Application Component
 */
const App = () => {
  const [goals, setGoals] = useState(initialGoals);
  const [isFormVisible, setIsFormVisible] = useState(false);

  // --- Statistics ---
  const stats = useMemo(() => {
    const totalGoals = goals.length;
    const completedGoals = goals.filter(g => g.status === 'completed').length;
    const stuckGoals = goals.filter(g => g.status === 'stuck').length;

    const overallProgress = goals.reduce((acc, goal) => {
      const percentage = Math.min(100, (goal.current / goal.target) * 100);
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
  const handleAddGoal = (newGoal) => {
    setGoals(prevGoals => [newGoal, ...prevGoals]);
  };

  const handleUpdateProgress = (id, newCurrent, newStatus) => {
    setGoals(prevGoals =>
      prevGoals.map(goal =>
        goal.id === id ? { ...goal, current: newCurrent, status: newStatus } : goal
      )
    );
  };

  const handleDeleteGoal = (id) => {
    setGoals(prevGoals => prevGoals.filter(goal => goal.id !== id));
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
          {goals.length === 0 ? (
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
