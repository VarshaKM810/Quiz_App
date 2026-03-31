import React, { useState } from 'react';
import axios from 'axios';
import { Sparkles, Brain, ArrowRight, Loader, AlertTriangle } from 'lucide-react';

const AIGenerator = ({ onQuizGenerated, onBack }) => {
  const [topic, setTopic] = useState('');
  const [numQuestions, setNumQuestions] = useState(5);
  const [difficulty, setDifficulty] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!topic.trim()) return;

    setLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post(
        'http://localhost:8000/api/quiz/generate',
        { topic, num_questions: numQuestions, difficulty: parseInt(difficulty) },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      onQuizGenerated(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate quiz. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card material-card analytics-page">
      <div className="material-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Sparkles className="trophy-gold" size={32} />
          <h1>AI Quiz Generator</h1>
        </div>
        <p className="quiz-info" style={{ marginTop: '8px' }}>
          Harness the power of Gemini to create a custom quiz on any topic in seconds.
        </p>
      </div>

      <form onSubmit={handleGenerate} className="ai-form" style={{ marginTop: '32px' }}>
        <div className="form-group">
          <label>What do you want to learn about?</label>
          <input 
            type="text" 
            placeholder="e.g. Quantum Physics, French Revolution, React Hooks..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            disabled={loading}
            required
            style={{ fontSize: '1.1rem', padding: '16px' }}
          />
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '24px' }}>
          <div className="form-group">
            <label>Number of Questions</label>
            <select 
              value={numQuestions} 
              onChange={(e) => setNumQuestions(e.target.value)}
              disabled={loading}
            >
              <option value="3">3 Questions</option>
              <option value="5">5 Questions</option>
              <option value="10">10 Questions</option>
            </select>
          </div>
          <div className="form-group">
            <label>Difficulty Level</label>
            <select 
              value={difficulty} 
              onChange={(e) => setDifficulty(e.target.value)}
              disabled={loading}
            >
              <option value="1">Beginner</option>
              <option value="2">Intermediate</option>
              <option value="3">Advanced</option>
            </select>
          </div>
        </div>

        {error && (
          <div className="error-banner" style={{ marginBottom: '24px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <AlertTriangle size={18} />
            {error}
          </div>
        )}

        <div className="material-footer" style={{ border: 'none', padding: 0 }}>
          <button type="button" className="btn btn-outline" onClick={onBack} disabled={loading}>
            Cancel
          </button>
          <button type="submit" className="btn btn-primary" disabled={loading || !topic.trim()}>
            {loading ? (
              <>
                <Loader className="animate-spin" size={18} />
                Generating...
              </>
            ) : (
              <>
                <Brain size={18} />
                Generate Quiz
                <ArrowRight size={18} />
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default AIGenerator;
