import java.io.*;
import java.util.*;
import static java.lang.System.out;

public class Main {
    static MyReader in = new MyReader();

    public static void main(String[] args) {
        int N = in.i();
        int[] A = in.ii(N);
        String ans;
        if (gcd(A) > 1) {
            ans = "not coprime";
        } else {
            ans = "pairwise coprime";
            int max = max(A);
            int[] D = new int[max + 1];
            for (int i = 2; i < D.length; i++) {
                if (D[i] == 0) {
                    for (int j = 1; i * j < D.length; j++) {
                        D[i * j] = i;
                    }
                }
            }
            HashSet<Integer> hs = new HashSet<>();
            loop: for (int i = 0; i < A.length; i++) {
                int a = A[i];
                while (a > 1) {
                    int x = D[a];
                    if (hs.add(x)) {
                        while (a % x == 0) {
                            a /= x;
                        }
                    } else {
                        ans = "setwise coprime";
                        break loop;
                    }
                }
            }
        }

        out.println(ans);
    }

    static int gcd(int a, int b) {
        int r;
        while ((r = a % b) != 0) {
            a = b;
            b = r;
        }
        return b;
    }

    static int gcd(int... a) {
        int g = a[0];
        for(int i = 1; i < a.length; i++){
            g = gcd(g, a[i]);
        }
        return g;
    }

    static int max(int... a) {
        int m = a[0];
        for (int i = 1; i < a.length; i++) {
            m = Math.max(m, a[i]);
        }
        return m;
    }
}

class MyReader extends BufferedReader {
    char[] cbuf = new char[1024];
    int head = 0;
    int tail = 0;

    MyReader() {
        super(new InputStreamReader(System.in));
    }

    char next() {
        if (head == tail) {
            try {
                tail = read(cbuf, 0, cbuf.length);
            } catch (IOException e) {}
            head = 0;
        }
        return cbuf[head++];
    }

    void back() {
        head--;
    }

    boolean minus() {
        boolean minus;
        while (true) {
            char c = next();
            if (c != ' ' && c != '\n' && c != '\r') {
                if (!(minus = c == '-')) back();
                return minus;
            }
        }
    }

    void skip() {
        while (true) {
            char c = next();
            if (c != ' ' && c != '\n' && c != '\r') {
                back();
                break;
            }
        }
    }

    char[] s(final int N) {
        skip();
        char[] s = new char[N];
        for (int i = 0; i < s.length; i++) {
            s[i] = next();
        }
        return s;
    }

    String s() {
        try {
            return readLine();
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    int i() {
        boolean minus = minus();
        int n = 0;
        while (true) {
            int k = next() - '0';
            if (k < 0 || 9 < k) break;
            n = 10 * n + k;
        }
        return minus ? -n : n;
    }

    int[] ii(final int N) {
        int[] a = new int[N];
        for (int j = 0; j < a.length; j++) a[j] = i();
        return a;
    }

    long l() {
        boolean minus = minus();
        long n = 0;
        while (true) {
            int k = next() - '0';
            if (k < 0 || 9 < k) break;
            n = 10 * n + k;
        }
        return minus ? -n : n;
    }
}
