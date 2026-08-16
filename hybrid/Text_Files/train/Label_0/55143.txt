
import java.io.*;
import java.util.StringTokenizer;

public class Contest1184A2 {
    public static PrintWriter out = new PrintWriter(System.out);
    public static FastScanner enter = new FastScanner(System.in);

    public static void main(String[] args) throws IOException {
        solve();
        out.close();
    }
    public static int input[];
    public static boolean goodLength[];
    private static void solve() throws IOException {
        int n=enter.nextInt();
        String in=enter.next();
        input=new int[n];
        goodLength=new boolean[n+1];
        for (int i = 0; i <n ; i++) {
            input[i]=in.charAt(i)-'0';
        }
        for (int i = 1; i <=n ; i++) {
            if(n%i==0){
                goodLength[i]=isLenGood(n,i);
            }
        }
        int ans=0;

        for (int i = 1; i <=n ; i++) {
            int gc= (int) gcd(i,n);
            if(goodLength[gc]) ans++;
        }
        out.println(ans);
    }

    private static boolean isLenGood(int n, int len) {
        for (int i = 0; i <len; i++) {
            int ans=0;
            for (int j = i; j <n ; j+=len) {
                ans^=input[j];
            }
            if(ans==1) {
                return false;
            }
        }
        return true;
    }
    public static long gcd(long a, long b){
        while(b!=0){
            a%=b;
            a^=(b^=a);
            b^=a;
        }
        return a;
    }


    static class FastScanner {
        BufferedReader br;
        StringTokenizer stok;

        FastScanner(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        String next() throws IOException {
            while (stok == null || !stok.hasMoreTokens()) {
                String s = br.readLine();
                if (s == null) {
                    return null;
                }
                stok = new StringTokenizer(s);
            }
            return stok.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        char nextChar() throws IOException {
            return (char) (br.read());
        }

        String nextLine() throws IOException {
            return br.readLine();
        }
    }
}
