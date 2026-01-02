import { useState } from 'react';
import './App.css';

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

const LOADING_MESSAGES = [
  { text: '🔬 Asking Isaac Newton...', duration: 1000 },
  { text: '🧠 Verifying from Einstein...', duration: 1500 },
  { text: '⚡ Calculating by Tesla...', duration: 1200 },
  { text: '🛸 Receiving data from alien planet 3.7 million light years away...', duration: 1800 },
  { text: '📡 Signal losing...', duration: 800 },
  { text: '🔄 Signal reconnecting...', duration: 1000 },
  { text: '✨ Processing quantum calculations...', duration: 1200 },
  { text: '🎯 Finalizing prediction...', duration: 500 }
];

function App() {
  const [selectedDay, setSelectedDay] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [currentMessage, setCurrentMessage] = useState('');
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    if (!selectedDay) return;
    
    setIsLoading(true);
    setProgress(0);
    setResult(null);

    let totalTime = 0;
    const totalDuration = LOADING_MESSAGES.reduce((sum, msg) => sum + msg.duration, 0);

    for (let i = 0; i < LOADING_MESSAGES.length; i++) {
      setCurrentMessage(LOADING_MESSAGES[i].text);
      
      const startProgress = (totalTime / totalDuration) * 100;
      const endProgress = ((totalTime + LOADING_MESSAGES[i].duration) / totalDuration) * 100;
      
      await animateProgress(startProgress, endProgress, LOADING_MESSAGES[i].duration);
      totalTime += LOADING_MESSAGES[i].duration;
    }

    const currentIndex = DAYS.indexOf(selectedDay);
    const nextDay = DAYS[(currentIndex + 1) % 7];
    
    setResult(nextDay);
    setIsLoading(false);
    setProgress(100);
  };

  const animateProgress = (start, end, duration) => {
    return new Promise((resolve) => {
      const startTime = Date.now();
      const animate = () => {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        setProgress(start + (end - start) * progress);
        
        if (progress < 1) {
          requestAnimationFrame(animate);
        } else {
          resolve();
        }
      };
      animate();
    });
  };

  const reset = () => {
    setSelectedDay('');
    setResult(null);
    setProgress(0);
    setCurrentMessage('');
  };

  return (
    <div className="app">
      <div className="stars"></div>
      <div className="stars2"></div>
      <div className="stars3"></div>
      
      <div className="container">
        <header className="header">
          <h1 className="title">🔮 Next Day Predictor</h1>
          <p className="subtitle">Powered by Quantum AI & Alien Technology</p>
        </header>

        {!isLoading && !result && (
          <div className="selector-container">
            <label className="label">Select Today's Day:</label>
            <div className="days-grid">
              {DAYS.map((day) => (
                <button
                  key={day}
                  className={`day-button ${selectedDay === day ? 'selected' : ''}`}
                  onClick={() => setSelectedDay(day)}
                >
                  {day}
                </button>
              ))}
            </div>
            <button 
              className="predict-button"
              onClick={handlePredict}
              disabled={!selectedDay}
            >
              🚀 Predict Tomorrow
            </button>
          </div>
        )}

        {isLoading && (
          <div className="loading-container">
            <div className="terminal">
              <div className="terminal-header">
                <span className="terminal-dot red"></span>
                <span className="terminal-dot yellow"></span>
                <span className="terminal-dot green"></span>
                <span className="terminal-title">quantum-predictor.exe</span>
              </div>
              <div className="terminal-body">
                <p className="terminal-text">{currentMessage}</p>
                <div className="progress-bar">
                  <div 
                    className="progress-fill" 
                    style={{ width: `${progress}%` }}
                  ></div>
                </div>
                <p className="progress-text">{Math.floor(progress)}%</p>
              </div>
            </div>
          </div>
        )}

        {result && !isLoading && (
          <div className="result-container">
            <div className="success-animation">🎉</div>
            <h2 className="result-title">Congratulations!</h2>
            <p className="result-text">Successfully calculated with 99.99% accuracy!</p>
            <div className="result-box">
              <p className="result-label">Tomorrow will be:</p>
              <h3 className="result-day">{result}</h3>
            </div>
            <button className="reset-button" onClick={reset}>
              🔄 Predict Again
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
