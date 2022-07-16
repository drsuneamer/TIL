import React from "react";

// 현재 시각을 출력하는 component
function Clock(props) {
  return (
    <div>
      <h1>Hello, React!</h1>
      <h2>현재 시각: {new Date().toLocaleTimeString()}</h2>
    </div>
  );
}

export default Clock;