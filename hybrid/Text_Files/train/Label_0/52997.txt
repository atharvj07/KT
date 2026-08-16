import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[]$) {
        int n = scanner.nextInt();
        long m = (long)n * (n + 1) / 2;
        long[] a = new long[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
            sum += a[i];
        }
        System.out.println(sum % m == 0 && f(a, n, sum / m) ? "YES" : "NO");
    }

    static boolean f(long[] a, int n, long k) {
        for (int i = 0; i < n; i++) {
            long b = a[i] - a[(i + 1) % n] + k;
            if (b < 0 || b % n != 0) {
                return false;
            }
        }
        return true;
    }
}