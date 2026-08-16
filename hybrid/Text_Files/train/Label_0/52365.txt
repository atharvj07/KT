import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.util.Comparator;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Bamboo solver = new Bamboo();
        solver.solve(1, in, out);
        out.close();
    }

    static class Bamboo {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int N = in.nextInt();
            long k = in.nextLong();
            int[] arr = new int[N];
            ArrayList<int[]> div = new ArrayList<>();
            long sumA = 0;
            long dA = 0;
            for (int i = 0; i < N; i++) {
                arr[i] = in.nextInt();
                sumA += arr[i];
                dA += arr[i];
                arr[i]--;
                for (int d = 2; d <= arr[i]; d = (arr[i] / (arr[i] / d)) + 1) {
                    div.add(new int[]{d, i});
                }
                if (arr[i] != 0) {
                    div.add(new int[]{arr[i] + 1, i});
                }
            }
            Collections.sort(div, new Comparator<int[]>() {

                public int compare(int[] ints, int[] t1) {
                    return Integer.compare(ints[0], t1[0]);
                }
            });
            long max = (k + sumA) / dA;
            for (int[] d : div) {
                dA -= (arr[d[1]]) / (d[0] - 1) - arr[d[1]] / (d[0]);
                long largest = (k + sumA) / dA;
                if (largest >= d[0]) {
                    max = Math.max(largest, max);
                }
            }
            out.println(max);
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
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
}

