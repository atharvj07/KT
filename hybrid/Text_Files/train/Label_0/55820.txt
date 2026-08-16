import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskATCG004B solver = new TaskATCG004B();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskATCG004B {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int N = in.nextInt();
            int x = in.nextInt();

            int[] a = new int[N];
            for (int i = 0; i < N; i++) {
                a[i] = in.nextInt();
            }

            long minSum = 0;
            int m[] = new int[N];
            for (int i = 0; i < N; i++) {
                m[i] = a[i];
                minSum += m[i];
            }

            for (int k = 1; k <= N - 1; k++) {
                long sum = (long) k * x;

                for (int i = 0; i < N; i++) {
                    int p = (i - k) % N;
                    if (p < 0) p += N;

                    m[i] = Math.min(m[i], a[p]);
                    sum += m[i];
                }
                minSum = Math.min(sum, minSum);
            }
            out.println(minSum);
        }

    }
}
