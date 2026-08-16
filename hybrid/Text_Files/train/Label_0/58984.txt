import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author silviase
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BK solver = new BK();
        solver.solve(1, in, out);
        out.close();
    }

    static class BK {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int k = in.nextInt();
            int n = in.nextInt();
            int[] a = new int[n];
            int max = 0;
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
                max = Math.max(max, a[i]);
            }

            out.println(Math.max(0, (max - (k + 1) / 2) * 2 - 1 + k % 2));

        }

    }
}

