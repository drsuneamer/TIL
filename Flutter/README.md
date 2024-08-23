why flutter?

- cross-platform (리눅스, 임베디드 등까지 가능)
- 구글도 현재 앱 개발에 사용 중이라 (구글 페이 등) 당장 사장될 기능은 아닐 것으로 보임
- flutterplasma.dev



How Flutter works

- 기존 swift 등은 버튼 등의 요소들 만들어달라고 운영체제에 직접 이야기함

- Flutter는 운영체제와 직접적으로 소통하지 않음
  - 위젯 등 보여지는 모든 것들은 호스트가 아닌 엔진이 그려내는 것
  - 그래서 부자연스럽게 느껴지기도 함
- Flutter framework는 애니메이션, 제스처 등 여러 요소 포함
- 크로스플랫폼을 위하여 - 운영체제와 직접 통신하는 대신 C나 C++로 짜인 엔진 사용
  - 엔진이 화면 상에 요청한 것 그려 줌
  - 엔진을 VM과 비슷한 느낌으로 생각해도 됨
- 플랫폼의 native widget 사용하지 않음
  - 엔진이 모든 것을 그려주기 때문
  - 운영체제는 엔진을 동작시키는 역할만 수행
  - 그래서 Navigation, 애니메이션 등을 직접적으로 통제하는 것이 용이함

* Embedder: 엔진을 가동시키는 runner 프로그램



Flutter vs React Native

- Flutter는 게임 엔진처럼 동작
  - 엔진이 화면 상의 모든 픽셀 그림

- 네이티브 앱 운영체제 상에서 가능한 위젯 사용하고 싶으면 RN
  - RN에서는 버튼 만들면 iOS와 안드로이드에서 서로 다르게 보임

- 세밀한 디자인 요구사항, 요소나 애니메이션 커스터마이징 필요한 경우 flutter
  - 커스텀된 Navbar, slider 등
  - ios나 android 앱처럼 보이지 않고 자유로운 커스터마이징 하기에 좋음

----



Flutter 프로젝트 시작

```bash
$ flutter create [pjtname]
$ cd [pjtname]
```



vscode extension 설치 : Dart, Flutter



---

widget: 레고 블럭과 같음

flutter에 있는 모든 것은 widget. widget을 조립해서 앱을 만든다

공식 widget도 많고 커뮤니티에 제작된 것도 많음



material / cupertino : root 앱의 두 선택지 (google/ios)

아무래도 구글이라 material이 더 보기 좋긴 함



scaffold: 화면의 구조 제공

모바일 앱의 모든 화면은 scaffold 필요



모든 widget은 class



---

Stateful widget



setState: State 클래스에게 데이터가 변경되었다고 알림

state가 바뀐다고 해서 무조건 재build하는 것은 아님. UI 바꾸지 않고 state만 바꾸는 것도 가능



context: 이전의 모든 요소들의 정보 가지고 있음 - 부모 요소에 접근할 수 있게 해 줌

!: 무조건 있을 테니 갖다 써라

?: 없을지도 모르겠는데?



initState: 상태 변수 초기화

- 부모 요소에 의존하는 상태 초기화할 때 좋음
- 무조건 build보다 먼저 호출되고, 단 한번만 호출돼야 함



dispose: 위젯이 스크린에서 제거될 때 호출되는 메서드

