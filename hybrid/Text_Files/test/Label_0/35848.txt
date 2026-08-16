import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.function.Function;

public class Main {

    public static void main(String[] args) {

        Parser parser = new Parser();
        int t = parser.parseInt();
        for (int i = 1; i <= t; i++) {
            Problem problem = new Problem();
            problem.solve(i);
        }
    }
}

class Problem {
    Parser parser = new Parser();

    private static final int MOD = 1_000_000_007;

    public void solve(int testNum) {
        int n = parser.parseInt();

        long[] x = new long[n];
        long[] counts = new long[62];

        long[] pows = new long[60];
        pows[0] = 1;
        for(int i = 1; i < 60; i++) {
            pows[i] = pows[i - 1] * 2;
        }

        for(int i = 0; i < n; i++) {
            x[i] = parser.parseLong();
            for (int j = 0; j < 60; j++) {
                if ((x[i] & pows[j]) > 0) {
                    counts[j] += 1;
                }
            }
        }

        long ans = 0;
        for(int i = 0; i < n; i++) {
            long v1 = 0;
            long v2 = 0;
            for(int j = 0; j < 60; j++) {
                long v3 = (pows[j] % MOD) % MOD;
                if((x[i] & pows[j]) > 0) {
                    v1 = (v1 + counts[j] * v3) % MOD;
                    v2 = (v2 + n * v3) % MOD;
                } else {
                    v2 = (v2 + counts[j] * v3) % MOD;
                }
            }
            ans = (ans + v1 * v2) % MOD;
        }
        System.out.println(ans);
    }

//    public void solve(int a) {
//        int n = parser.parseInt();
//
//        long[] x = new long[n];
//        for(int i = 0; i < n; i++) {
//            x[i] = parser.parseLong();
//        }
//
//        long ans = 0;
//        for(int i = 0; i < n; i++) {
//            for(int j = 0; j < n; j++) {
//                long v1 = (x[i] & x[j]);
//                long sum = 0;
//                for(int k = 0; k < n; k++) {
//                    long v2 = (x[j] | x[k]);
//                    sum += v2;
//                }
//                ans += v1 * sum;
////                System.out.println("v1 = " + v1 + " sum = " + sum);
//            }
//        }
//
//        System.out.println("ans: " + ans);
//    }
}

class MathUtil {

    public static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static long pow(long x, long y) {
        return pow(x, y, Function.identity());
    }

    public static long pow(long x, long y, long mod) {
        return pow(x, y, v -> v % mod);
    }

    private static long pow(long x, long y, Function<Long, Long> action) {
        long res = 1;
        long t = x;
        while (y > 0) {
            if ((y & 1) == 1) {
                res += t;
                res = action.apply(res);
            }
            t *= t;
            t = action.apply(t);
            y /= 2;
        }
        return res;
    }
}

class DisjointSet {

    private final int[] f;

    public DisjointSet(int size) {
        f = new int[size + 1];
        for (int i = 0; i <= size; i++) {
            f[i] = i;
        }
    }

    public int find(int u) {
        if (f[u] == u) return u;
        return f[u] = find(f[u]);
    }

    public boolean merge(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return false;
        if (u > v) {
            int t = u;
            u = v;
            v = t;
        }
        f[u] = v;
        return true;
    }
}

class Parser {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private StringTokenizer tokenizer;

    void fill() {
        while (tokenizer == null || !tokenizer.hasMoreElements()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    int parseInt() {
        fill();
        return Integer.parseInt(tokenizer.nextToken());
    }

    long parseLong() {
        fill();
        return Long.parseLong(tokenizer.nextToken());
    }

    double parseDouble() {
        fill();
        return Double.parseDouble(tokenizer.nextToken());
    }

    String parseString() {
        fill();
        return tokenizer.nextToken();
    }
}