
import java.util.*;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a <= 2 * b) {
            if (c % 1000 != 0) {
                if (c % 1000 <= 500 && b <= a) {
                    System.out.println(a * (c / 1000) + b);
                } else {
                    System.out.println(a * (c / 1000) + a);
                }
            } else {
                System.out.println(a * (c / 1000));
            }
        } else {
            if (c % 500 == 0) {
                System.out.println(c / 500 * b);
            } else {
                System.out.println(c / 500 * b + b);
            }
        }
    }
}

