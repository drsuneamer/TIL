package HW0302;

public class WhileExamV2 {
    public static void main(String[] args) {
        // 이중 while문
        int i = 0;
        int j = 1;
        while (i <= 9) {
            while (j <= 10) {
                int k = i * 10 + j;
                System.out.print(k + " ");
                if (k % 10 == 0) {
                    System.out.println();
                }
                j++;
            }
            i++;
            j = 1;
        }
    }
}
