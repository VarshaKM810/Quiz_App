import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Trophy, ArrowLeft, Medal } from 'lucide-react';

const Leaderboard = ({ onBack }) => {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/leaderboard');
        setEntries(response.data);
      } catch (err) {
        setError('Failed to load leaderboard.');
      } finally {
        setLoading(false);
      }
    };
    fetchLeaderboard();
  }, []);

  if (loading) return <div className="loader">Loading Leaderboard...</div>;
  if (error) return <div className="error-banner">{error}</div>;

  return (
    <div className="card material-card">
      <div className="material-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button className="icon-btn" onClick={onBack}>
            <ArrowLeft size={20} />
          </button>
          <h1>Global Leaderboard</h1>
        </div>
        <p className="quiz-info" style={{ marginTop: '8px' }}>Top performers across all subjects</p>
      </div>

      <div className="leaderboard-container">
        {entries.length === 0 ? (
          <p style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
            No scores recorded yet. Be the first to top the charts!
          </p>
        ) : (
          <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid var(--border)', textAlign: 'left' }}>
                <th style={{ padding: '12px', color: 'var(--text-muted)' }}>Rank</th>
                <th style={{ padding: '12px', color: 'var(--text-muted)' }}>Player</th>
                <th style={{ padding: '12px', color: 'var(--text-muted)' }}>Quiz</th>
                <th style={{ padding: '12px', color: 'var(--text-muted)', textAlign: 'center' }}>Score</th>
                <th style={{ padding: '12px', color: 'var(--text-muted)', textAlign: 'right' }}>Accuracy</th>
              </tr>
            </thead>
            <tbody>
              {entries.map((entry, index) => (
                <tr key={index} style={{ borderBottom: '1px solid var(--border)', transition: 'var(--transition)' }} className="leaderboard-row">
                  <td style={{ padding: '16px 12px' }}>
                    {index === 0 ? <Trophy size={20} color="#facc15" /> : 
                     index === 1 ? <Medal size={20} color="#94a3b8" /> : 
                     index === 2 ? <Medal size={20} color="#b45309" /> : 
                     index + 1}
                  </td>
                  <td style={{ padding: '16px 12px', fontWeight: '600' }}>{entry.username}</td>
                  <td style={{ padding: '16px 12px', color: 'var(--text-muted)' }}>{entry.quiz_title}</td>
                  <td style={{ padding: '16px 12px', textAlign: 'center' }}>{entry.score} / {entry.total}</td>
                  <td style={{ padding: '16px 12px', textAlign: 'right', fontWeight: '700', color: 'var(--secondary)' }}>
                    {entry.percentage.toFixed(1)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      <div className="material-footer">
        <button className="btn btn-primary" onClick={onBack}>
          <ArrowLeft size={18} />
          Back to Dashboard
        </button>
      </div>
    </div>
  );
};

export default Leaderboard;
