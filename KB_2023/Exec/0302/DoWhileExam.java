package day01;

public class DoWhileExam {

	public static void main(String[] args) {
		// 1 ~ 100 10행 10열
		int i = 1;
		do {
			System.out.print(i+" ");
			if (i % 10 == 0) {
				System.out.println();
			}
			i++;
		} while (i <= 100);

	}

}
