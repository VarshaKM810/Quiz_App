import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BookOpen, Loader, Award, Sparkles } from 'lucide-react';

const Dashboard = ({ onSelectQuiz, onStudyQuiz, onOpenAI, loading: appLoading }) => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/quizzes');
        setQuizzes(response.data);
      } catch (error) {
        console.error('Failed to fetch quizzes', error);
      } finally {
        setLoading(false);
      }
    };
    fetchQuizzes();
  }, []);

  if (loading) return <div className="loader"><Loader className="animate-spin" /> Fetching Quizzes...</div>;

  return (
    <div className="dashboard-container">
      <div className="ai-promo-card" style={{ 
        background: 'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)', 
        color: 'white', 
        padding: '32px', 
        borderRadius: '20px', 
        marginBottom: '40px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        boxShadow: '0 20px 25px -5px rgba(99, 102, 241, 0.3)'
      }}>
        <div style={{ maxWidth: '60%' }}>
          <h2 style={{ fontSize: '1.75rem', marginBottom: '8px' }}>AI-Powered Learning</h2>
          <p style={{ opacity: 0.9 }}>Can't find what you're looking for? Generate a custom quiz on any topic using Gemini AI.</p>
          <button 
            className="btn" 
            style={{ marginTop: '20px', background: 'white', color: '#6366f1' }}
            onClick={onOpenAI}
          >
            <Sparkles size={18} />
            Try AI Generator
          </button>
        </div>
        <div className="ai-icon-large">
          <Sparkles size={80} style={{ opacity: 0.2 }} />
        </div>
      </div>

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '32px' }}>
        <h2 className="section-title" style={{ margin: 0 }}>Available Quizzes</h2>
        <button className="btn btn-outline" onClick={() => (window.location.hash = '#leaderboard')}>
          <Award size={18} />
          View Leaderboard
        </button>
      </div>

      <div className="quiz-grid">
        {quizzes.map((quiz) => (
          <div 
            key={quiz.id} 
            className="quiz-card"
          >
            <div className="quiz-card-content">
              <div className="quiz-icon-bg">
                <BookOpen size={24} />
              </div>
              <div className="quiz-info">
                <h3>{quiz.title}</h3>
                <p>{quiz.description || 'Test your skills in this subject.'}</p>
              </div>
            </div>
            
            <div className="quiz-card-actions">
              <button 
                className="btn btn-outline btn-sm" 
                onClick={() => onStudyQuiz(quiz.id)}
              >
                Study
              </button>
              <button 
                className="btn btn-primary btn-sm"
                onClick={() => onSelectQuiz(quiz.id)}
              >
                Start Quiz
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
