import java.io.*;
import java.util.StringTokenizer;

public class ZeroXORSubsetless
{
    public static final long mod=1000000007;
    public static final int d=31;

    public static void main (String[] args) throws java.lang.Exception {
        FastScanner sc = new FastScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

        int N = sc.nextInt();

        int arr[] = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = sc.nextInt();
            arr[i] ^= arr[i - 1];
        }
        if (arr[N] == 0) {
            out.println(-1);
        } else {

            int basis[] = new int[d];
            int size = 0;
            for (int i = N; i > 0; i--) {
                if (insertVector(arr[i], d, basis, size))
                    size++;
            }
            out.println(size);
        }

        out.close();
    }

    public static boolean insertVector(int vec,int d,int basis[],int size) {
        if (size == d)
            return false;

        for (int i = d - 1; i >= 0; i--) {
            if ((vec & (1 << i)) == 0) continue;
            if (basis[i] != 0) {
                vec = vec ^ basis[i];
            } else {
                basis[i] = vec;
                return true;
            }
        }
        return false;
    }

    //finding if x can represented as linear combination of the given basis
    public static boolean FindIfXinBasis(int X,int d,int basis[]) {
        for (int i = 31; i >= 0; i--) {
            if ((X & (1 << i)) == 0) continue;

            if (i >= d || basis[i] == 0)
                return false;

            X = X ^ basis[i];
        }
        return true;
    }

    //a power b
    static long pow(long a,long b){
        if(b==0)
            return 1;
        else if(b==1)
            return a;
        long ans=pow(a,b/2);
        ans=(ans*ans)%mod;
        if(b%2==1)
            ans=(ans*a)%mod;
        return ans%mod;
    }

    //-----------MyScanner class for faster input----------
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

    }
    //--------------------------------------------------------
}
