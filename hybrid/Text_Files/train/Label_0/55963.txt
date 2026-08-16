import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class A {

    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;

    public static void main(String[] args) throws IOException {
        try {
            in = new BufferedReader(new FileReader("a.in"));
            out = new PrintWriter(new File("a.out"));
        } catch (Exception e) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(new OutputStreamWriter(System.out));
        }
        tok = new StringTokenizer("");
        new A().solve();
        out.flush();
        out.close();
    }

    String nextTok() throws IOException {
        if (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextTok());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextTok());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextTok());
    }

    static class Pair implements Comparable<Pair>  {
        int x;
        int y;

        Pair (int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair o) {
            if (x < o.x) return -1;
            if (x > o.x) return 1;
            return 0;
        }
    }

    void solve() throws IOException {
        int n = nextInt();
        int cnt = nextInt();

        if (n/2 > cnt || (n > 1 && cnt == 0) || (n == 1 && cnt > 0)) {
            System.out.println(-1);
            return;
        }
        if (n == 1 && cnt == 0) {
            System.out.println(1);
            return;
        }

        int pair = n/2;


        pair--;

        int f = cnt - pair;
        int s = f*2;
        if (n >= 2) {
            out.print(f + " " + s + " ");
        }


        pair--;
        int ff = 3;
        int ss = 4;
        while (pair >= 0) {
            if (ff != f && ff != s && ss != s && ss != f) {
                out.print(ff + " " + ss+" ");
                ff+=2;
                ss+=2;
                pair--;
            } else {
                ff+=2;
                ss+=2;
            }
        }
        ss -=2;
        if (n%2 != 0) {
            int rr = ss+1;
            while (rr == f || rr == s) {
                rr++;
            }
            out.print(rr);
        }


    }

    private BigInteger catalan (int i) {
        return factorial(2 * i).divide((factorial(i + 1).multiply(factorial(i))));
    }

    private BigInteger factorial (int i) {
        BigInteger n = BigInteger.valueOf(i);
        if (i == 0) {
            return new BigInteger("1");
        }
        while (--i > 0) {
            n = n.multiply(BigInteger.valueOf(i));
        }
        return n;
    }
}