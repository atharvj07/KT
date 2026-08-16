import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {


        new Main().solve();
    }

    int mod = 1000000007;

    //15084000000000

    int inf = 1000000000;

    PrintWriter out;

    int n;

    ArrayList<Integer>[] g = new ArrayList[5000];

    void solve() throws IOException {

        Reader in;

        try {

            in = new Reader("input.txt");
            out = new PrintWriter( new BufferedWriter(new FileWriter("output.txt")) );
        }
        catch (Exception e) {

            in = new Reader();
            out = new PrintWriter( new BufferedWriter(new OutputStreamWriter(System.out)) );
        }

        //BufferedReader br = new BufferedReader( new FileReader("in.txt") );
        //BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );

        int n = in.nextInt();

        Pair[] a = new Pair[n];

        for (int i = 0; i < n; i++) {

            int x = in.nextInt();
            int y = in.nextInt();
            a[i] = new Pair(x, y, i);
        }

        Arrays.sort(a);

        int pos = n-1;
        int ans = 0;
        while (pos > 0) {

            if (a[pos].b <= 0)
                pos--;
            else
            {
                a[pos].a += a[pos].b;
                a[pos].b = 0;
                int tpos = pos;
                while (tpos > 0 && (a[tpos].a > a[tpos-1].a || (a[tpos].a == a[tpos-1].a && a[tpos].c < a[tpos-1].c))) {
                    ans++;
                    Pair p = a[tpos];
                    a[tpos] = a[tpos-1];
                    a[tpos-1] = p;
                    tpos--;
                }
            }
        }


        pos = 0;

        while (pos < n-1) {

            if (a[pos].b >= 0)
                pos++;
            else
            {
                a[pos].a += a[pos].b;
                a[pos].b = 0;
                int tpos = pos;
                while (tpos < n-1 && (a[tpos].a < a[tpos+1].a || (a[tpos].a == a[tpos+1].a && a[tpos].c > a[tpos+1].c))) {
                    ans++;
                    Pair p = a[tpos];
                    a[tpos] = a[tpos+1];
                    a[tpos+1] = p;
                    tpos++;
                }
            }
        }

        out.println(ans);
        out.flush();
        out.close();
    }

    class Pair implements Comparable<Pair>{

        int a;
        int b;
        int c;


        Pair(int a, int b, int c) {

            this.a = a;
            this.b = b;
            this.c = c;
        }

        public int compareTo(Pair p) {

            if (a < p.a)
                return 1;

            if (a > p.a)
                return -1;

            return 0;
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

    }

}