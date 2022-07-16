// 여러 개의 댓글을 포함하는 댓글 목록 컴포넌트

import React from "react";
import Comment from "./Comment";

const comments = [  // comment 데이터들을 별도의 객체로 분리하기
  {
    name: "HY",
    comment: "Hello, it's HY here."
  },
  {
    name: "Sev",
    comment: "Always"
  },
]

function CommentList(props) {
  return (
    <div>
      {comments.map((comment) => {
        return (
          <Comment name={comment.name} comment={comment.comment} />
        );
      })}
    </div>
  );
}

export default CommentList;

