/*
  길이가 서로 다른 A, B, C 세 개의 막대 길이가 주어지면
  이 세 막대로 삼각형을 만들 수 있으면 "YES"를 출력하고, 만들 수 없으면 "NO"를 출력한다.
*/

function solution(a, b, c) {
	let answer = "YES",
		sum = a + b + c,
		max;

	// 가장 큰 막대의 값 구하기
	if (a > b) max = a;
	else max = b;
	if (c > max) max = c;

	// 전체에서 가장 큰 값을 뺀 나머지 값과 비교하기
	if (sum - max <= max) answer = "NO";

	return answer;
}

console.log(solution(6, 7, 11)); // YES
console.log(solution(13, 33, 17)); // NO
console.log(solution(5, 5, 10));

/*
  TIP)
  삼각형이 만들어지려면 가장 긴 막대를 뺀 나머지 두 개의 합이
  가장 긴 막대의 길이보다 커야한다.
*/
