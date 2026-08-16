import java.util.*;
import java.io.*;


public class Main {
    static int mod = (int) 1e9 + 7;
    static int DX[] = { -1, 0, 1, 0 }, DY[] = { 0, -1, 0, 1 };

    static int n;
    static long k;
    static long a[];
    public static void main(String[] args) {
        FastScanner fs = new FastScanner(System.in);
        n = fs.nextInt();
        k = fs.nextLong();
        a = fs.nextLongArray(n);
        Arrays.sort(a);
        long INF = (long)(1e18)+1;
        long l = -INF;
        long r = INF;
        while(l+1<r) {
            long c = (l+r)/2;
            if(check(c))l=c;
            else r = c;
        }
        System.out.println(l);
    }
    //x未満の組合せがk個未満ならtrue
    static boolean check(long x) {
        long tot = 0;
        for(int i=0;i<n;i++) {
            long now = a[i];
            int l = -1, r = n;
            if(now >= 0) {
                while(l+1<r) {
                    int c = (l+r)/2;
                    if(now * a[c] < x) l = c;
                    else r = c;
                }
                tot += (l+1);
            }
            else {
                while(l+1<r) {
                    int c = (l+r)/2;
                    if(now * a[c] < x) r = c;
                    else l = c;
                }
                tot += (n - r);
            }
            if((long)a[i] * a[i]<x)tot--;
        }
        if(tot/2 < k) return true;
        else return false;
    }
}

//高速なScanner
class FastScanner {
    private BufferedReader reader = null;
    private StringTokenizer tokenizer = null;

    public FastScanner(InputStream in) {
        reader = new BufferedReader(new InputStreamReader(in));
        tokenizer = null;
    }

    public String next() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public String nextLine() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken("\n");
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public int[] nextIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = nextInt();
        return a;
    }

    public long[] nextLongArray(int n) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = nextLong();
        return a;
    }
}