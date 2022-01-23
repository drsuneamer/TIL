# Git

## Git?

- 분산 **버전 관리** 시스템 (DVCS, Distributed Version Control System)
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율

## 버전 관리

- 오픈소스 사례 (크로미움)

  - 최신 버전 소스코드 용량 1.58GB

  - 현재까지 백만여개의 버전

    -> 전체 용량은 얼마일까? : 25GB, 하나의 폴더

- 하나의 파일이지만 버전을 기록, 확인 (ex. google docs)
- Git을 활용한다면?
  - 버전들을 소프트웨어에 하나하나 기록
- 버전관리(VCS), 소스코드 관리(SCM)란 동일한 정보에 대한 여러 버전을 관리하는 것을 말한다
  - In software engineering, version control(also known as revision control, source control, or source code management) is a class of systems responsible for **managing changes to** computer programs, documents, large web sites, or other **collections of information**)

- CVCS vs DVCS
  - 중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용
  - 분산버전관리시스템은 원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유
    - 파일은 각자의 로컬 컴퓨터에서, 버전을 만들어서 공유 가능
    - 공유 단위가 파일이 아닌 버전



## Git bash

- 윈도우에서 Git을 활용하기 위한 기본 도구
- 프롬프트 기본 인터페이스
  - 컴퓨터 정보
  - 디렉토리
  - $

### CLI
  - CLI, 커맨드 라인 인터페이스 또는 명령어 인터페이스는 가상 터미널 또는 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식
  - 작업 명령은 사용자가 툴파 키보드 등을 통해 문자열의 형태로 입력
  - 인터페이스를 제공하는 프로그램을 명령 줄 해석기 또는 셸
    - 유닉스 셸(sh, ksh, csh, tcsh, bash 등)과 CP/M, 도스의 command.com("명령 프롬프트 등")
  - GUI - **그래픽** 기반의 인터페이스
    - Graphical User Interface
  - CLI - **명령** 기반의 인터페이스
    - Command Line Interface

- 명령을 제대로 했는지 확인하는 것이 매우 중요!

- Q. 인터페이스?

  ​	A. 접면, 점점 - 얼굴을 마주하고 있다!

  ​		GUI는 그래픽적인 접면을 지니고 있다

  ​		스마트폰은 터치 인터페이스를 지니고 있다

  ​		--> 패러다임의 변화! **행동 방식**을 바꾸어야 함

- *<u>내가 무엇인가를 알고 싶으면, 명령을 하고 그 결과를 읽어야 한다.</u>*

  

![image-20220121093227120](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220121093227120.png)

​		ls : list

​		mkdir : make directory

​		cd : change directory

​			-cd .. => 상위 폴더 / cd . => 지금 내가 있는 곳

​		pwd : 내가 지금 있는 곳의 전체 경로 (pin working directory)

​		rm : 삭제



## Git 기초 흐름

- Git 저장소 생성

  ```bash
  $ git init
  ```

  - 특정 폴더에 저장소(repository)를 만들어 관리
  
  - .git 폴더가 생성되며 (master)라는 표기를 확인할 수 있음
  
    

1. 작업을 하고

2. 변경된 파일을 모아 *(add)*

3. 버전으로 기록한다  *(commit)*

   

- Status - 상태 보기

  ```bash
  $ git status
  ```

  - Git 저장소의 변경된 파일의 상태를 확인하기 위하여 활용

  - 파일의 상태를 알 수 있음
    - 

- log 
- 



## 원격 저장소 활용

- 기본 흐름

- clone

  - 로컬 저장소가 없는 경우 원격 저장소를 복제하여 활용 가능

    ```bash
    $ git clone
    ```

- 로컬 저장소와 원격 저장소가 모두 있는 경우
  - pull : 원격 저장소의 커밋을 로컬 저장소로



# 파이썬을 활용한 데이터 수집

## 목표

- Python 기본 문법 실습

- 파일 입출력에 대한 이해

- 데이터 구조에 대한 분석과 이해

- 데이터를 가공하고 JSON 형태로 저장

  

## 프로젝트 안내

- JSON 데이터를 원하는 결과물로 반환



## 파일 입력

- open(file, more = 'r', encoding = None)
  - file : 파일명
  - mode : 텍스트 모드
  - encoding : 인코딩 방식 (일반적으로 utf-8 활용)



- 파일 입력 활용법

  - 파일 객체 활용

  - with 키워드 활용

    ![image-20220121110941019](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220121110941019.png)

    

## JSON

> Javascript Object Notation

- JSON은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함
- 문자 기반(텍스트) 데이터 포맷으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함
  - 텍스트를 언어별 타입으로 변환시키거나
  - 언어별 데이터 타입을 적절하게 텍스트로 변환

- 활용
  - 객체(리스트, 딕셔너리 등)를 JSON으로 변환
  - JSON을 객체(리스트, 딕셔너리 등)로 변환

## Pprint

- 임의의 파이썬 데이터 구조를 예쁘게 인쇄할 수 있는 기능을 제공



## 리스트 순회

- 이름만 출력하고 싶다면?
- 

## 딕셔너리 접근 방법

- dict.get(key, default)



## 프로젝트 제출 가이드

- 저장소 설정
  - GitLab 저장소 생성 및 담당 교수 maintainer 등록
  - 로컬 저장소 생성 및 README.me 추가 후 루트 커밋
  - GitLab 원격저장소 등록 및 push 테스트
- 과제 수행 및 제출
  - 수행 후 단계별 커밋
  - 과제 제출
    - 과제 제출시 반드시 README.md 파일에 수행 내용 작성 필수
