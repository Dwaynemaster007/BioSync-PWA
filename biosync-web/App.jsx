import React, { useState, useEffect, useCallback } from 'react';
import { BookOpen, CheckCircle, Clock, Loader2, PlayCircle } from 'lucide-react';

// Mock API base URL (assuming Django runs locally, e.g., on port 8000)
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Mock User Token and ID based on Canvas environment globals
const USER_ID = typeof __app_id !== 'undefined' ? `User-${__app_id.slice(0, 8)}` : 'mock-user-123';
const MOCK_TOKEN = 'mock-auth-token-xyz'; // In a real scenario, this would be the JWT/Session ID

// --- Mock Data and Fetch Simulation ---

const mockCourses = [
    { id: 1, title: 'Introduction to Fitness Tracking', description: 'Learn the basics of logging your workouts and biometrics.', lesson_count: 3 },
    { id: 2, title: 'Advanced Strength Training Principles', description: 'Dive deep into progressive overload and RPE.', lesson_count: 5 },
    { id: 3, title: 'Mastering Nutrition and Recovery', description: 'Understanding macros and optimizing sleep cycles.', lesson_count: 4 },
];

const mockLessons = [
    { id: 101, course: 1, course_title: 'Intro', title: 'Setting Up Your Goals', order: 1, content_url: '#', is_active: true },
    { id: 102, course: 1, course_title: 'Intro', title: 'Logging Your First Workout', order: 2, content_url: '#', is_active: true },
    { id: 103, course: 1, course_title: 'Intro', title: 'Biometrics Explained', order: 3, content_url: '#', is_active: true },
    { id: 201, course: 2, course_title: 'Adv Str', title: 'The Science of RPE', order: 1, content_url: '#', is_active: true },
    // ... more mock lessons
];

const mockProgressRecords = [
    { id: 1, user_id: USER_ID, lesson: 101, lesson_title: 'Setting Up Your Goals', status: 'COMPLETED', completed_at: new Date().toISOString(), last_viewed_at: new Date().toISOString() },
    { id: 2, user_id: USER_ID, lesson: 102, lesson_title: 'Logging Your First Workout', status: 'IN_PROGRESS', completed_at: null, last_viewed_at: new Date().toISOString() },
];


/**
 * Simulates an API call with latency.
 * In a real application, replace this with a standard fetch call.
 */
const mockFetch = (url, options = {}) => new Promise((resolve, reject) => {
    setTimeout(() => {
        if (url.includes('/courses')) {
            resolve({
                ok: true,
                json: () => Promise.resolve(mockCourses),
            });
        } else if (url.includes('/lessons')) {
            // Usually lessons are fetched by course ID, but we return all mock data here
            resolve({
                ok: true,
                json: () => Promise.resolve(mockLessons),
            });
        } else if (url.includes('/progress')) {
             if (options.method === 'POST') {
                const { lesson, status } = JSON.parse(options.body);
                // Simulate saving/updating a record
                const newRecord = {
                    id: Math.floor(Math.random() * 1000) + 10,
                    user_id: USER_ID,
                    lesson: lesson,
                    lesson_title: mockLessons.find(l => l.id === lesson)?.title || 'Unknown Lesson',
                    status: status,
                    completed_at: status === 'COMPLETED' ? new Date().toISOString() : null,
                    last_viewed_at: new Date().toISOString(),
                };
                mockProgressRecords.push(newRecord); // Add to mock state
                resolve({
                    ok: true,
                    json: () => Promise.resolve(newRecord),
                });
             } else {
                 resolve({
                    ok: true,
                    json: () => Promise.resolve(mockProgressRecords),
                });
             }
        } else {
            reject(new Error('Mock API path not found'));
        }
    }, 800);
});

// --- Components ---

const StatusIcon = ({ status }) => {
    switch (status) {
        case 'COMPLETED':
            return <CheckCircle className="w-5 h-5 text-green-500" />;
        case 'IN_PROGRESS':
            return <Clock className="w-5 h-5 text-yellow-500" />;
        case 'NOT_STARTED':
        default:
            return <PlayCircle className="w-5 h-5 text-gray-400" />;
    }
};

