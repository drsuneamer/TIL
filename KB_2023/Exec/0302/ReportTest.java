package day01;

public class ReportTest {
	public static void main(String[] args) {
		String name;
		int korean, english, math, total;
		double average;
		char grade;
		
		// 데이터값 저장
		name = "sy";
		korean = 81;
		english = 70;
		math = 90;
		total = korean + english + math;
		// /3으로 하면 average가 double이어도 int/int라서 int로 저장 (.0 붙어서)
		average = total / 3.0;
		
		if (average >= 90) {
			grade = 'A';
		} else {
			grade = 'F';
		}
		
		// 삼항연산자 -> 조건식 ? 참 : 거짓
		grade = average >= 90 ? 'A' : 'F';
		
		System.out.println("이름: " + name);
		System.out.println("국어: " + korean);
		System.out.println("영어: " + english);
		System.out.println("수학: " + math);
		System.out.println("총점: " + total);
		System.out.println("평균: " + average);
		System.out.println("학점: " + grade);
		
		// 평균 소수점 두번째자리만 출력하고 싶을 때
		System.out.println((int)(average * 100) / 100.0);
	}

}
