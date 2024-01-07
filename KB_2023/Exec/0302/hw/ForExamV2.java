package HW0302;

public class ForExamV2 {
    public static void main(String[] args) {
        // 이중 for문 이용 1 ~ 100
        for (int i = 0; i <= 9; i++) {
            for (int j = 1; j <= 10; j++) {
                int k = 10 * i + j;
                System.out.print(k + " ");
                if (k % 10 == 0) {
                    System.out.println();
                }
            }
        }
    }
}
