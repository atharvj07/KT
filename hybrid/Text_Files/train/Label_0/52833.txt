import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Comparator;
import java.util.Collections;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author HBonsai
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        LIS solver = new LIS();
        solver.solve(1, in, out);
        out.close();
    }

    static class LIS {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = Integer.parseInt(in.next());
            int[] a = new int[n];
            Arrays.setAll(a, i -> Integer.parseInt(in.next()));
            Integer[] dp = new Integer[n + 1];
            final int INF = Integer.MAX_VALUE;
            Arrays.fill(dp, INF);
            List<Integer> dpList = Arrays.asList(dp);
            Comparator<Integer> lowerBound = (x, y) -> x.compareTo(y) >= 0 ? 1 : -1;
            for (int i = 0; i < n; i++) {
                int replaced = ~Collections.binarySearch(dpList, a[i], lowerBound);
                if (replaced >= 0) {
                    dp[replaced] = a[i];
                }
            }
            int ans = -1;
            for (int i = n; i >= 0; i--) {
                if (dp[i] < INF) {
                    ans = i + 1;
                    break;
                }
            }
            out.println(ans);
        }

    }
}


