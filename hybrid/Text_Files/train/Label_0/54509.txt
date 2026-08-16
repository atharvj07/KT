import java.util.*;

public class Main implements Runnable {

    private static int MOD = 1_000_000_007;

    public static void main(String[] args) {
        // Run with 32MB stack
        Thread thread = new Thread(null, new Main(), "", 32 * 1024 * 1024);
        thread.start();
    }

    @Override
    public void run() {
        final Scanner scanner = new Scanner(System.in);
        solve(scanner);
    }

    static void solve(Scanner scanner) {
        int N = Integer.parseInt(scanner.next());
        int A[] = new int[N];
        for (int i = 0; i < N; i++) {
            A[Integer.parseInt(scanner.next()) - 1]++;
        }
        Arrays.sort(A);

        int S[] = new int[N + 1];
        for (int i = 0; i < N; i++) {
            S[i + 1] = S[i] + A[i];
        }

        for (int k = 1; k <= N; k++) {
            int l = 0; // ok
            int r = N / k + 1; // ng
            while (r - l > 1) {
                int mid = (l + r) >>> 1;
                int index = lowerBound(A, 0, A.length, mid);
                int sum = mid * (N - index) + S[index];
                if (sum >= mid * k) {
                    l = mid;
                } else {
                    r = mid;
                }
            }
            System.out.println(l);
        }

    }

    // return first index whose value is more than or equal to val;
    static int lowerBound(int[] A, int fromInc, int toExc, int val) {
        int left = fromInc, right = toExc;
        while (right - left > 1) {
            int mid = (left + right) >>> 1;
            if (A[mid] < val) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (A[left] < val) {
            return left + 1;
        }
        return left;
    }

}
