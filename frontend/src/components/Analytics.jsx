import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { Trophy, Star, TrendingUp, Award, ArrowLeft, Zap, Shield } from 'lucide-react';

const Analytics = ({ onBack }) => {
  const [profile, setProfile] = useState(null);
  const [analytics, setAnalytics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        const headers = { Authorization: `Bearer ${token}` };
        
        const [profRes, analytRes] = await Promise.all([
          axios.get('http://localhost:8000/api/user/profile', { headers }),
          axios.get('http://localhost:8000/api/user/analytics', { headers })
        ]);
        
        setProfile(profRes.data);
        setAnalytics(analytRes.data);
      } catch (err) {
        setError('Failed to load profile data.');
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <div className="loader">Analyzing Performance...</div>;
  if (error) return <div className="error-banner">{error}</div>;

  const COLORS = ['#6366f1', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981'];

  return (
    <div className="card material-card analytics-page">
      <div className="material-header" style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button className="icon-btn" onClick={onBack}>
            <ArrowLeft size={20} />
          </button>
          <h1>Learning Insights</h1>
        </div>
      </div>

      <div className="profile-stats-grid">
        <div className="stat-card level-card">
          <div className="stat-icon"><Zap size={24} /></div>
          <div className="stat-info">
            <span className="stat-label">Current Level</span>
            <span className="stat-value">Level {profile.level}</span>
            <div className="xp-bar-container">
              <div className="xp-bar-fill" style={{ width: `${(profile.xp % 1000) / 10}%` }}></div>
            </div>
            <span className="xp-text">{profile.xp % 1000} / 1000 XP to next level</span>
          </div>
        </div>

        <div className="stat-card xp-total-card">
          <div className="stat-icon"><Star size={24} /></div>
          <div className="stat-info">
            <span className="stat-label">Total XP</span>
            <span className="stat-value">{profile.xp.toLocaleString()}</span>
          </div>
        </div>

        <div className="stat-card badges-count-card">
          <div className="stat-icon"><Award size={24} /></div>
          <div className="stat-info">
            <span className="stat-label">Badges Earned</span>
            <span className="stat-value">{profile.badges.length}</span>
          </div>
        </div>
      </div>

      <div className="analytics-content-grid">
        <div className="chart-section">
          <h3><TrendingUp size={18} style={{ marginRight: '8px' }} /> Performance by Category</h3>
          <div style={{ height: '300px', marginTop: '20px' }}>
            {analytics.length > 0 ? (
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={analytics}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--border)" />
                  <XAxis dataKey="category" axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 12 }} />
                  <YAxis axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 12 }} domain={[0, 100]} />
                  <Tooltip 
                    contentStyle={{ borderRadius: '12px', border: 'none', background: 'var(--card-bg)', boxShadow: 'var(--shadow-lg)' }}
                    itemStyle={{ color: 'var(--primary)', fontWeight: 'bold' }}
                  />
                  <Bar dataKey="average_score" radius={[4, 4, 0, 0]} barSize={40}>
                    {analytics.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            ) : (
              <p className="empty-state">Complete a quiz to see your insights!</p>
            )}
          </div>
        </div>

        <div className="badges-section">
          <h3><Shield size={18} style={{ marginRight: '8px' }} /> Achievements</h3>
          <div className="badge-list">
            {profile.badges.length > 0 ? profile.badges.map((badge, idx) => (
              <div key={idx} className="badge-item">
                <div className="badge-icon-bg">
                  <Award size={20} />
                </div>
                <div className="badge-info">
                  <span className="badge-name">{badge.name}</span>
                  <span className="badge-desc">{badge.description}</span>
                </div>
              </div>
            )) : (
              <p className="empty-state">No badges yet. Keep studying!</p>
            )}
          </div>
        </div>
      </div>

      <div className="material-footer" style={{ marginTop: '32px' }}>
        <button className="btn btn-primary" onClick={onBack}>
          <ArrowLeft size={18} />
          Back to Dashboard
        </button>
      </div>
    </div>
  );
};

export default Analytics;
