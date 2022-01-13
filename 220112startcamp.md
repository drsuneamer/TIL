# 220112 start camp

git과 관련된 모든 명령은 git init(enter)로 시작

.git이라는 숨김 폴더 생성됨

git이 여기에 모든 정보를 저장할 거지만 우리는 신경 쓰지 않는다!



## git

> 분산 버전 관리 시스템(DVCS)

1. git 저장소 만들기

```bash
$ git init
Initialized empty Git repository in C:/Users/drsuneamer/Desktop/first/.git/

```

- `.git`이라는 폴더 생성 -> 버전이 기록되는 저장소
  - 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의!

- `(master)` 

- 화면 초기화: `Ctrl + l`



## 버전 기록하기

### add

> add file contents to the index

```bash
$ git add 파일명
$ git add a.txt
$ git add my_folder
$ git add a.txt b. txt (여러 개의 파일도 가능)
```

### commit

> Record changes to the repository

```bash
$ git commit -m '커밋메시지'
```

- 커밋 메시지는 항상 버전의 내용(변경사항)에 대해서 나타낼 수 있도록 기록한다.

Q. 왜 굳이 add와 commit 두 개의 과정을 거쳐야 할까?

​	working directory(working tree) / staging area(index) / repository(commit 기록)



## status

```bash
$ git status

# 커밋할 변경사항들 (staging area)
Changes to be committed:
	(use "git restore --staged <file>..." to unstage)
		deleted: b.txt
	
# 커밋을 위한 준비가 되지 않은 변경 사항 (not in staging area -> in working directory)
Changes not staged for commit:
	(use "git add <file>..." to update what will be committed)
	(use "git restore <file>..." to discard changes in working directory)
		modified: a.txt

# 트래킹되지 않은 파일들 (working directory) not even been added at all
Untracked files:
	(use "git add <file>..." to include in what will be committed)
		c.txt
```



- 파일을 조작하는 방법이 총 4 가지
  - 생성 Create	
  - ~~읽기 Read~~
  - 수정 Update
  - 삭제 Delete



### git 파일의 라이프사이클

- untracked: 커밋에 포함된 적 없는 파일
- tracked
  - modified: 이전 커밋에 비해 수정된 경우
  - staged: 커밋 되기 전 목록에 있음 (staging area)
  - committed: commit된 (이후로 어떠한 변화도 없는) 상태



![image-20220113102109045](220112 start camp.assets/image-20220113102109045-16420368709841.png)

![image-20220113102153432](220112 start camp.assets/image-20220113102153432-16420369145762.png)



## log

> show commit logs

```bash
$ git log
```

