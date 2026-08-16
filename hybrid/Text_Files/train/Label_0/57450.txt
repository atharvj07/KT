import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Random;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author MaxHeap
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastReader in = new FastReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskA {
        public void solve(int testNumber, FastReader in, PrintWriter out) {
            int n = in.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            TaskA.Can[] cans = new TaskA.Can[n];
            long sum = 0;
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
                sum += a[i];
            }
            for (int i = 0; i < n; i++) {
                b[i] = in.nextInt();
            }
            if (n <= 2) {
                out.println("YES");
                return;
            }
            ArrayUtils.sort(b);
            if (sum <= b[n - 2] + b[n - 1]) {
                out.println("YES");
            } else {
                out.println("NO");
            }
        }

        static class Can implements Comparable<TaskA.Can> {
            int cap;
            int value;

            public Can(int cap, int value) {
                this.cap = cap;
                this.value = value;
            }


            public int compareTo(TaskA.Can o) {
                return Integer.compare(value, o.value);
            }

        }

    }

    static class ArrayUtils {
        public static void sort(int[] arr) {
            int n = arr.length;
            Random r = new Random();
            for (int i = 0; i < n; i++) {
                int p = r.nextInt(n + 1);
                if (p < n) {
                    int temp = arr[i];
                    arr[i] = arr[p];
                    arr[p] = temp;
                }
            }
            Arrays.sort(arr);
        }

    }

    static class FastReader {
        BufferedReader reader;
        StringTokenizer st;

        public FastReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            st = null;
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String line = reader.readLine();
                    if (line == null) {
                        return null;
                    }
                    st = new StringTokenizer(line);
                } catch (Exception e) {
                    throw new RuntimeException();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

