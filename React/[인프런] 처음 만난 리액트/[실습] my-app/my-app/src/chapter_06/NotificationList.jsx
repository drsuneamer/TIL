import React from "react";
import Notification from "./Notification";

const reservedNotifications = [
  {
    message: "Hello, this is your schedule today.",
  },
  {
    message: "Lunch time!",
  },
  {
    message: "The meeting will start soon.",
  },
];

var timer;

class NotificationList extends React.Component {
  constructor(props) {    // 생성자에서는 앞으로 사용할 데이터를 state에 넣어서 초기화한다.
    super(props);

    this.state = {
      notifications: [],
    };
  }

  componentDidMount() {   // 1초마다 정해진 작업 수행 (미리 만들어둔 알림 데이터 배열로부터 state의 notification 배열에 넣고 update => setState 사용)
    const { notifications } = this.state;
    timer = setInterval(() => {
      if (notifications.length < reservedNotifications.length) {
        const index = notifications.length;
        notifications.push(reservedNotifications[index]);
        this.setState({
          notifications: notifications,
        });
      } else {
        clearInterval(timer);
      }
    }, 1000);
  }

  render() {
    return (
      <div>
        {this.state.notifications.map((notification) => {
          return <Notification message={notification.message} />;
        })}
      </div>
    );
  }
}

export default NotificationList;