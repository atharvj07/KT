import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[]$) {
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        long[] b = new long[n + 1];
        long[] w = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            int a = scanner.nextInt();
            if (a < 0) {
                b[i] = -a;
            } else {
                w[i] = a;
            }
        }
        Arrays.parallelPrefix(b, Long::sum);
        Arrays.parallelPrefix(w, Long::sum);
        long m = Long.MAX_VALUE;
        for (int i = k; i <= n; i++) {
            m = Math.min(m, Math.min(b[i] - b[i - k], w[i] - w[i - k]));
        }
        System.out.println(w[n] - m);
    }
}