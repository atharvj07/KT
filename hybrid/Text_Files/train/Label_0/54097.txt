import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class TaskC {

    public static void main(String[] args) throws IOException {

        new TaskC().go();
    }

    PrintWriter out;
    Reader in;
    BufferedReader br;

    TaskC() throws IOException {

        try {

            //br = new BufferedReader( new FileReader("input.txt") );
            in = new Reader("input.txt");
            out = new PrintWriter( new BufferedWriter(new FileWriter("output.txt")) );
        }
        catch (Exception e) {

            //br = new BufferedReader( new InputStreamReader( System.in ) );
            in = new Reader();
            out = new PrintWriter( new BufferedWriter(new OutputStreamWriter(System.out)) );
        }
    }

    void go() throws IOException {

        int t = 1;
        while (t > 0) {
            solve();
            //out.println();
            t--;
        }

        out.flush();
        out.close();
    }

    int inf = 2000000000;
    int mod = 1000000007;
    double eps = 0.000000001;

    int n;
    int m;
    ArrayList<Integer>[] g;
    void solve() throws IOException {

        //System.err.println(getOdd(6));

        long l = in.nextLong();
        long r = in.nextLong();

        out.print(((f(r) - f(l - 1)) % mod + mod) % mod);
    }

    long f(long r) {
        if (r <= 0)
            return 0;

        long odd = 0;
        long even = 0;
        long all = 0;
        long st = 1;
        int cur = 0;
        while (all + st <= r) {
            cur ^= 1;
            if (cur == 1) {
                odd += st;
            } else {
                even += st;
            }
            all += st;
            st *= 2;
        }

        cur ^= 1;
        if (cur == 1) {
            odd += r - all;
        } else {
            even += r - all;
        }

        //System.err.println(odd);
        //System.err.println(even);

        return (getOdd(odd * 2) + getEven(even * 2)) % mod;
    }

    long getEven(long r) {
        if (r % 2 != 0)
            r--;
        r /= 2;
        return (getSum(r) * 2) % mod;
    }

    long getOdd(long r) {
        return ((getSum(r) - getEven(r)) % mod + mod) % mod;
    }

    long getSum(long r) {
        if (r % 2 == 0)
            return  (r / 2) % mod * ((r + 1) % mod) % mod;
        return  (r % mod * (((r + 1) / 2) % mod)) % mod;
    }

    class Pair implements Comparable<Pair> {
        int a;
        int b;

        Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }

        public int compareTo(Pair p) {
            if (a != p.a)
                return Integer.compare(a, p.a);
            else
                return Integer.compare(b, p.b);
        }
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

        int[] nextIntArray(int n) throws IOException {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        ArrayList<Integer>[] nextGraph(int n, int m) throws IOException {
            ArrayList<Integer>[] g = new ArrayList[n];
            for (int i = 0; i < n; i++)
                g[i] = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                int x = nextInt() - 1;
                int y = nextInt() - 1;
                g[x].add(y);
                g[y].add(x);
            }

            return g;
        }

    }

}