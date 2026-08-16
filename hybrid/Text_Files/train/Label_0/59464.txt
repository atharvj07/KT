import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[]$) {
        int n = scanner.nextInt();
        for (double i = 1; i <= 3500; i++) {
            for (double j = 1; j <= 3500; j++) {
                double k = n * i * j / (4 * i * j - n * i - n * j);
                if (k > 0 && k % 1 == 0) {
                    System.out.println((long)i + " " + (long)j + " " + (long)k);
                    return;
                }
            }
        }
    }
}