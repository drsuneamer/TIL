package HW0302;

public class Star {
    public static void main(String[] args) {
        String star = "";
        for (int i = 1; i <= 5; i++) {
            star += '★';
            System.out.println(star);
        }
        System.out.println("************************");
        for (int i = 5; i >= 1; i--) {
            star = "";
            for (int j = i; j > 0; j--)
                star += '★';
            System.out.println(star);
        }
        System.out.println("************************");
        for (int i = 1; i <= 5; i++) {
            star = "";
            for (int j = 0; j < 5 - i; j++) {
                star += " ";
            }
            for (int j = 0; j < i; j++) {
                star += '★';
            }
            System.out.println(star);
        }
        System.out.println("************************");
        for (int i = 1; i <= 5; i++) {
            star = "";
            for (int j = 0; j < i; j++) {
                star += " ";
            }
            for (int j = 0; j <= 5 - i; j++) {
                star += '★';
            }
            System.out.println(star);
        }
    }
}
