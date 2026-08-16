
import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);


    public static void main(String[] args) {
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int count = 0;
        while (a % 2 == 0 && b % 2 == 0 && c % 2 == 0) {
            if (a == b && b == c) {
                System.out.println(-1);
                return;
            }
            count++;
            int tempA = a;
            int tempB = b;
            a = b / 2 + c / 2;
            b = tempA / 2 + c / 2;
            c = tempA / 2 + tempB / 2;
        }
        System.out.println(count);
    }
}
