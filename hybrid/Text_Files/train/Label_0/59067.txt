import java.io.*;
import java.util.*;

public class Main {

    private static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException exp) {
                    throw new RuntimeException(exp);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }

    public static void main(String[] args) {    //throws FileNotFoundException {
        InputStream inputStream = System.in;    //new FileInputStream("input.txt");
        OutputStream outputStream = System.out; //new FileOutputStream("output.txt");
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        Task newTask = new Task();
        newTask.solve(in, out);

        out.close();
    }

    private static class Task {
        //.constant
        private final int INF = Integer.MAX_VALUE;
        private final int MOD = (int)1e9 + 7;

        //.data
        private int[] t = new int[101];
        private int[] v = new int[101];
        private int[] maxv = new int[101];

        //.code
        public void solve(InputReader in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 0; i < n; ++i) {
                t[i] = in.nextInt();
            }
            for (int i = 0; i < n; ++i) {
                v[i] = in.nextInt();
            }

            for (int i = n - 1; i > 0; --i) {
                int minV = Math.min(v[i - 1], v[i]);
                maxv[i] = minV - maxv[i + 1] <= t[i] ? minV : maxv[i + 1] + t[i];
            }

            double s = 0;
            double curV = 0;
            for (int i = 0; i < n; ++i) {
                double nextV = Math.min(curV + t[i], maxv[i + 1]);
                double diffV = Math.abs(nextV - curV);
                double c = Math.abs(t[i] - diffV);
                s += c * Math.max(curV, nextV) + diffV * Math.min(curV, nextV) + diffV * diffV / 2.0;
                if (c / 2.0 + Math.max(curV, nextV) > v[i]) {
                    double h = v[i] - Math.max(curV, nextV);
                    s += h * (c - h);
                } else {
                    s += c * c / 4.0;
                }
                curV = nextV;
            }

            out.println(s);

        }//end

    }

}