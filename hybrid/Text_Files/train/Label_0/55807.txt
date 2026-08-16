import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Queue;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

import static java.util.Arrays.fill;

/**
 * Created by timur on 28.03.15.
 */

public class TaskD {
    boolean eof;
    BufferedReader br;
    StringTokenizer st;
    PrintWriter out;

    public static void main(String[] args) throws IOException {
        new TaskD().run();
    }

    public String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return "-1";
            }
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(nextToken());
    }

    public long nextLong() {
        return Long.parseLong(nextToken());
    }

    double nextDouble() {
        return Double.parseDouble(nextToken());
    }

    String nextLine() throws IOException {
        return br.readLine();
    }


    void run() throws IOException {
        InputStream input = System.in;
        PrintStream output = System.out;
        try {
            File f = new File("a.in");
            if (f.exists() && f.canRead()) {
                input = new FileInputStream(f);
                output = new PrintStream("a.out");
            }
        } catch (Throwable e) {
        }
        br = new BufferedReader(new InputStreamReader(input));
        out = new PrintWriter(output);
        solve();
        br.close();
        out.close();
    }

    void solve() {
        long n = nextLong(), m = nextLong();
        long x;
        if (n > m) {
            x = m;
            m = n;
            n = x;
        }
        if (n > 3) {
            out.print(n * m - (n * m) % 2);
        } else {
            long s = m - m % 6;
            long h = 0, o = m % 6;
            if (n == 1) {
                if (o == 4) {
                    h = 2;
                } else if (o == 5) {
                    h = 4;
                } else {
                    h = 0;
                }
            } else if (n == 2) {
                if (o == 3) {
                    h = 4;
                } else if (o == 4) {
                    h = 8;
                } else if (o == 5) {
                    h = 10;
                } else {
                    h = 0;
                }
            } else if (n == 3) {
                if (o == 2) {
                    h = 4;
                } else if (o == 3) {
                    h = 8;
                } else if (o == 4) {
                    h = 12;
                } else if (o == 5) {
                    h = 14;
                } else {
                    h = 0;
                }
            }
            if (n + m > 9 && n > 1) {
                out.print(n * m - (n * m) % 2);
                return;
            }
            out.print(s * n + h);
        }

    }

}