import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
//        InputStream inputStream = new FileInputStream("sum.in");
        OutputStream outputStream = System.out;
//        OutputStream outputStream = new FileOutputStream("sum.out");

        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Answer solver = new Answer();
        solver.solve(in, out);
        out.close();
    }
}

class Answer {
    private final int INF = (int) (1e9 + 7);
    private final int MOD = (int) (1e9 + 7);
    private final int MOD1 = (int) (1e6 + 3);
    private final long INF_LONG = (long) (1e18 + 1);
    private final double EPS = 1e-9;

    private long gcd(long a, long b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

    private long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }

    private boolean tmp1(int[] a, int l, int r) {
        int i = l;
        while (i <= r) {
            if (a[i] != a[l]) {
                return false;
            }
            i++;
        }
        return true;
    }

    private boolean test1(int[] a) {
        return tmp1(a, 0, 3) && tmp1(a, 8, 11)
                || tmp1(a, 12, 15) && tmp1(a, 16, 19)
                || tmp1(a, 4, 7) && tmp1(a, 20, 23);
    }

    private boolean test2(int[] a) {
        return tmp1(a, 0, 3) && tmp1(a, 8, 11)
                && tmp1(a, 12, 15) && tmp1(a, 16, 19)
                && tmp1(a, 4, 7) && tmp1(a, 20, 23);
    }

    private int[] sdvig(int[] t, boolean isLeft) {
        int[] a = Arrays.copyOf(t, t.length);

        if (isLeft) {
            int x = a[0];
            int y = a[1];

            for (int i = 0; i < a.length - 2; i++) {
                a[i] = a[i + 2];
            }
            a[a.length - 2] = x;
            a[a.length - 1] = y;
        } else {
            int x = a[a.length - 2];
            int y = a[a.length - 1];
            for (int i = a.length - 1; i > 1; i--) {
                a[i] = a[i - 2];
            }
            a[0] = x;
            a[1] = y;
        }
        return a;
    }

    private boolean tmp3(int[] a, int[] b) {
        for (int i = 0; i < a.length; i += 2) {
            if (a[i] != b[i] || a[i] != a[i + 1] || b[i] != b[i + 1]) {
                return false;
            }
        }
        return true;
    }

    private boolean test3(int[] a, int[] b) {

        int[] t = sdvig(a, false);
        if (tmp3(t, b)) {
            return true;
        }

        t = sdvig(a, true);
        if (tmp3(t, b)) {
            return true;
        }

        t = sdvig(b, false);
        if (tmp3(a, t)) {
            return true;
        }

        t = sdvig(b, true);

        return tmp3(a, t);
    }

    public void solve(InputReader in, PrintWriter out) throws IOException {
        int[] a = in.nextArrayInt(24);

        if (!test1(a)) {
            out.print("NO");
            return;
        }

        if (test2(a)) {
            out.print("NO");
            return;
        }

        int[] index1_1 = {12, 13, 4, 5, 16, 17, 20, 21};
        int[] index1_2 = {14, 15, 6, 7, 18, 19, 22, 23};

        int[] index2_1 = {0, 2, 4, 6, 8, 10, 21, 23};
        int[] index2_2 = {1, 3, 5, 7, 9, 11, 20, 22};

        int[] index3_1 = {0, 1, 17, 19, 10, 11, 12, 14};
        int[] index3_2 = {2, 3, 16, 18, 8, 9, 13, 15};

        if (tmp1(a, 0, 3) && tmp1(a, 8, 11)) {
            int[] a1 = new int[8];
            int[] a2 = new int[8];
            for (int i = 0; i < a1.length; i++) {
                a1[i] = a[index1_1[i]];
                a2[i] = a[index1_2[i]];
            }

            if (test3(a1, a2)) {
                out.print("YES");
            } else {
                out.print("NO");
            }
            return;
        }

        if (tmp1(a, 12, 15) && tmp1(a, 16, 19)) {
            int[] a1 = new int[8];
            int[] a2 = new int[8];
            for (int i = 0; i < a1.length; i++) {
                a1[i] = a[index2_1[i]];
                a2[i] = a[index2_2[i]];
            }

            if (test3(a1, a2)) {
                out.print("YES");
            } else {
                out.print("NO");
            }
            return;
        }

        int[] a1 = new int[8];
        int[] a2 = new int[8];
        for (int i = 0; i < a1.length; i++) {
            a1[i] = a[index3_1[i]];
            a2[i] = a[index3_2[i]];
        }

        if (test3(a1, a2)) {
            out.print("YES");
        } else {
            out.print("NO");
        }
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    InputReader(InputStream stream) {
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

    public int[] nextArrayInt(int count) {
        int[] a = new int[count];
        for (int i = 0; i < count; i++) {
            a[i] = nextInt();
        }
        return a;
    }

    public long[] nextArrayLong(int count) {
        long[] a = new long[count];
        for (int i = 0; i < count; i++) {
            a[i] = nextLong();
        }
        return a;
    }
}
