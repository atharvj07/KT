import java.io.*;
import java.util.*;

public class Test {
    int readInt() {
        int ans = 0;
        boolean neg = false;
        try {
            boolean start = false;
            for (int c = 0; (c = System.in.read()) != -1; ) {
                if (c == '-') {
                    start = true;
                    neg = true;
                    continue;
                } else if (c >= '0' && c <= '9') {
                    start = true;
                    ans = ans * 10 + c - '0';
                } else if (start) break;
            }
        } catch (IOException e) {
        }
        return neg ? -ans : ans;
    }

    final int N = 1_000_001, B = 20;
    int M = 1_000_000_007;
    int r, n;
    long ans;
    int[][] tab = new int[N][B];
    int[] p = new int[N];

    PrintWriter writer = new PrintWriter(System.out);

    void start() {
        Arrays.fill(tab[0], 2);
        tab[0][0] = 1;
        for (int i = 1; i < N; i++) {
            int sum = 0;
            for (int j = 0; j < B; j++) {
                sum += tab[i-1][j];
                if (sum >= M) sum -= M;
                tab[i][j] = sum;
            }
        }
        for (int i = 1; i < N; i++) p[i] = i;
        for (int i = 2; i < N; i++)
            if (p[i] == i) {
                for (int j = i + i; j < N; j += i) p[j] = i;
            }

        int q = readInt();
        while (q-- > 0) {
            r = readInt();
            n = readInt();
            ans = 1;
            while (n > 1) {
                int c = 0;
                int d = p[n];
                while (n % d == 0) {
                    n /= d;
                    c++;
                }
                ans = (ans*tab[r][c]) % M;
            }
            writer.println(ans);
        }
        writer.flush();
    }

    public static void main(String[] args) {

        new Test().start();

    }
}
