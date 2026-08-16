import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.*;

class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Task solver = new Task();
        solver.solve(in, out);
        out.close();
    }

    static class Task {
        static int A, B, Q;
        static long[] S, T;

        int lowerBound(long x, long[] arr) {
           int low = 0, high = arr.length;
           while (low < high - 1) {
               int mid = (low + high) / 2;
               if (x <= arr[mid]) {
                   high = mid;
               } else if (x > arr[mid]) {
                   low = mid;
               }
           }
           return arr[low] < x ? high : low;
        }

        long shortest(long x, long[] arr) {
            int idx = lowerBound(x, arr);
            if (idx == 0) {
                return Math.abs(x - arr[idx]);
            } else if (idx == arr.length) {
                return Math.abs(x - arr[idx - 1]);
            } else {
                return Math.min(Math.abs(x - arr[idx]), Math.abs(x - arr[idx - 1]));
            }
        }

        long templeShrine(long x) {
            long d = Long.MAX_VALUE;
            int idx = lowerBound(x, T);

            if (idx < T.length) d = Math.min(d, Math.abs(T[idx] - x) + shortest(T[idx], S));
            if (idx > 0) d = Math.min(d, Math.abs(T[idx - 1] - x) + shortest(T[idx - 1], S));

            return d;
        }

        long shrineTemple(long x) {
            long d = Long.MAX_VALUE;
            int idx = lowerBound(x, S);

            if (idx < S.length) d = Math.min(d, Math.abs(S[idx] - x) + shortest(S[idx], T));
            if (idx > 0) d = Math.min(d, Math.abs(S[idx - 1] - x) + shortest(S[idx - 1], T));

            return d;
        }

        void solve(InputReader in, PrintWriter out) {
            A = in.nextInt();
            B = in.nextInt();
            Q = in.nextInt();
            S = new long[A];
            T = new long[B];

            for (int i = 0; i < A; i++) {
                S[i] = in.nextLong();
            }

            for (int i = 0; i < B; i++) {
                T[i] = in.nextLong();
            }

            for (int i = 0; i < Q; i++) {
                long x = in.nextLong();
                out.println(Math.min(shrineTemple(x), templeShrine(x)));
            }
        }
    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }

        long nextLong() { return Long.parseLong(next()); }

    }
}
