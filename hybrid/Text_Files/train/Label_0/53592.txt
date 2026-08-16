import java.io.*;
import java.util.*;
import java.math.*;


public class b {
    String _token() throws IOException {
        while (in.ready() && !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        if (st.hasMoreTokens())
            return st.nextToken();
        return "";
    }

    void do_solve() throws NumberFormatException, IOException {
        int n = _int();
        int w[] = new int[n];
        int h[] = new int[n];
        int l[] = new int[n];
        for(int i=0;i<n;i++) {
            l[i]=_int();
            w[i]=_int();
            h[i]=_int();
        }
        int m = _int();
        int a[] = new int[m];
        int b[] = new int[m];
        long c[] = new long[m];
        for(int i=0;i<m;i++)
        {
            a[i] = _int();
            b[i] = _int();
            c[i] = _int();
        }
        long sum=0;
        for(int i=0;i<n;i++) {
            long best = Long.MAX_VALUE;
            for(int j=0;j<m;j++) {
                if (a[j]>=h[i]){
                long x = ((2*(w[i]+l[i])-1)/((a[j]/h[i])*b[j])+1)*c[j]; 
                if (x < best)
                    best = x;
                }
            }
            sum += best;
        }
        out.println(sum);
    }

    void mainProgram() throws NumberFormatException, IOException {
        /*
         test("b.in");
         */
        init(false, "b");
        boolean multy = false;

        if (!multy) {
//          while (in.ready() || st.hasMoreTokens()) {
                do_solve();
//          }
        } else {
            for (int T = _int(); T > 0; --T) {
                do_solve();
            }
        }
        out.close();
    }

    int rand(int x) {
        return (int) (Math.random() * x);
    }

    void test(String name) throws IOException {
        out = new PrintWriter(new File(name));

        out.close();
    }

    void init(boolean FILE, String name) throws NumberFormatException,
            IOException {
        Locale.setDefault(Locale.US);
        if (FILE) {
            in = new BufferedReader(new FileReader(name + ".in"));
            out = new PrintWriter(name + ".out");
        } else {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }
        st = new StringTokenizer("");
    }

    public static void main(String[] args) throws NumberFormatException,
            IOException {
        long T = System.currentTimeMillis();
        new b().mainProgram();
        System.err.println("Time of working: "
                + (System.currentTimeMillis() - T) + " ms");
    }

    void deb(String s) {
        System.err.println(s);
    }

    void deb(Object a) {
        System.err.println(a.toString());
    }

    BigInteger add(BigInteger A, BigInteger B) {
        return A.add(B);
    }

    BigInteger mult(BigInteger A, BigInteger B) {
        return A.multiply(B);
    }

    BigInteger sub(BigInteger A, BigInteger B) {
        return A.subtract(B);
    }

    BigInteger div(BigInteger A, BigInteger B) {
        return A.divide(B);
    }

    BigInteger mi(BigInteger A) {
        return (BigInteger.ZERO).subtract(A);
    }

    BigInteger sq(BigInteger A) {
        return A.multiply(A);
    }

    BigInteger val(long a) {
        return BigInteger.valueOf(a);
    }

    int cmp(BigInteger a, BigInteger b) {
        return a.compareTo(b);
    }

    BufferedReader in;
    StringTokenizer st;
    PrintWriter out;

    int _int() throws NumberFormatException, IOException {
        return Integer.parseInt(_token());
    }

    long _long() throws NumberFormatException, IOException {
        return Long.parseLong(_token());
    }

    double _double() throws NumberFormatException, IOException {
        return Double.parseDouble(_token());
    }

    int gcd(int a, int b) {
        if (a < 0)
            a = -a;
        if (b < 0)
            b = -b;
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    long gcd(long a, long b) {
        if (a < 0)
            a = -a;
        if (b < 0)
            b = -b;
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    BigInteger gcd(BigInteger a, BigInteger b) {
        if (cmp(a, val(0)) < 0)
            a = mi(a);
        if (cmp(b, val(0)) < 0)
            b = mi(b);
        return a.gcd(b);
    }
}
