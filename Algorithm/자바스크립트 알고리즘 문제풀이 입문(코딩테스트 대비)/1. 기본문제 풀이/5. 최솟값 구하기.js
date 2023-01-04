/*
7개의 수가 주어지면 그 숫자 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
*/

function solution(arr) {
	let answer,
		min = Number.MAX_SAFE_INTEGER;
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] < min) min = arr[i];
	}
	answer = min;
	return answer;
}

let arr = [5, 7, 1, 3, 2, 9, 11];
console.log(solution(arr));

// Number.MAX_SAFE_INTEGER: 안정적인 최대 정수값

// [보충] 내장함수로 최솟값, 최댓값 구하기

function solution(arr) {
	// 그냥 배열로 넘기면 안됨! 전개 연산자 사용
	let answer1 = Math.min(...arr);
	let answer2 = Math.max(...arr);

	// 전개 연산자 사용하지 않는 방법
	let answer = Math.min.apply(null, arr);
	return answer1, answer2;
}
