import logo from './logo.svg';
import './App.css';
import {useState} from 'react'

function Header(props) {   // 사용자 정의 태그! >> "컴포넌트"
  return <header>
    <h1><a href="/" onClick={(event)=>{  // a태그 클릭시 함수 호출
      event.preventDefault();
      props.onChangeMode();
    }}>{props.title}</a></h1>
  </header>
}

function Nav(props) {
  const lis = []
  for(let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
    // key: 이 반복문 안에서 고유해야 함
    lis.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={(event) => {
        event.preventDefault();
        props.onChangeMode(Number(event.target.id));  // Number 함수: JS에서 문자를 숫자로 converting
      }}>{t.title}</a>
    </li>)
  }
  return <nav>
        <ol>
          {lis}
        </ol>
      </nav>
}

function Article(props) {
  return <article>
        <h2>{props.title}</h2>
        {props.body}
      </article>
}

function Create(props){
  return <article>
    <h2>Create</h2>
    <form onSubmit={event=>{
      event.preventDefault();  // form태그 제출 시 리로드 현상 막음
      // title, body 값을 가져와야 함
      const title = event.target.title.value;  // event.target = form tag
      const body = event.target.body.value;
      props.onCreate(title, body);  // 실행 시 onCreate가 가리키는 함수가 실행

    }}>
      <p><input type="text" name="title" placeholder="title"/></p>
      <p><textarea name="body" placeholder="body"></textarea></p>
      <p><input type="submit" value="Create"/></p>
    </form>
  </article>
}

function App() {
  // const _mode = useState('WELCOME');
  // const mode = _mode[0];
  // const setMode = _mode[1];
  const [mode, setMode] = useState('WELCOME');  // 위 세 줄과 같은 코드
  const [id, setId] = useState(null)
  const [nextId, setNextId] = useState(4);  // id 따로 관리
  const [topics, setTopics] = useState([   // create시 추가될 수 있도록 useState로 승격
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'javascript', body: 'javascript is ...'}
  ]);

  let content = null;

  if(mode === 'WELCOME'){
    content = <Article title="Welcome" body="Hello, Web"></Article>
  } else if(mode === 'READ'){
    let title, body = null;
    for(let i=0; i<topics.length; i++){
      if(topics[i].id === id){
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>
  } else if(mode === 'CREATE'){
    content = <Create onCreate={(_title, _body)=>{
      const newTopic = {id:nextId, title:_title, body:_body}
      const newTopics = [...topics]   // topics의 복제본 생성
      newTopics.push(newTopic);
      setTopics(newTopics);
      setMode('READ');  // 생성 시 상세 페이지로 이동
      setId(nextId);
      setNextId(nextId+1);
    }}></Create>   // 별도의 Component 생성
  }
  return (
    <div>
      <Header title="WEB" onChangeMode={()=>{
        setMode('WELCOME');
      }}></Header>
      <Nav topics={topics} onChangeMode={(_id)=>{
        setMode('READ');
        setId(_id)
      }}></Nav>
      {content}
      <a href="/create" onClick={event=>{
        event.preventDefault();   // 클릭했을 때 URL이 바뀌지 않도록
        setMode('CREATE');    // Mode값이 CREATE로 바뀌고 App component가 다시 실행
      }}>Create</a>
    </div>
  );
}

export default App;
