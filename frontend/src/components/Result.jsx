import React from 'react';
import { Trophy, RotateCcw, BarChart3 } from 'lucide-react';

const Result = ({ result, quizTitle, onRestart }) => {
  const isGreat = result.percentage >= 80;
  
  return (
    <div className="card result-card">
      <div className="result-header">
        <Trophy size={64} className={isGreat ? 'trophy-gold' : 'trophy-silver'} />
        <h1>{isGreat ? 'Congratulations!' : 'Goal Reached!'}</h1>
        <p>You completed the <strong>{quizTitle}</strong></p>
      </div>

      <div className="score-summary">
        <div className="score-main">
          <span className="score-value">{result.score}</span>
          <span className="score-divider">/</span>
          <span className="score-total">{result.total}</span>
        </div>
        <div className="percentage-bar">
          <div className="percentage-fill" style={{ width: `${result.percentage}%` }}></div>
        </div>
        <p className="percentage-text">{Math.round(result.percentage)}% Correct</p>
      </div>

      <div className="result-actions">
        <button className="btn btn-primary" onClick={onRestart}>
          <RotateCcw size={18} />
          Try Another Quiz
        </button>
        <button className="btn btn-outline" onClick={() => (window.location.hash = '#leaderboard')}>
          <BarChart3 size={18} />
          View Leaderboard
        </button>
      </div>
    </div>
  );
};

export default Result;