const LessonCard = ({ lesson, progress, onTrack }) => {
    const record = progress.find(p => p.lesson === lesson.id);
    const status = record?.status || 'NOT_STARTED';

    const handleToggleStatus = (newStatus) => {
        onTrack(lesson.id, newStatus);
    };

    return (
        <div className="flex justify-between items-center p-4 bg-white rounded-xl shadow-sm border border-gray-100 mb-2 transition duration-150 ease-in-out hover:shadow-md">
            <div className="flex items-center space-x-3">
                <StatusIcon status={status} />
                <div>
                    <p className="text-sm font-medium text-gray-800">{lesson.order}. {lesson.title}</p>
                    <p className="text-xs text-gray-500">Status: {status.replace('_', ' ')}</p>
                </div>
            </div>
            <div className="space-x-2">
                {status !== 'COMPLETED' && (
                    <button
                        onClick={() => handleToggleStatus('COMPLETED')}
                        className="px-3 py-1 text-xs font-semibold text-white bg-green-600 rounded-lg hover:bg-green-700 transition"
                    >
                        Mark Complete
                    </button>
                )}
                {status !== 'IN_PROGRESS' && status !== 'COMPLETED' && (
                    <button
                        onClick={() => handleToggleStatus('IN_PROGRESS')}
                        className="px-3 py-1 text-xs font-semibold text-white bg-yellow-500 rounded-lg hover:bg-yellow-600 transition"
                    >
                        Start
                    </button>
                )}
            </div>
        </div>
    );
};

const CourseDetail = ({ course, lessons, progress, onTrack }) => {
    const courseLessons = lessons.filter(l => l.course === course.id);

    return (
        <div className="mt-6 p-6 bg-indigo-50 rounded-xl shadow-lg">
            <h3 className="text-2xl font-bold text-indigo-700 mb-2">{course.title}</h3>
            <p className="text-gray-600 mb-4">{course.description}</p>
            <div className="space-y-3">
                <h4 className="text-lg font-semibold text-indigo-700 border-b pb-2">Lessons ({courseLessons.length})</h4>
                {courseLessons.map(lesson => (
                    <LessonCard 
                        key={lesson.id} 
                        lesson={lesson} 
                        progress={progress} 
                        onTrack={onTrack} 
                    />
                ))}
            </div>
        </div>
    );
};

// --- Main Application Component ---

