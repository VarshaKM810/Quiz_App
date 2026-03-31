import React from 'react';
import { BookOpen, ArrowLeft, Play } from 'lucide-react';

const Material = ({ material, onBack, onStartQuiz }) => {
  if (!material) return <div className="loader">Loading material...</div>;

  // Simple parser to handle headers and lists in the content string
  const renderContent = (text) => {
    return text.split('\n').map((line, index) => {
      if (line.startsWith('# ')) {
        return <h1 key={index}>{line.replace('# ', '')}</h1>;
      }
      if (line.startsWith('## ')) {
        return <h2 key={index}>{line.replace('## ', '')}</h2>;
      }
      if (line.startsWith('### ')) {
        return <h3 key={index}>{line.replace('### ', '')}</h3>;
      }
      if (line.startsWith('- ')) {
        return <li key={index}>{line.replace('- ', '')}</li>;
      }
      if (line.trim() === '') {
        return <br key={index} />;
      }
      
      // Handle bold text **...**
      const processedLine = line.split(/(\*\*.*?\*\*)/).map((part, i) => {
        if (part.startsWith('**') && part.endsWith('**')) {
          return <strong key={i}>{part.slice(2, -2)}</strong>;
        }
        // Handle code `...`
        return part.split(/(`.*?`)/).map((subPart, j) => {
          if (subPart.startsWith('`') && subPart.endsWith('`')) {
            return <code key={`${i}-${j}`}>{subPart.slice(1, -1)}</code>;
          }
          return subPart;
        });
      });

      return <p key={index}>{processedLine}</p>;
    });
  };

  return (
    <div className="material-container">
      <div className="material-card">
        <div className="material-header">
          <div className="quiz-title-label">Study Guide</div>
          <h1>{material.title}</h1>
        </div>

        <div className="material-content">
          {renderContent(material.content)}
        </div>

        <div className="material-footer">
          <button className="btn btn-outline" onClick={onBack}>
            <ArrowLeft size={18} /> Back to Dashboard
          </button>
          <button className="btn btn-primary" onClick={() => onStartQuiz(material.quiz_id)}>
            Start Quiz <Play size={18} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Material;
