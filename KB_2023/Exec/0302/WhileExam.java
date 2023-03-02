package day01;

public class WhileExam {

	public static void main(String[] args) {
		// 1 ~ 100까지 10행 10열
		int i = 1;
		while (i <= 100) {
			System.out.print(i+" ");
			if (i % 10 == 0) {
				System.out.println();
			}
			i++;
		}

	}

}
