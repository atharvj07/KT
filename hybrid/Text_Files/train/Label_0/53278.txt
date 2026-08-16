import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.HashMap;

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
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            final Map<Integer, Integer> r = new HashMap<>();
            final int n = in.nextInt();
            for (int i = 0; i < n; i++) {
                int f = in.nextInt();
                int s = in.nextInt();
                r.put(f, s);
            }

            final int m = in.nextInt();
            for (int j = 0; j < m; j++) {
                int f = in.nextInt();
                int s = in.nextInt();

                if (r.containsKey(f)) {
                    int v = r.get(f);
                    if (v < s) {
                        r.put(f, s);
                    }
                } else {
                    r.put(f, s);
                }
            }

            long v = 0L;
            for (Map.Entry<Integer, Integer> entry : r.entrySet()) {
                v += entry.getValue();
            }

            System.out.printf("%d\n", v);
        }

    }
}