const App = () => {
    const [courses, setCourses] = useState([]);
    const [lessons, setLessons] = useState([]);
    const [progress, setProgress] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedCourse, setSelectedCourse] = useState(null);
    const [error, setError] = useState(null);

    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            // Simulate fetching all required data concurrently
            const [coursesRes, lessonsRes, progressRes] = await Promise.all([
                mockFetch(`${API_BASE_URL}/courses/`),
                mockFetch(`${API_BASE_URL}/lessons/`),
                mockFetch(`${API_BASE_URL}/progress/`),
            ]);

            const [coursesData, lessonsData, progressData] = await Promise.all([
                coursesRes.json(),
                lessonsRes.json(),
                progressRes.json(),
            ]);

            setCourses(coursesData);
            setLessons(lessonsData);
            setProgress(progressData);
        } catch (err) {
            console.error("Error fetching data:", err);
            setError("Failed to load data from API. Check the console for details.");
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    const trackProgress = async (lessonId, newStatus) => {
        try {
            // Update UI optimistically
            const updatedProgress = progress.filter(p => p.lesson !== lessonId);
            const optimisticRecord = {
                lesson: lessonId, 
                status: newStatus, 
                user_id: USER_ID, 
                lesson_title: lessons.find(l => l.id === lessonId)?.title || 'Unknown', 
                last_viewed_at: new Date().toISOString()
            };
            if (newStatus === 'COMPLETED') {
                optimisticRecord.completed_at = new Date().toISOString();
            }
            
            setProgress([...updatedProgress, optimisticRecord]);

            // API Call: Note the /track action is used here
            const response = await mockFetch(`${API_BASE_URL}/progress/track/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Authorization header is needed in a real DRF app
                    'Authorization': `Bearer ${MOCK_TOKEN}`
                },
                body: JSON.stringify({ lesson: lessonId, status: newStatus }),
            });

            if (!response.ok) {
                // If the API call fails, revert the optimistic update (simple fallback for mock)
                fetchData();
                throw new Error("Failed to update progress.");
            }
            // Re-fetch progress to ensure consistency after successful update
            // For this simple mock, we just trust the optimistic update and log
            console.log(`Progress updated for lesson ${lessonId} to ${newStatus}`);
            // In a real app, call fetchData() here or update state with response data
        } catch (err) {
            console.error("Tracking error:", err);
            setError(err.message);
            // Revert state if error occurs
            fetchData();
        }
    };


    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen bg-gray-50">
                <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mr-2" />
                <span className="text-lg text-gray-700">Loading fitness courses...</span>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 p-4 sm:p-8 font-inter">
            <header className="max-w-4xl mx-auto mb-8 text-center">
                <h1 className="text-4xl font-extrabold text-indigo-700">BioSync Progress Tracker</h1>
                <p className="text-gray-600 mt-2">
                    Welcome, <span className="font-mono text-sm bg-gray-200 px-1 rounded">{USER_ID}</span>. 
                    Manage your learning progress on our fitness modules.
                </p>
                {error && (
                    <div className="mt-4 p-3 bg-red-100 text-red-700 border border-red-300 rounded-lg">
                        Error: {error}
                    </div>
                )}
            </header>

            <main className="max-w-4xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Course List / Sidebar */}
                <div className="lg:col-span-1 bg-white p-5 rounded-xl shadow-lg h-fit border border-indigo-100">
                    <h2 className="text-xl font-bold text-gray-700 mb-4 flex items-center">
                        <BookOpen className="w-5 h-5 mr-2 text-indigo-500" />
                        Available Courses
                    </h2>
                    <nav className="space-y-2">
                        {courses.map(course => {
                            // Calculate completion percentage for the summary view
                            const lessonsInCourse = lessons.filter(l => l.course === course.id);
                            const completedCount = lessonsInCourse.filter(l => 
                                progress.some(p => p.lesson === l.id && p.status === 'COMPLETED')
                            ).length;
                            const completion = lessonsInCourse.length > 0 
                                ? Math.round((completedCount / lessonsInCourse.length) * 100) 
                                : 0;
                            
                            const isSelected = selectedCourse && selectedCourse.id === course.id;

                            return (
                                <button
                                    key={course.id}
                                    onClick={() => setSelectedCourse(course)}
                                    className={`w-full text-left p-3 rounded-lg transition duration-150 ${
                                        isSelected 
                                            ? 'bg-indigo-600 text-white shadow-md' 
                                            : 'bg-gray-100 text-gray-700 hover:bg-indigo-100'
                                    }`}
                                >
                                    <p className="font-semibold">{course.title}</p>
                                    <div className="text-xs mt-1 flex justify-between items-center">
                                        <span>{completedCount}/{lessonsInCourse.length} Lessons</span>
                                        <span className={`px-2 py-0.5 rounded-full font-bold ${
                                            isSelected ? 'bg-white text-indigo-600' : 'bg-indigo-200 text-indigo-600'
                                        }`}>
                                            {completion}%
                                        </span>
                                    </div>
                                </button>
                            );
                        })}
                    </nav>
                </div>

                {/* Course Detail / Main Content */}
                <div className="lg:col-span-2">
                    {selectedCourse ? (
                        <CourseDetail 
                            course={selectedCourse} 
                            lessons={lessons} 
                            progress={progress} 
                            onTrack={trackProgress}
                        />
                    ) : (
                        <div className="p-10 bg-white rounded-xl shadow-lg text-center border-2 border-dashed border-indigo-300">
                            <BookOpen className="w-10 h-10 text-indigo-400 mx-auto mb-3" />
                            <p className="text-lg font-medium text-gray-600">Select a course from the left panel to view lessons and track your progress.</p>
                        </div>
                    )}
                </div>
            </main>
        </div>
    );
};

export default App;
