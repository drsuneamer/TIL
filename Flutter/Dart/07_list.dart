void main() {
  var nums1 = [
    1,
    2,
    3,
    4, // 마지막에 쉼표 넣으면 여러 줄로 포매팅 가능
  ];
  List<int> nums2 = [1, 2, 3, 4];
  nums2.add(5);

  nums1.first; // 첫 번째 요소

  // collection if : 존재할 수도, 안 할 수도 있는 변수로 리스트 생성 가능
  var five = true;
  var ifFive = [
    1,
    2,
    3,
    4,
    if (five) 5, // five가 true인 경우 5가 추가됨
  ];

  // collection for
  var olds = ['N', 'B'];
  var news = [
    'J',
    'K',
    for (var o in olds) "👽$o",
  ];

  print(news);
  // 출력 결과: [J, K, 👽N, 👽B]
}
