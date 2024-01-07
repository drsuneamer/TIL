package HW0302;

public class DoWhileExamV2 {
    public static void main(String[] args) {
        int i = 0;
        int j = 1;
        do {
            do {
                int k = i * 10 + j;
                System.out.print(k + " ");
                if (k % 10 == 0) {
                    System.out.println();
                }
                j++;
            } while (j <= 10);
            i++;
            j = 1;
        } while (i <= 9);

    }
}
