import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        long n = stdin.nextLong();
        long a = stdin.nextLong();
        long b = stdin.nextLong();
        long c = stdin.nextLong();
        long d = stdin.nextLong();
        for (long i = 0; i < n; i++) {
            long max = a + i * d - (n - 1 - i) * c;
            long min = a + i * c - (n - 1 - i) * d;
            if (min <= b && b <= max) {
                System.out.println("YES");
                System.exit(0);
            }
        }
        System.out.println("NO");
    }
}
