import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;

public class Task2 {

    public static void main(String[] args) throws IOException {

        new Task2().solve();

    }

    //ArrayList<Integer>[] g;

    int mod = 1000000007;

    PrintWriter out;

    int n;
    int m;
    //int[][] a = new int[1000][1000];


    //int cnt = 0;

    long base = (1L << 63);
    long P = 31;

    int[][] a;

    void solve() throws IOException {

        //Reader in = new Reader("in.txt");
        //out = new PrintWriter( new BufferedWriter(new FileWriter("output.txt")) );
        Reader in = new Reader();
        PrintWriter out = new PrintWriter( new BufferedWriter(new OutputStreamWriter(System.out)) );

        //BufferedReader br = new BufferedReader( new FileReader("in.txt") );
        //BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );

        int n = in.nextInt();

        double[][] a = new double[n][n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = in.nextDouble();

        double[] dp = new double[1 << n];

        dp[(1 << n) - 1] = 1;

        for (int mask = (1 << n) -1; mask >= 0; mask--) {

            int k = Integer.bitCount(mask);
            double p = 1.0 / (k*(k-1)/2.0);

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if ((mask & (1 << i)) != 0 && (mask & (1 << j)) != 0)
                        dp[(mask & ~(1 << j))] += p*dp[mask]*a[i][j];

        }

        for (int i = 0; i < n; i++)
            out.print(dp[1 << i]+" ");

        out.flush();
        out.close();
    }

    long gcd(long a, long b) {

        if (b == 0)
            return a;

        return gcd(b, a%b);

    }

    class Item {

        int a;
        int b;
        int c;

        Item(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

    }

    class Pair implements Comparable<Pair>{

        int a;
        int b;

        Pair(int a, int b) {

            this.a = a;
            this.b = b;
        }

        public int compareTo(Pair p) {

            if (b < p.b)
                return 1;

            if (b > p.b)
                return -1;

            return 0;
        }

        //		@Override
        //		public boolean equals(Object o) {
        //			Pair p = (Pair) o;
        //			return a == p.a && b == p.b;
        //		}
        //
        //		@Override
        //		public int hashCode() {
        //			return Integer.valueOf(a).hashCode() + Integer.valueOf(b).hashCode();
        //		}

    }

    class Reader {

        BufferedReader  br;
        StringTokenizer tok;

        Reader(String file) throws IOException {
            br = new BufferedReader( new FileReader(file) );
        }

        Reader() throws IOException {
            br = new BufferedReader( new InputStreamReader(System.in) );
        }

        String next() throws IOException {

            while (tok == null || !tok.hasMoreElements())
                tok = new StringTokenizer(br.readLine());
            return tok.nextToken();
        }

        int nextInt() throws NumberFormatException, IOException {
            return Integer.valueOf(next());
        }

        long nextLong() throws NumberFormatException, IOException {
            return Long.valueOf(next());
        }

        double nextDouble() throws NumberFormatException, IOException {
            return Double.valueOf(next());
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

    }

}