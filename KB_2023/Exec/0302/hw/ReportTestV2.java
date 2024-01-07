package HW0302;

public class ReportTestV2 {
    public static void main(String[] args) {
        String name;
        int korean, english, math, total;
        double average;
        char grade;

        name = "sy";
        korean = 81;
        english = 70;
        math = 90;
        total = korean + english + math;
        average = total / 3.0;

        if (average >= 90) {
            grade = 'A';
        } else if (average >= 80) {
            grade = 'B';
        } else if (average >= 70) {
            grade = 'C';
        } else if (average >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }

        System.out.println(grade);
    }
}
