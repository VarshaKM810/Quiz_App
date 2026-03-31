import React from 'react'

const Intro = ({ onStart, loading, error }) => {
  return (
    <div className="card intro-card">
      <h1>Quiz App</h1>
      <p style={{ marginBottom: '2rem', opacity: 0.8 }}>
        Test your knowledge of web development with this interactive quiz. 
        Are you ready to challenge yourself?
      </p>
      {error && <p className="incorrect" style={{ marginBottom: '1rem' }}>{error}</p>}
      <button 
        className="btn btn-primary" 
        onClick={onStart}
        disabled={loading}
      >
        {loading ? 'Loading...' : 'Start Quiz'}
      </button>
    </div>
  )
}

export default Intro
