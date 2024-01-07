package HW0302;

public class ReportTestV3 {
    public static void main(String[] args) {
        String name;
        int korean, english, math, total;
        double average;
        char grade;

        name = "sy";
        korean = 90;
        english = 90;
        math = 90;
        total = korean + english + math;
        average = total / 3.0;

        switch ((int)average / 10) {
            case 9: grade = 'A'; break;
            case 8: grade = 'B'; break;
            case 7: grade = 'C'; break;
            case 6: grade = 'D'; break;
            default: grade = 'F';
        }

        System.out.println(grade);
    }
}
