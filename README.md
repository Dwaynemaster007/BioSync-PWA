# 💪 BioSync - Full-Stack Fitness Tracking Platform

A comprehensive, cross-platform fitness tracking application that empowers users to log workouts, monitor progress, and achieve their fitness goals. BioSync delivers seamless fitness experiences across Web, Mobile (iOS/Android), and Progressive Web App platforms, powered by a robust Django REST API and integrated with the WGER Exercise Database.

[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14+-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![React Native](https://img.shields.io/badge/React_Native-0.76+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactnative.dev/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Redux](https://img.shields.io/badge/Redux-5.0+-764ABC?style=for-the-badge&logo=redux&logoColor=white)](https://redux.js.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-3.4+-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

<div align="center">

### 🏋️ Track Every Rep, Celebrate Every Milestone 🏋️

*Your Personal Fitness Journey, Synchronized Across All Devices*

[Overview](#-project-overview) • [Features](#-key-features) • [Tech Stack](#-technology-stack) • [API](#-api-documentation) • [Getting Started](#-getting-started)

</div>

---

## 📋 Project Overview

**BioSync** is a modern, full-stack fitness tracking platform developed as part of the **ALX Professional Development Program**. This capstone project demonstrates mastery of both frontend and backend engineering, integrating external APIs, building responsive user interfaces, and implementing secure, scalable backend systems.

### 🎯 Project Goals

**Frontend Excellence:**
- Build intuitive workout logging interfaces
- Implement real-time progress tracking with charts
- Integrate WGER Exercise API for comprehensive exercise database
- Create responsive designs across Web, Mobile, and PWA
- Optimize user experience with smooth navigation and interactions
- Implement offline capabilities with PWA features

**Backend Mastery:**
- Design RESTful APIs for fitness activity management
- Implement secure JWT authentication
- Build CRUD operations for workouts and activities
- Optimize database queries for performance
- Deploy production-ready API infrastructure
- Document APIs with Swagger/OpenAPI

### 🏆 Why BioSync?

This project demonstrates:
- ✅ **Full-Stack Proficiency** - Frontend to backend expertise
- ✅ **Cross-Platform Development** - Web, Mobile (iOS/Android), PWA
- ✅ **API Integration** - External API consumption (WGER)
- ✅ **Data Visualization** - Charts and progress metrics
- ✅ **Modern Tech Stack** - Industry-standard technologies
- ✅ **Best Practices** - Clean code, testing, documentation
- ✅ **Real-World Application** - Solving actual fitness tracking needs

---

## 🚀 Key Features

### 🏃 Workout Logging

**Comprehensive Activity Tracking**
```typescript
// Log workouts with detailed information
- Exercise selection from WGER database
- Sets, reps, and weight tracking
- Duration and distance logging
- Calories burned calculation
- Timestamp for each workout
- Activity type categorization (Running, Cycling, Weightlifting, etc.)
- Notes and comments for workouts
```

**Activity Types:**
- 🏃 Running & Cardio
- 🚴 Cycling
- 🏋️ Weightlifting & Strength Training
- 🧘 Yoga & Flexibility
- 🏊 Swimming
- 🥊 Martial Arts & Boxing
- ⚽ Sports Activities
- 🚶 Walking & Hiking

**Workout Entry Features:**
- ✅ Quick workout logging
- ✅ Exercise search and filtering
- ✅ Pre-filled templates for common workouts
- ✅ Rest timer between sets
- ✅ Form validation and error handling
- ✅ Auto-save drafts (PWA)
- ✅ Duplicate previous workouts

### 📊 Progress Tracking & Analytics

**Visual Progress Metrics**
```javascript
// Comprehensive fitness analytics
- Total weight lifted over time
- Average reps per exercise
- Workout frequency (weekly/monthly)
- Calories burned trends
- Distance covered (running/cycling)
- Personal records (PRs)
- Body measurements tracking
- Goal completion percentage
```

**Charts & Visualizations:**
- 📈 Line charts for progress trends
- 📊 Bar charts for workout comparisons
- 🥧 Pie charts for activity distribution
- 📉 Calendar heatmaps for consistency
- 🎯 Goal progress indicators

**Progress Features:**
- ✅ Weekly/Monthly/Yearly views
- ✅ Compare periods side-by-side
- ✅ Export data as CSV/PDF
- ✅ Share achievements on social media
- ✅ Personal records highlighting
- ✅ Achievement badges and milestones

### 📜 Workout History

**Comprehensive Activity Log**
```typescript
// View complete workout history
- Chronological workout listing
- Detailed exercise breakdown
- Sets, reps, weight for each exercise
- Duration and calories burned
- Date and time stamps
- Filter by date range
- Filter by activity type
- Search by exercise name
```

**History Features:**
- ✅ Infinite scroll pagination
- ✅ Quick filters (This Week, This Month, Custom)
- ✅ Edit past workouts
- ✅ Delete unwanted entries
- ✅ Duplicate workouts for quick logging
- ✅ Export history to CSV
- ✅ Print workout logs

### 💪 WGER Exercise Database Integration

**Comprehensive Exercise Library**
```javascript
// WGER API Integration
Endpoints:
- GET /api/v2/exercise/ - List all exercises
- GET /api/v2/exerciseinfo/:id/ - Exercise details
- GET /api/v2/exercise/?muscle=1 - Filter by muscle group

Features:
- 1000+ exercises
- Detailed descriptions
- Muscle groups targeted
- Equipment required
- Difficulty levels
- Exercise images/videos
- Proper form instructions
```

**Exercise Search:**
- 🔍 Search by name
- 🔍 Filter by muscle group (Chest, Back, Legs, Arms, etc.)
- 🔍 Filter by equipment (Barbell, Dumbbell, Bodyweight, etc.)
- 🔍 Filter by difficulty (Beginner, Intermediate, Advanced)

**Exercise Details:**
- ✅ Step-by-step instructions
- ✅ Muscle groups highlighted
- ✅ Alternative exercises
- ✅ Exercise variations
- ✅ Tips and warnings
- ✅ Save favorites

### 👤 User Authentication & Profiles

**Secure Authentication System**
```python
# JWT-based authentication
- User registration with email verification
- Login/logout functionality
- Password reset via email
- Token refresh mechanism
- Protected routes and endpoints
- Session management
```

**User Profiles:**
- Personal information management
- Profile picture upload
- Bio and fitness goals
- Body measurements tracking
- Fitness level (Beginner, Intermediate, Advanced)
- Preferred units (Metric/Imperial)
- Privacy settings

**Profile Features:**
- ✅ Public/Private profile toggle
- ✅ Activity visibility settings
- ✅ Social connections (follow/unfollow)
- ✅ Achievement badges display
- ✅ Custom profile themes

### 🎯 Goal Setting & Tracking

**Smart Goal Management**
```typescript
// Set and track fitness goals
Goal Types:
- Weight loss/gain goals
- Distance goals (e.g., run 100 km/month)
- Strength goals (e.g., bench press 100 kg)
- Frequency goals (e.g., workout 4x/week)
- Consistency goals (e.g., 30-day streak)

Features:
- Progress tracking with percentage
- Goal deadlines and reminders
- Goal achievement notifications
- Historical goal performance
- Motivational milestones
```

**Goal Features:**
- ✅ Multiple concurrent goals
- ✅ Weekly/Monthly/Yearly goals
- ✅ Progress notifications
- ✅ Goal completion badges
- ✅ Recommended goals based on activity
- ✅ Share goals with friends

### 📅 Workout Plans

**Custom Workout Routines**
```typescript
// Create and follow structured plans
Plan Types:
- Strength training programs
- Cardio programs
- Hybrid training plans
- Weekly routines
- Monthly challenges

Features:
- Day-by-day workout schedules
- Exercise templates
- Rest day planning
- Progressive overload tracking
- Plan sharing with community
```

**Workout Plan Features:**
- ✅ Pre-built plans (Beginner, Intermediate, Advanced)
- ✅ Custom plan creation
- ✅ Plan templates library
- ✅ Exercise substitutions
- ✅ Track plan progress
- ✅ Print weekly schedule

### 🍎 Diet & Nutrition Tracking

**Comprehensive Nutrition Management**
```typescript
// Track meals and nutrition
Features:
- Meal logging (Breakfast, Lunch, Dinner, Snacks)
- Calorie tracking
- Macronutrient breakdown (Protein, Carbs, Fats)
- Water intake tracking
- Food database integration
- Barcode scanning (mobile)
- Recipe builder
```

**Nutrition Features:**
- ✅ Daily calorie goals
- ✅ Macro targets (protein, carbs, fats)
- ✅ Meal planning and prep
- ✅ Nutrition charts and trends
- ✅ Food diary with photos
- ✅ Integration with workout data

### 🏆 Leaderboards & Community

**Social Fitness Features**
```typescript
// Compete and connect with others
Leaderboard Types:
- Most workouts logged
- Total distance covered
- Total weight lifted
- Total calories burned
- Longest workout streaks
- Goal completions

Community Features:
- Follow other users
- Like and comment on activities
- Share workout achievements
- Join fitness challenges
- Community workout plans
```

**Social Features:**
- ✅ Friends and followers system
- ✅ Activity feed
- ✅ Motivation and support
- ✅ Group challenges
- ✅ Share on social media
- ✅ Private messaging (future)

### 📱 Progressive Web App (PWA)

**Offline-First Capabilities**
```javascript
// PWA features for enhanced experience
- Add to home screen
- Offline workout logging
- Service worker caching
- Background sync
- Push notifications for:
  - Workout reminders
  - Goal achievements
  - Friend activities
  - Streak maintenance
- Fast loading with caching
- App-like experience
```

**PWA Features:**
- ✅ Works offline
- ✅ Install on any device
- ✅ Push notifications
- ✅ Background updates
- ✅ Responsive on all screens
- ✅ Native app feel

### 🔔 Notifications & Reminders

**Stay Motivated with Alerts**
```typescript
// Smart notification system
Notification Types:
- Workout reminders (customizable times)
- Goal progress updates
- Achievement unlocked alerts
- Streak maintenance reminders
- Friend activity notifications
- Challenge invitations
- New exercise recommendations

Delivery Methods:
- In-app notifications
- Push notifications (PWA/Mobile)
- Email notifications
- SMS notifications (future)
```

### 🌙 Dark Mode

**Enhanced User Experience**
```css
// Beautiful dark mode design
- Automatic theme detection
- Manual toggle switch
- Persistent preference
- Optimized for OLED screens
- Reduced eye strain
- Battery saving on mobile
```

### 📤 Social Sharing

**Share Your Achievements**
```typescript
// Share progress and milestones
Share Options:
- Workout summaries
- Progress charts
- Achievement badges
- Personal records
- Goal completions
- Workout plans

Platforms:
- Twitter/X
- Facebook
- Instagram (stories)
- WhatsApp
- Copy link
- Export as image
```

### 🔗 Wearables Integration (Future)

**Connect Your Devices**
```typescript
// Integration with fitness wearables
Supported Devices:
- Apple Watch
- Fitbit
- Garmin
- Samsung Galaxy Watch
- Google Fit
- Strava

Features:
- Auto-sync workouts
- Heart rate data
- Sleep tracking
- Step counting
- Calorie burn tracking
```

---

## 🛠️ Technology Stack

### Frontend Technologies

#### Web Application (Next.js)
```json
{
  "framework": "Next.js 14+",
  "language": "TypeScript 5.0+",
  "styling": "TailwindCSS 3.4+",
  "state": "Redux Toolkit / Zustand",
  "routing": "Next.js App Router",
  "api": "Axios",
  "charts": "Recharts / Chart.js",
  "forms": "React Hook Form",
  "validation": "Zod / Yup",
  "icons": "Lucide Icons / Heroicons"
}
```

**Key Features:**
- Server-Side Rendering (SSR)
- Static Site Generation (SSG)
- API Routes for Backend-for-Frontend (BFF)
- Image optimization
- SEO optimization
- Fast refresh development

#### Mobile Application (React Native)
```json
{
  "framework": "React Native 0.76+",
  "platform": "Expo 52+",
  "language": "TypeScript 5.0+",
  "styling": "NativeWind (Tailwind for RN)",
  "state": "Redux Toolkit / Zustand",
  "navigation": "Expo Router",
  "storage": "AsyncStorage",
  "icons": "@expo/vector-icons",
  "charts": "Victory Native",
  "camera": "Expo Camera"
}
```

**Key Features:**
- Cross-platform (iOS & Android)
- Native performance
- Push notifications
- Camera for meal photos
- Biometric authentication
- Offline support

#### Progressive Web App
```json
{
  "base": "Next.js + PWA",
  "serviceWorker": "Workbox",
  "manifest": "Web App Manifest",
  "caching": "Cache API",
  "notifications": "Push API",
  "offline": "IndexedDB",
  "sync": "Background Sync API"
}
```

**PWA Features:**
- Offline functionality
- Installable on devices
- Push notifications
- Background sync
- App-like experience

### Backend Technologies

#### Django REST Framework
```python
{
  "framework": "Django 4.2+",
  "api": "Django REST Framework 3.14+",
  "database": "PostgreSQL 15+",
  "auth": "JWT (djangorestframework-simplejwt)",
  "cors": "django-cors-headers",
  "docs": "drf-yasg (Swagger/OpenAPI)",
  "storage": "Django Storage",
  "email": "Django Email Backend",
  "filtering": "django-filter",
  "pagination": "DRF Pagination"
}
```

**Key Features:**
- RESTful API architecture
- JWT authentication
- Database optimization
- Query optimization
- API rate limiting
- CORS configuration
- Comprehensive API documentation

#### Database Design
```sql
-- Core Models
- Users (authentication, profiles)
- Activities (workout logs)
- Exercises (WGER integration cache)
- WorkoutPlans (custom routines)
- Goals (fitness objectives)
- Meals (nutrition tracking)
- Achievements (badges, milestones)
- SocialConnections (followers, friends)
```

### External APIs

#### WGER Workout Manager API
```javascript
// Free, open-source exercise database
Base URL: https://wger.de/api/v2/

Endpoints:
- GET /exercise/ - List all exercises
- GET /exercise/:id/ - Exercise details
- GET /exerciseinfo/:id/ - Detailed exercise info
- GET /exercise/?muscle=:id - Filter by muscle
- GET /muscle/ - List muscle groups
- GET /equipment/ - List equipment types
- GET /category/ - Exercise categories

Features:
- 1000+ exercises
- No API key required
- Multiple languages
- Images and descriptions
- Muscle group mapping
- Equipment information
```

### DevOps & Deployment

```yaml
Development:
  - Docker & Docker Compose
  - Git version control
  - GitHub for collaboration
  - VS Code / PyCharm

Testing:
  - Jest (Frontend unit tests)
  - React Testing Library
  - Pytest (Backend tests)
  - Django TestCase
  - Postman (API testing)

Deployment:
  - Frontend: Vercel / Netlify
  - Backend: Heroku / PythonAnywhere / Railway
  - Database: Managed PostgreSQL
  - CI/CD: GitHub Actions
  - Monitoring: Sentry (future)
```

---

## 🏗️ System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend Layer                           │
├──────────────┬──────────────────┬──────────────────────────┤
│   Web App    │   Mobile App     │         PWA              │
│  (Next.js)   │ (React Native)   │  (Next.js + SW)          │
│              │                  │                           │
│  - SSR/SSG   │  - iOS/Android   │  - Offline Mode          │
│  - Charts    │  - Native Feel   │  - Installable           │
│  - Desktop   │  - Camera        │  - Push Notif            │
└──────────────┴──────────────────┴──────────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   BioSync API       │
              │   (Django REST)     │
              └─────────────────────┘
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
┌────────────────────┐   ┌────────────────────┐
│   PostgreSQL DB    │   │    WGER API        │
│   (User Data)      │   │   (Exercises)      │
└────────────────────┘   └────────────────────┘
```

### Detailed System Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
├─────────────────────────────────────────────────────────────┤
│  Web / Mobile / PWA                                         │
│                                                              │
│  Components:                                                 │
│  - WorkoutLog (Log new workouts)                           │
│  - WorkoutHistory (View past workouts)                     │
│  - ProgressChart (Visualize progress)                      │
│  - ExerciseSearch (Search WGER database)                   │
│  - GoalTracker (Set and track goals)                       │
│  - UserProfile (Manage profile)                            │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   State Management Layer                     │
├─────────────────────────────────────────────────────────────┤
│  Redux Store / Zustand                                      │
│                                                              │
│  Slices:                                                     │
│  - authSlice (User authentication)                          │
│  - workoutsSlice (Workout data)                            │
│  - exercisesSlice (WGER exercises cache)                   │
│  - goalsSlice (Fitness goals)                              │
│  - profileSlice (User profile)                             │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    API Integration Layer                     │
├─────────────────────────────────────────────────────────────┤
│  Axios / Fetch API                                          │
│                                                              │
│  Services:                                                   │
│  - authService (Login, Register, JWT)                       │
│  - workoutService (CRUD activities)                         │
│  - wgerService (Fetch exercises from WGER)                 │
│  - goalService (Goal management)                            │
│  - profileService (Profile updates)                         │
└─────────────────────────────────────────────────────────────┘
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
┌────────────────────┐   ┌────────────────────┐
│  BioSync Backend   │   │    WGER API        │
│   (Django REST)    │   │  (External)        │
│                    │   │                    │
│  - Authentication  │   │  - Exercises       │
│  - Activity CRUD   │   │  - Muscle Groups   │
│  - Goals API       │   │  - Equipment       │
│  - Profile API     │   │  - Categories      │
│  - Metrics API     │   └────────────────────┘
└────────────────────┘
         │
         ▼
┌────────────────────┐
│   PostgreSQL DB    │
│                    │
│  Tables:           │
│  - users           │
│  - activities      │
│  - goals           │
│  - workout_plans   │
│  - meals           │
│  - achievements    │
└────────────────────┘
```

---

## 📡 API Documentation

### Authentication Endpoints

```http
# User Registration
POST /api/v1/auth/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe"
}

Response: 201 Created
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}

# User Login
POST /api/v1/auth/login/
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "SecurePass123!"
}

Response: 200 OK
{
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  },
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}

# Refresh Token
POST /api/v1/auth/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

Response: 200 OK
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

# Password Reset Request
POST /api/v1/auth/password-reset/
Content-Type: application/json

{
  "email": "john@example.com"
}

Response: 200 OK
{
  "message": "Password reset email sent"
}
```

### Activity Management Endpoints

```http
# List User Activities
GET /api/v1/activities/
Authorization: Bearer <access_token>
Query Parameters:
  - page: 1
  - limit: 20
  - activity_type: Running | Cycling | Weightlifting
  - date_from: 2024-01-01
  - date_to: 2024-12-31
  - sort_by: date | duration | calories

Response: 200 OK
{
  "count": 45,
  "next": "/api/v1/activities/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "activity_type": "Weightlifting",
      "duration": 60,
      "distance": null,
      "calories_burned": 350,
      "date": "2024-12-05T10:00:00Z",
      "exercises": [
        {
          "name": "Bench Press",
          "sets": 3,
          "reps": 10,
          "weight": 80
        }
      ],
      "notes": "Great workout!"
    }
  ]
}

# Create Activity
POST /api/v1/activities/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "activity_type": "Weightlifting",
  "duration": 60,
  "calories_burned": 350,
  "date": "2024-12-05T10:00:00Z",
  "exercises": [
    {
      "exercise_id": 123,
      "name": "Bench Press",
      "sets": 3,
      "reps": 10,
      "weight": 80
    },
    {
      "exercise_id": 145,
      "name": "Squats",
      "sets": 4,
      "reps": 8,
      "weight": 100
    }
  ],
  "notes": "Felt strong today"
}

Response: 201 Created
{
  "id": 46,
  "activity_type": "Weightlifting",
  "duration": 60,
  "calories_burned": 350,
  "date": "2024-12-05T10:00:00Z",
  "exercises": [...],
  "created_at": "2024-12-05T10:05:00Z"
}

# Get Activity Details
GET /api/v1/activities/:id/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "id": 1,
  "activity_type": "Weightlifting",
  "duration": 60,
  "exercises": [...],
  "notes": "Great workout!",
  "created_at": "2024-12-05T10:00:00Z",
  "updated_at": "2024-12-05T10:05:00Z"
}

# Update Activity
PUT /api/v1/activities/:id/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "duration": 65,
  "notes": "Updated: Felt even stronger!"
}

Response: 200 OK
{
  "id": 1,
  "duration": 65,
  "notes": "Updated: Felt even stronger!",
  "updated_at": "2024-12-05T11:00:00Z"
}

# Delete Activity
DELETE /api/v1/activities/:id/
Authorization: Bearer <access_token>

Response: 204 No Content
```

### Activity Metrics Endpoints

```http
# Get Activity Summary
GET /api/v1/activities/summary/
Authorization: Bearer <access_token>
Query Parameters:
  - period: week | month | year
  - date_from: 2024-01-01
  - date_to: 2024-12-31

Response: 200 OK
{
  "period": "month",
  "total_activities": 20,
  "total_duration": 1200,
  "total_distance": 50.5,
  "total_calories": 8500,
  "activity_breakdown": {
    "Running": 8,
    "Cycling": 5,
    "Weightlifting": 7
  },
  "average_duration": 60,
  "average_calories": 425
}

# Get Progress Trends
GET /api/v1/activities/trends/
Authorization: Bearer <access_token>
Query Parameters:
  - metric: duration | calories | distance
  - period: week | month | year

Response: 200 OK
{
  "metric": "calories",
  "period": "month",
  "data": [
    {
      "date": "2024-12-01",
      "value": 450
    },
    {
      "date": "2024-12-02",
      "value": 380
    }
  ]
}
```

### Goals Endpoints

```http
# List User Goals
GET /api/v1/goals/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "results": [
    {
      "id": 1,
      "title": "Run 100km this month",
      "goal_type": "distance",
      "target_value": 100,
      "current_value": 45.5,
      "unit": "km",
      "deadline": "2024-12-31",
      "status": "in_progress",
      "progress_percentage": 45.5
    }
  ]
}

# Create Goal
POST /api/v1/goals/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Bench press 100kg",
  "goal_type": "strength",
  "target_value": 100,
  "unit": "kg",
  "deadline": "2025-03-01"
}

Response: 201 Created

# Update Goal Progress
PUT /api/v1/goals/:id/progress/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "current_value": 55.2
}

Response: 200 OK
```

### Workout Plans Endpoints

```http
# List Workout Plans
GET /api/v1/workout-plans/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "results": [
    {
      "id": 1,
      "name": "5x5 Strength Program",
      "description": "Classic strength building program",
      "duration_weeks": 12,
      "difficulty": "intermediate",
      "workouts": [...]
    }
  ]
}

# Create Workout Plan
POST /api/v1/workout-plans/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "My Custom Plan",
  "description": "Personalized routine",
  "duration_weeks": 8,
  "workouts": [
    {
      "day": "Monday",
      "exercises": [
        {
          "exercise_id": 123,
          "sets": 3,
          "reps": 10
        }
      ]
    }
  ]
}

Response: 201 Created
```

### User Profile Endpoints

```http
# Get User Profile
GET /api/v1/profile/
Authorization: Bearer <access_token>

Response: 200 OK
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "bio": "Fitness enthusiast",
  "fitness_level": "intermediate",
  "height": 180,
  "weight": 75,
  "date_of_birth": "1990-01-15",
  "profile_picture": "https://example.com/avatar.jpg",
  "created_at": "2024-01-01T00:00:00Z"
}

# Update Profile
PUT /api/v1/profile/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "bio": "Marathon runner and weightlifter",
  "fitness_level": "advanced",
  "weight": 73
}

Response: 200 OK
```

### WGER API Integration

```http
# Fetch Exercises List
GET https://wger.de/api/v2/exercise/
Query Parameters:
  - language: 2 (English)
  - limit: 20
  - offset: 0

Response: 200 OK
{
  "count": 392,
  "next": "https://wger.de/api/v2/exercise/?limit=20&offset=20",
  "results": [
    {
      "id": 345,
      "name": "Bench Press",
      "description": "Lie on bench, lower bar to chest...",
      "category": 8,
      "muscles": [4],
      "equipment": [1]
    }
  ]
}

# Get Exercise Details
GET https://wger.de/api/v2/exerciseinfo/345/

Response: 200 OK
{
  "id": 345,
  "name": "Bench Press",
  "description": "Full exercise description...",
  "muscles": ["Pectoralis major"],
  "muscles_secondary": ["Triceps brachii"],
  "equipment": ["Barbell"],
  "images": [
    {
      "id": 1,
      "image": "https://wger.de/media/exercise-images/1/Bench-press-1.png"
    }
  ]
}

# Search by Muscle Group
GET https://wger.de/api/v2/exercise/?muscle=4
# muscle=4 represents Pectoralis major (Chest)

Response: 200 OK
{
  "results": [
    {
      "id": 345,
      "name": "Bench Press"
    },
    {
      "id": 346,
      "name": "Incline Bench Press"
    }
  ]
}
```

---

## 📂 Project Structure

### Frontend Structure (Web - Next.js)

```
biosync-web/
├── app/
│   ├── (auth)/
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── register/
│   │   │   └── page.tsx
│   │   └── reset-password/
│   │       └── page.tsx
│   ├── (dashboard)/
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   ├── workouts/
│   │   │   ├── page.tsx
│   │   │   ├── new/
│   │   │   │   └── page.tsx
│   │   │   └── [id]/
│   │   │       └── page.tsx
│   │   ├── history/
│   │   │   └── page.tsx
│   │   ├── progress/
│   │   │   └── page.tsx
│   │   ├── goals/
│   │   │   └── page.tsx
│   │   ├── exercises/
│   │   │   ├── page.tsx
│   │   │   └── [id]/
│   │   │       └── page.tsx
│   │   ├── plans/
│   │   │   └── page.tsx
│   │   └── nutrition/
│   │       └── page.tsx
│   ├── profile/
│   │   ├── page.tsx
│   │   ├── settings/
│   │   │   └── page.tsx
│   │   └── achievements/
│   │       └── page.tsx
│   ├── community/
│   │   ├── leaderboard/
│   │   │   └── page.tsx
│   │   └── challenges/
│   │       └── page.tsx
│   ├── api/
│   │   └── (BFF routes)
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── common/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   ├── Modal.tsx
│   │   ├── Loading.tsx
│   │   └── Toast.tsx
│   ├── layout/
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   ├── Footer.tsx
│   │   └── MobileNav.tsx
│   ├── workouts/
│   │   ├── WorkoutLog.tsx
│   │   ├── WorkoutCard.tsx
│   │   ├── WorkoutHistory.tsx
│   │   ├── ExerciseSearch.tsx
│   │   └── ExerciseCard.tsx
│   ├── progress/
│   │   ├── ProgressChart.tsx
│   │   ├── StatsCard.tsx
│   │   └── CalendarHeatmap.tsx
│   ├── goals/
│   │   ├── GoalCard.tsx
│   │   ├── GoalForm.tsx
│   │   └── GoalProgress.tsx
│   └── auth/
│       ├── LoginForm.tsx
│       ├── RegisterForm.tsx
│       └── ProtectedRoute.tsx
├── lib/
│   ├── redux/
│   │   ├── store.ts
│   │   ├── slices/
│   │   │   ├── authSlice.ts
│   │   │   ├── workoutsSlice.ts
│   │   │   ├── exercisesSlice.ts
│   │   │   ├── goalsSlice.ts
│   │   │   └── profileSlice.ts
│   │   └── api/
│   │       └── apiSlice.ts
│   ├── utils/
│   │   ├── api.ts
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   └── types/
│       ├── workout.ts
│       ├── exercise.ts
│       ├── user.ts
│       └── goal.ts
├── public/
│   ├── icons/
│   ├── images/
│   ├── manifest.json
│   └── sw.js
├── styles/
│   └── globals.css
├── .env.local
├── next.config.js
├── tailwind.config.js
├── tsconfig.json
└── package.json
```

### Frontend Structure (Mobile - React Native)

```
biosync-mobile/
├── app/
│   ├── (tabs)/
│   │   ├── _layout.tsx
│   │   ├── index.tsx (Dashboard)
│   │   ├── workouts.tsx
│   │   ├── progress.tsx
│   │   └── profile.tsx
│   ├── (auth)/
│   │   ├── login.tsx
│   │   ├── register.tsx
│   │   └── forgot-password.tsx
│   ├── workout/
│   │   ├── new.tsx
│   │   └── [id].tsx
│   ├── exercise/
│   │   ├── search.tsx
│   │   └── [id].tsx
│   ├── goal/
│   │   ├── new.tsx
│   │   └── [id].tsx
│   ├── _layout.tsx
│   └── index.tsx
├── components/
│   ├── common/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   ├── Loading.tsx
│   │   └── EmptyState.tsx
│   ├── workouts/
│   │   ├── WorkoutCard.tsx
│   │   ├── WorkoutList.tsx
│   │   ├── ExerciseSearch.tsx
│   │   └── ExerciseSelector.tsx
│   ├── progress/
│   │   ├── ProgressChart.tsx
│   │   ├── StatsCard.tsx
│   │   └── ActivityCalendar.tsx
│   └── navigation/
│       ├── TabBar.tsx
│       └── Header.tsx
├── store/
│   ├── index.ts
│   └── slices/
│       ├── authSlice.ts
│       ├── workoutsSlice.ts
│       ├── exercisesSlice.ts
│       └── goalsSlice.ts
├── services/
│   ├── api.ts
│   └── wgerApi.ts
├── types/
│   ├── workout.ts
│   ├── exercise.ts
│   ├── user.ts
│   └── goal.ts
├── utils/
│   ├── formatters.ts
│   ├── validators.ts
│   └── storage.ts
├── constants/
│   ├── Colors.ts
│   └── Config.ts
├── assets/
│   ├── images/
│   └── fonts/
├── styles/
│   └── global.css
├── app.json
├── tailwind.config.js
├── tsconfig.json
└── package.json
```

### Backend Structure (Django)

```
biosync-backend/
├── biosync/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── tests.py
│   ├── activities/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   └── tests.py
│   ├── goals/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── workout_plans/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   ├── nutrition/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   └── social/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
├── utils/
│   ├── permissions.py
│   ├── pagination.py
│   ├── exceptions.py
│   ├── validators.py
│   └── wger_integration.py
├── tests/
│   ├── test_activities.py
│   ├── test_goals.py
│   └── test_auth.py
├── static/
├── media/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

**System Requirements:**
- Node.js 18+ (Frontend)
- Python 3.11+ (Backend)
- PostgreSQL 15+ (Database)
- Docker & Docker Compose (Optional, Recommended)
- Git version control

**Development Tools:**
- VS Code / PyCharm
- Postman (API testing)
- PostgreSQL client (pgAdmin, DBeaver)
- React DevTools (browser extension)

### Installation

#### Backend Setup

```bash
# Clone the repository
git clone https://github.com/Dwaynemaster007/BioSync-PWA.git
cd BioSync-PWA

# Navigate to backend directory
cd biosync-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your configurations

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata fixtures/sample_data.json

# Run development server
python manage.py runserver

# Backend will be running at http://localhost:8000
# Admin panel: http://localhost:8000/admin
# API docs: http://localhost:8000/api/docs
```

#### Frontend Setup (Web - Next.js)

```bash
# Navigate to web frontend directory
cd ../biosync-web

# Install dependencies
npm install

# Create .env.local file
cp .env.example .env.local
# Add your API URL and other configs

# Run development server
npm run dev

# Web app will be running at http://localhost:3000
```

#### Frontend Setup (Mobile - React Native)

```bash
# Navigate to mobile frontend directory
cd ../biosync-mobile

# Install dependencies
npm install

# Start Expo development server
npx expo start

# Scan QR code with:
# - iOS: Camera app
# - Android: Expo Go app
```

### Docker Setup (Recommended)

```bash
# From project root
cd BioSync-PWA

# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Services:
# - Backend API: http://localhost:8000
# - Web App: http://localhost:3000
# - PostgreSQL: localhost:5432
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: biosync_db
      POSTGRES_USER: biosync_user
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./biosync-backend
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./biosync-backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://biosync_user:secure_password@db:5432/biosync_db

  frontend:
    build: ./biosync-web
    command: npm run dev
    volumes:
      - ./biosync-web:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000

volumes:
  postgres_data:
```

---

## 🧪 Testing

### Backend Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.activities

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html

# Run tests in Docker
docker-compose exec backend python manage.py test
```

### Frontend Testing

```bash
# Web - Next.js
cd biosync-web

# Run unit tests
npm test

# Run with coverage
npm test -- --coverage

# Run E2E tests (if configured)
npm run test:e2e

# Mobile - React Native
cd biosync-mobile

# Run tests
npm test
```

---

## 📊 Database Schema

### Core Models

```python
# users/models.py
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True)
    fitness_level = models.CharField(max_length=20, choices=FITNESS_LEVELS)
    height = models.IntegerField(null=True)  # in cm
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)  # in kg
    date_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# activities/models.py
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration = models.IntegerField()  # in minutes
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # in km
    calories_burned = models.IntegerField(null=True)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Exercise(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='exercises')
    wger_exercise_id = models.IntegerField()
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # in kg

# goals/models.py
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=255)
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES)
    target_value = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=20)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# workout_plans/models.py
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration_weeks = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class WorkoutDay(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='workout_days')
    day_name = models.CharField(max_length=50)
    exercises = models.JSONField()  # Store exercise details
```

---

## 🎨 UI/UX Design Principles

### Design System

**Color Palette:**
```css
/* Primary Colors */
--primary-green: #10B981;     /* Success, Active states */
--primary-blue: #3B82F6;      /* Links, Info */
--primary-purple: #8B5CF6;    /* Premium features */

/* Neutral Colors */
--gray-50: #F9FAFB;
--gray-900: #111827;
--white: #FFFFFF;
--black: #000000;

/* Semantic Colors */
--success: #10B981;
--warning: #F59E0B;
--error: #EF4444;
--info: #3B82F6;
```

**Typography:**
```css
/* Font Family */
font-family: 'Inter', system-ui, sans-serif;

/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
```

**Spacing:**
```css
/* Consistent spacing scale */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
```

### Responsive Breakpoints

```javascript
// TailwindCSS breakpoints
const breakpoints = {
  sm: '640px',   // Mobile landscape
  md: '768px',   // Tablet
  lg: '1024px',  // Desktop
  xl: '1280px',  // Large desktop
  '2xl': '1536px' // Extra large
}
```

---

## 🚢 Deployment

### Frontend Deployment (Vercel)

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
cd biosync-web
vercel

# Production deployment
vercel --prod
```

### Backend Deployment (Heroku)

```bash
# Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create new app
heroku create biosync-api

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

### Alternative: PythonAnywhere

```bash
# 1. Sign up at pythonanywhere.com
# 2. Upload code via Git
# 3. Create virtual environment
# 4. Install requirements
# 5. Configure WSGI file
# 6. Set up static files
# 7. Reload web app
```

---

## 📈 Future Enhancements

### Short-Term (Next 3 Months)

**Features:**
- ✅ Exercise video tutorials
- ✅ Workout rest timer
- ✅ Voice commands for logging
- ✅ Apple Health / Google Fit integration
- ✅ Workout streaks and badges
- ✅ Dark mode improvements

**Technical:**
- ✅ GraphQL API implementation
- ✅ Real-time notifications with WebSockets
- ✅ Redis caching layer
- ✅ CDN for static assets
- ✅ Performance monitoring (Sentry)

### Mid-Term (3-6 Months)

**Features:**
- 🎯 AI-powered workout recommendations
- 🎯 Personal trainer marketplace
- 🎯 Group challenges and competitions
- 🎯 Live workout classes
- 🎯 Meal planning and recipes
- 🎯 Integration with smart scales

**Technical:**
- 🎯 Microservices architecture
- 🎯 Kubernetes deployment
- 🎯 Advanced analytics dashboard
- 🎯 Machine learning for predictions
- 🎯 API rate limiting improvements

### Long-Term (6-12 Months)

**Features:**
- 🚀 AR workout form checker
- 🚀 Virtual reality workouts
- 🚀 Certified trainer certifications
- 🚀 E-commerce for supplements
- 🚀 Corporate wellness programs
- 🚀 White-label solutions

**Technical:**
- 🚀 Multi-region deployment
- 🚀 Advanced security features
- 🚀 Blockchain for achievements
- 🚀 AI chatbot for fitness advice
- 🚀 Advanced data analytics

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click 'Fork' on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yourusername/BioSync-PWA.git
   cd BioSync-PWA
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new features
   - Update documentation

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: Add your feature description"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe your changes
   - Reference related issues
   - Add screenshots for UI changes

### Contribution Guidelines

- ✅ Follow React/Django best practices
- ✅ Write meaningful commit messages
- ✅ Add tests for new features
- ✅ Update documentation
- ✅ Keep PRs focused and small
- ✅ Be respectful and constructive

---

## 📝 Git Commit Workflow

### Commit Message Format

```bash
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Code style (formatting, no logic change)
- `refactor` - Code refactoring
- `perf` - Performance improvement
- `test` - Adding tests
- `chore` - Maintenance tasks

### Examples

```bash
# Initial Setup
git commit -m "feat: set up project structure with React and TypeScript"
git commit -m "feat: add API integration for fetching product data"

# Feature Development
git commit -m "feat: implement workout logging functionality"
git commit -m "feat: add progress tracking with charts"
git commit -m "feat: integrate WGER API for exercise data"
git commit -m "feat(goals): implement goal setting and tracking"

# UI Enhancements
git commit -m "style: enhance UI with Tailwind CSS"
git commit -m "style(mobile): improve responsive design"

# Bug Fixes
git commit -m "fix: resolve bug in workout filtering logic"
git commit -m "fix(auth): correct JWT token refresh issue"

# Backend
git commit -m "feat(backend): implement JWT authentication"
git commit -m "feat(api): add workout CRUD endpoints"
git commit -m "perf(db): optimize database queries with indexing"

# Documentation
git commit -m "docs: update README with setup instructions"
git commit -m "docs(api): add Swagger documentation"

# Deployment
git commit -m "chore: configure deployment for Vercel"
git commit -m "chore(docker): add Docker configuration"
```

---

## 🐛 Known Issues & Troubleshooting

### Common Issues

**Issue 1: WGER API Rate Limiting**
```javascript
// Solution: Implement caching
const cachedExercises = localStorage.getItem('exercises');
if (cachedExercises) {
  return JSON.parse(cachedExercises);
}
// Fetch from API and cache
```

**Issue 2: JWT Token Expiration**
```typescript
// Solution: Implement token refresh
axios.interceptors.response.use(
  response => response,
  async error => {
    if (error.response.status === 401) {
      // Refresh token logic
      await refreshToken();
      return axios.request(error.config);
    }
    return Promise.reject(error);
  }
);
```

**Issue 3: CORS Errors**
```python
# Solution: Configure CORS in Django
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:19006",
]
CORS_ALLOW_CREDENTIALS = True
```

---

## 📚 Resources & References

### Official Documentation

**Frontend:**
- [React Documentation](https://reactjs.org/)
- [Next.js Docs](https://nextjs.org/docs)
- [React Native Docs](https://reactnative.dev/)
- [Expo Documentation](https://docs.expo.dev/)
- [TailwindCSS](https://tailwindcss.com/)
- [Redux Toolkit](https://redux-toolkit.js.org/)

**Backend:**
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [JWT Authentication](https://jwt.io/)

**APIs:**
- [WGER API Docs](https://wger.de/en/software/api)

### Learning Resources

**Tutorials:**
- [freeCodeCamp](https://www.freecodecamp.org/)
- [Real Python](https://realpython.com/)
- [React Native Express](https://www.reactnative.express/)

**Community:**
- [Stack Overflow](https://stackoverflow.com/)
- [Reddit r/reactnative](https://www.reddit.com/r/reactnative/)
- [Reddit r/django](https://www.reddit.com/r/django/)

---
 align="center">

## 💜 Built with Excellence & Passion 💜

### *From Concept to Deployment - A Full-Stack Journey* 🚀✨

**Created by [Thubelihle Dlamini (Dwaynemaster007)](https://github.com/Dwaynemaster007)**

---

[![GitHub](https://img.shields.io/badge/GitHub-Dwaynemaster007-181717?style=for-the-badge&logo=github)](https://github.com/Dwaynemaster007)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Thubelihle_Dlamini-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/thubelihledlamini/)
[![Twitter](https://img.shields.io/badge/Twitter-@dwaynemaster-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/dwaynemaster)
[![Email](https://img.shields.io/badge/Email-thubelihledlamini88-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:thubelihledlamini88@gmail.com)

---

*"Code is like humor. When you have to explain it, it's bad."* – Cory House

*"First, solve the problem. Then, write the code."* – John Johnson

*"The best error message is the one that never shows up."* – Thomas Fuchs

---

**Last Updated:** November 2025  
**Version:** 1.0.0  
**License:** Educational Use - ALX Africa  

© 2025 ALX Africa. All rights reserved.

</div
