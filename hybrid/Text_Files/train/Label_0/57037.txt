import java.io.*;
import java.util.*;
import java.math.*;


public class Main {
    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;

    static void solve() throws Exception {
        int n = nextInt();
        int m = nextInt();
        int[] l = new int[n+1];
        int[] r = new int[n+1]; 
        for (int i = 1; i <= n; i++) {
            l[i] = nextInt();
            r[i] = l[i];
        }
        for (int i = 1; i <= n; i++) {
            if (l[i] == r[i]) {
                for (int j = 1; j <= n; j++) {
                    if (i != j) {
                        if (l[j] != r[i] && l[i] != r[j]) {
                            int tmp = l[i];
                            l[i] = l[j];
                            l[j] = tmp;
                        } else if(l[i] != r[j] && l[j] != r[i]) {
                            int tmp = r[i];
                            r[i] = r[j];
                            r[j] = tmp;
                        }
                    }
                }
            }           
        }
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (l[i] != r[i]) {
                res++;
            }
        }
        out.println(res);
        for (int i = 1; i <= n; i++) {
            out.println(l[i] + " " + r[i]);
        }
    }
    
    static int sqr(int x) {
        return x*x;
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    static long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    static BigInteger nextBigInteger() throws IOException {
        return new BigInteger(next());
    }
    
    static String next() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    static String nextLine() throws IOException {
        tok = new StringTokenizer("");
        return in.readLine();
    }

    static boolean hasNext() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            String s = in.readLine();
            if (s == null) {
                return false;
            }
            tok = new StringTokenizer(s);
        }
        return true;
    }

    public static void main(String args[]) {
        try {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(new OutputStreamWriter(System.out));
            //in = new BufferedReader(new FileReader("peacefulsets.in"));
            //out = new PrintWriter(new FileWriter("peacefulsets.out"));
            solve();
            in.close();
            out.close();
        } catch (Throwable e) {
            e.printStackTrace();
            java.lang.System.exit(1);
        }
    }
}