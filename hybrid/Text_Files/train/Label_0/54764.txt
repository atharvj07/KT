import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

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
        RGBTriplets solver = new RGBTriplets();
        solver.solve(1, in, out);
        out.close();
    }

    static class RGBTriplets {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            char[] strings = in.next().toCharArray();

            long r = 0;
            long g = 0;
            long b = 0;
            for (int i = 0; i < n; i++) {
                if (strings[i] == 'R') {
                    r++;
                }
                if (strings[i] == 'G') {
                    g++;
                }
                if (strings[i] == 'B') {
                    b++;
                }
            }
            long all = r * g * b;
            long sub = 0;
            for (int i = 0; i < n; i++) {
                char ci = strings[i];

                for (int j = i + 1; j < n; j++) {
                    char cj = strings[j];
                    if (ci == cj) {
                        continue;
                    }
                    int k = 2 * j - i;
                    if (n <= k) {
                        continue;
                    }

                    char ck = strings[k];
                    if (ci == ck || cj == ck) {
                        continue;
                    }
                    sub++;
                }
            }

            out.append(String.valueOf(all - sub));
        }

    }
}

