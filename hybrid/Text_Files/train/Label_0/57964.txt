import java.util.Scanner;

class Main {
    private static int dp[];

    private static int cost(int i, int w, int[] a) {
        int result;
        if (i == a.length) {
            result = 0;
        } else if (dp[i] > 0) {
            result = dp[i];
        } else {
            int s = 0;
            int j = i;
            for (; j < a.length && a[j] <= w - s; j++) {
                s += a[j];
            }
            if (s == w) {
                result = cost(j, w, a);
            } else if (j == a.length) {
                result = 0;
            } else {
                result = Math.min(cost(j, w, a) + w - s, cost(j + 1, w, a) + s + a[j] - w);
            }
            dp[i] = result;
        }
        return result;
    }

    private static void solve() {
        final Scanner scanner = new Scanner(System.in);

        for (int i = 1; ; i++) {
            final int n = scanner.nextInt();
            final int w = scanner.nextInt();
            if (n == 0 && w == 0) {
                break;
            }
            final int a[] = new int[n];
            for (int j = 0; j < n; j++) {
                a[j] = scanner.nextInt();
            }
            dp = new int[n];
            System.out.println(String.format("Case %d: %d", i, cost(0, w, a)));
        }
    }

    public static void main(String... args) {
        solve();
    }
}