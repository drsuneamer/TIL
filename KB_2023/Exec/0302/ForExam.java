package day01;

public class ForExam {

	public static void main(String[] args) {
		// 1 ~ 100까지 한줄출력
		for (int i=1; i<=100; i++) {
			System.out.print(i+" ");
			if (i % 10 == 0) {
				System.out.println();
			}
		}
	}

}
