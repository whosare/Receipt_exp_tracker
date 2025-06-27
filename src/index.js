import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);

// Note: This version is missing the import and call for './index.css' and 'reportWebVitals'.
// These were likely removed either intentionally or accidentally during modification.
// They are not directly related to React Router.
