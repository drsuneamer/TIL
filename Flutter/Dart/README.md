# Dart

> https://nomadcoders.co/dart-for-beginners
>
> Dart 온라인 실습 환경: https://dartpad.dev/

## 0. Introduction

Dart is a language Optimized for UI

Dart has 2 compilers

- dart web: javascript로 변환
- dart native: ARM64, x86_64 등 여러 CPU 아키텍처에 맞게 변환

AOT(Ahead-Of-Time)
JIT(Just-In-Time)

Dart는 개발 환경에서 VM을 이용하여 JIT로 바로 실행 결과 볼 수 있게 함. 이때는 코드가 가상 머신에서 작동하기 때문에 느리다
배포 시에는 AOT를 이용하여 컴파일된 파일이 더 빠르게 작동할 수 있게

null safety: 안전한 프로그램 위해 반영됨 (null 참조 오류 방지)

Flutter가 Dart를 채택한 이유

- JIT와 AOT가 모두 제공됨
- Flutter와 Dart 모두 구글에서 만들기 때문에, 서로 필요 시에 수정이 가능함 (cf. 리액트를 위해 JS를 수정할 수는 없음)

## 1. Variables

main 함수: 모든 Dart 프로그램의 Entry Point (반드시 작성 필요)

- class 등이 아닌 실제 작동 코드는 main 내부에 작성해야 함

세미콜론 필수!
(의도적으로 쓰지 않는 부분도 있긴 함 - 그래서 formatter에서 작성해주지 않음)

var

- 값 업데이트 할 때 타입 같아야 함

## 2. Data Types

String, Integer 등은 모두 class
num은 integer와 double의 부모 class이므로 둘 다에 사용 가능하다

dart에서는 모든 것이 class이다.
