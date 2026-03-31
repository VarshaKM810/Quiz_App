import React, { useState, useEffect, useCallback } from 'react';
import { AuthProvider, useAuth } from './context/AuthContext';
import axios from 'axios';
import Quiz from './components/Quiz';
import Result from './components/Result';
import Dashboard from './components/Dashboard';
import Material from './components/Material';
import Login from './components/Login';
import Signup from './components/Signup';
import Leaderboard from './components/Leaderboard';
import Analytics from './components/Analytics';
import AIGenerator from './components/AIGenerator';
import { LogOut, Sun, Moon, Trophy, BarChart3, Sparkles } from 'lucide-react';

const AppContent = () => {
  const { user, logout, loading: authLoading } = useAuth();
  const [step, setStep] = useState('dashboard'); // 'dashboard', 'quiz', 'result', 'material', 'analytics', 'ai-generator'
  const [showAuth, setShowAuth] = useState('login'); // 'login', 'signup'
  const [currentQuiz, setCurrentQuiz] = useState(null);
  const [currentMaterial, setCurrentMaterial] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  }, [darkMode]);

  const fetchQuizData = async (quizId) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`http://localhost:8000/api/quiz/${quizId}`);
      setCurrentQuiz(response.data);
      setStep('quiz');
    } catch (err) {
      setError('Failed to load quiz. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const fetchMaterialData = async (quizId) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`http://localhost:8000/api/quiz/${quizId}/material`);
      setCurrentMaterial(response.data);
      setStep('material');
    } catch (err) {
      setError('Failed to load study material.');
    } finally {
      setLoading(false);
    }
  };

  const submitQuiz = useCallback(async (answers, cheatingDetected = false) => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const payload = {
        quiz_id: currentQuiz.id,
        answers: answers,
        cheating_detected: cheatingDetected
      };
      const response = await axios.post(`http://localhost:8000/api/submit`, payload, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setResult(response.data);
      setStep('result');
    } catch (err) {
      setError('Failed to submit results. Please ensure you are logged in.');
    } finally {
      setLoading(false);
    }
  }, [currentQuiz]);

  const handleRestart = () => {
    setStep('dashboard');
    setCurrentQuiz(null);
    setCurrentMaterial(null);
    setResult(null);
    window.location.hash = '';
  };

  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash;
      if (hash === '#leaderboard') {
        setStep('leaderboard');
      } else if (hash === '#analytics') {
        setStep('analytics');
      } else if (hash === '') {
        setStep('dashboard');
      }
    };
    window.addEventListener('hashchange', handleHashChange);
    handleHashChange(); // Initial check
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  if (authLoading) return <div className="loader">Loading Auth...</div>;

  if (!user) {
    return (
      <div className="auth-container">
        {showAuth === 'login' ? (
          <Login onToggleAuth={() => setShowAuth('signup')} />
        ) : (
          <Signup onToggleAuth={() => setShowAuth('login')} />
        )}
      </div>
    );
  }

  return (
    <div className={`app-container ${darkMode ? 'dark' : ''}`}>
      <header className="app-header">
        <div className="header-left">
          <h1>QuizMaster</h1>
        </div>
        <div className="header-right">
          <button className="icon-btn" onClick={() => (window.location.hash = '#analytics')} title="Insights & Profile">
            <BarChart3 size={20} />
          </button>
          <button className="icon-btn" onClick={() => setDarkMode(!darkMode)} title={`Switch to ${darkMode ? 'light' : 'dark'} mode`}>
            {darkMode ? <Sun size={20} /> : <Moon size={20} />}
          </button>
          <div className="user-profile">
            <span>⚡ Lvl {user.level || 1} · {user.username}</span>
            <button className="icon-btn logout-btn" onClick={logout} title="Logout">
              <LogOut size={18} />
            </button>
          </div>
        </div>
      </header>

      <main className="app-main">
        {error && <div className="error-banner">{error}</div>}
        
        {step === 'dashboard' && (
          <Dashboard 
            onSelectQuiz={fetchQuizData} 
            onStudyQuiz={fetchMaterialData}
            onOpenAI={() => setStep('ai-generator')}
            loading={loading} 
          />
        )}

        {step === 'ai-generator' && (
          <AIGenerator 
            onQuizGenerated={(quiz) => {
              setCurrentQuiz(quiz);
              setStep('quiz');
            }}
            onBack={() => setStep('dashboard')}
          />
        )}

        {step === 'leaderboard' && (
          <Leaderboard 
            onBack={() => { window.location.hash = ''; setStep('dashboard'); }}
          />
        )}

        {step === 'analytics' && (
          <Analytics 
            onBack={() => { window.location.hash = ''; setStep('dashboard'); }}
          />
        )}

        {step === 'material' && currentMaterial && (
          <Material 
            material={currentMaterial}
            onBack={() => setStep('dashboard')}
            onStartQuiz={fetchQuizData}
          />
        )}
        
        {step === 'quiz' && currentQuiz && (
          <Quiz 
            quiz={currentQuiz} 
            onSubmit={submitQuiz} 
            onReturn={() => setStep('dashboard')}
            loading={loading}
          />
        )}
        
        {step === 'result' && result && (
          <Result 
            result={result} 
            quizTitle={currentQuiz?.title}
            onRestart={handleRestart} 
          />
        )}
      </main>
    </div>
  );
};

const App = () => (
  <AuthProvider>
    <AppContent />
  </AuthProvider>
);

export default App;
