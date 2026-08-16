import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.io.*;
import java.util.*;
import java.util.regex.Matcher;

public class Main {

    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = /*new InputReader(new FileReader("input.txt"));*/   new InputReader(inputStream);
        PrintWriter out = /*new PrintWriter("output.txt"); */  new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(in, out);
        out.close();
    }

    private static class TaskB {

        static final long max = 1000000000000000000L;
        static final double eps = 0.000000001;
        static final long mod = 1000000007;

        void solve(InputReader in, PrintWriter out) throws IOException {

            int N = in.nextInt();
            int A = in.nextInt();
            int B = in.nextInt();
            int C = in.nextInt();

            int count = 0;
            for (int i = 0; i <= B; i++)
                for (int j = 0; j <= C; j++) {
                    int sum = i + j * 2;
                    if (sum == N) {
                        count++;
                    } else if (sum < N) {
                        int rem = N - sum;
                        if (rem * 2 <= A) count++;
                    }
                }

            out.println(count);

        }
    }

    private static class InputReader {
        StringTokenizer st;
        BufferedReader br;

        public InputReader(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public InputReader(FileReader s) throws FileNotFoundException {
            br = new BufferedReader(s);
        }

        public String next() {
            while (st == null || !st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public String nextLine() {
            try {
                return br.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public boolean ready() {
            try {
                return br.ready();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
}