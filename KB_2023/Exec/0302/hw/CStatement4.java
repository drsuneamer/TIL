package HW0302;

public class CStatement4 {
    public static void main(String[] args) {
        int num = 0;
        while (num != 5) {
            int a = (int)(Math.random() * 6 + 1);
            int b = (int)(Math.random() * 6 + 1);
            num = a + b;
        }
    }
}
