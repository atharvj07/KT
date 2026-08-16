import java.util.Scanner;

/**
 * Created by user on 06.01.2017.
 */
public class A9 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int max;
        if (x > y) {
            max = x;
        } else max = y;
        int l = 6 - max + 1;
        if (6 % l == 0) {
            System.out.println(1 + "/" + 6/l);
        } else if (l == 4) {
            System.out.println(2 + "/" + 3);
        } else
            System.out.println(l + "/" + 6);
    }
}
