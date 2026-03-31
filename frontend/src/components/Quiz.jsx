import React, { useState, useEffect, useCallback } from 'react';
import { Timer, ArrowRight, CheckCircle2, Shield } from 'lucide-react';

const Quiz = ({ quiz, onSubmit, onReturn, loading: submitting }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState([]);
  const [currentOption, setCurrentOption] = useState(null);
  const [timeLeft, setTimeLeft] = useState(30);
  const [tabSwitches, setTabSwitches] = useState(0);
  const [cheatingDetected, setCheatingDetected] = useState(false);

  const currentQuestion = quiz.questions[currentIndex];
  const progress = (currentIndex / quiz.questions.length) * 100;

  // 1. Move the logic into a stable callback
  const handleNext = useCallback(() => {
    const newAnswer = {
      question_id: currentQuestion.id,
      option_id: currentOption || -1
    };
    
    const newAnswers = [...selectedAnswers, newAnswer];
    setSelectedAnswers(newAnswers);
    setCurrentOption(null);

    if (currentIndex < quiz.questions.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setTimeLeft(-1);
      onSubmit(newAnswers, cheatingDetected);
    }
  }, [currentIndex, currentOption, currentQuestion.id, onSubmit, quiz.questions.length, selectedAnswers, cheatingDetected]);

  // 2. Tab-switch detection
  useEffect(() => {
    const handleVisibilityChange = () => {
      if (document.hidden) {
        setTabSwitches(prev => {
          const newCount = prev + 1;
          if (newCount >= 2) setCheatingDetected(true);
          return newCount;
        });
      }
    };

    const handleBlur = () => {
      setTabSwitches(prev => {
        const newCount = prev + 1;
        if (newCount >= 2) setCheatingDetected(true);
        return newCount;
      });
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('blur', handleBlur);
    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('blur', handleBlur);
    };
  }, []);

  // 3. Timer logic
  useEffect(() => {
    if (submitting || timeLeft < 0) return;

    if (timeLeft === 0) {
      handleNext();
      return;
    }
    const timer = setInterval(() => setTimeLeft(prev => prev - 1), 1000);
    return () => clearInterval(timer);
  }, [timeLeft, handleNext, submitting]);

  useEffect(() => {
    setTimeLeft(30);
  }, [currentIndex]);

  return (
    <div className="card quiz-card">
      {cheatingDetected && (
        <div className="cheating-warning-overlay">
          <div className="warning-content">
            <Shield size={48} color="#ef4444" />
            <h2>Cheating Detected!</h2>
            <p>Your progress is being monitored. Multiple tab switches will be logged.</p>
            <button className="btn btn-primary" onClick={() => setCheatingDetected(false)}>
              I Understand
            </button>
          </div>
        </div>
      )}

      <div className="quiz-header">
        <div className="quiz-progress-info">
          <span className="quiz-title-label">{quiz.title}</span>
          <span className="question-counter">Question {currentIndex + 1} of {quiz.questions.length}</span>
        </div>
        <div className={`quiz-timer ${timeLeft < 10 ? 'danger' : ''}`}>
          <Timer size={18} />
          <span>{timeLeft}s</span>
        </div>
      </div>

      <div className="progress-bar-container">
        <div className="progress-bar-fill" style={{ width: `${progress}%` }}></div>
      </div>

      <h2 className="question-text">{currentQuestion.question_text}</h2>

      <div className="options-list">
        {currentQuestion.options.map((option) => (
          <div 
            key={option.id}
            className={`option-item ${currentOption === option.id ? 'selected' : ''}`}
            onClick={() => setCurrentOption(option.id)}
          >
            <div className="option-indicator"></div>
            <span className="option-text">{option.option_text}</span>
            {currentOption === option.id && <CheckCircle2 size={18} className="selected-icon" />}
          </div>
        ))}
      </div>

      <div className="quiz-footer">
        <button 
          className="btn btn-outline" 
          onClick={onReturn}
          disabled={submitting}
        >
          Cancel & Return
        </button>
        <button 
          className="btn btn-primary next-btn" 
          onClick={handleNext}
          disabled={submitting}
        >
          {currentIndex === quiz.questions.length - 1 ? 'Finish Quiz' : 'Next Question'}
          <ArrowRight size={18} />
        </button>
      </div>
    </div>
  );
};

export default Quiz;
