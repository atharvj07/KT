import java.util.Scanner;

public class TaskA {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[] firstName = in.next().toCharArray();
        char[] lastName = in.next().toCharArray();

        String res = "" + firstName[0];
        for (int i = 1; i < firstName.length; i++) {
            if (firstName[i] < lastName[0]) {
                res += firstName[i];
            } else {
                res += lastName[0];
                System.out.println(res);
                return;
            }
        }

        res += lastName[0];
        System.out.println(res);
    }
}
