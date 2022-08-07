import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';

// import Library from './chapter_03/Library';   // ch03
// import Clock from './chapter_04/Clock';   // ch04
// import CommentList from './chapter_05/CommentList';   // ch05
// import NotificationList from './chapter_06/NotificationList'   // ch06
import Accommodate from './chapter_07/Accommodate'

ReactDOM.render(
  <React.StrictMode>
    <Accommodate />
  </React.StrictMode>,
  document.getElementById('root')
);

/* [chapter_06]
ReactDOM.render(
  <React.StrictMode>
    <NotificationList />
  </React.StrictMode>,
  document.getElementById('root')
);
*/

/* [chapter_05]
ReactDOM.render(
  <React.StrictMode>
    <CommentList />
  </React.StrictMode>,
  document.getElementById('root')
);
*/

/* [chapter_04]
// setInterval 함수를 사용하여 1000ms마다 Clock 컴포넌트를 새롭게 root div에 렌더링
setInterval(() => {
  ReactDOM.render(
    <React.StrictMode>
      <Clock />
    </React.StrictMode>,
    document.getElementById('root')
  );
}, 1000);
*/

/* [chapter_03]
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Library />
  </React.StrictMode>
);
*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
