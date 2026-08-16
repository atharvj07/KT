import java.io.*;
import java.util.StringTokenizer;

//solution classes here

public class Main {

    //main solution here

    static Scanner sc = new Scanner(System.in);
    static PrintWriter out = new PrintWriter(System.out);
    static long mod = (long)1e9+7;
    static long MOD = 998244353;
    //static ArrayList<Integer> list[] = new ArrayList[(int)1e6+1];
    //static int color[] = new int[(int)1e6+1];
    //static int visit[] = new int[(int)1e5+1];
    //static Deque<Integer> q = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        long n = sc.nextLong();
        long k = sc.nextLong();
        long ans[] = new long[(int)k+1];
        for(long i=k;i>=1;i--) {
            long mul = power(k/i,n);
            long ex=0;
            mul%=mod;
            for(long j=1;j*i<=k;j++) {
                ex = (ex+ans[(int)(j*i)])%mod;
            }
            ans[(int)i]=(mod+mul-ex)%mod;
        }

        long sum=0;
        for(int i=1;i<=k;i++) {
            sum=(sum+(i*ans[i]))%mod;
        }

        out.println(sum);


        out.flush();
        out.close();
    }
    //solution functions here
    static long power(long x, long y)
    {
        long res = 1;
        x = x % mod;
        if (x == 0) return 0;
        while (y > 0)
        {
            if((y & 1)==1)
                res = (res * x) % mod;
            y = y >> 1;
            x = (x * x) % mod;
        }
        return res;
    }

    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public Scanner(FileReader fileReader) {
            br = new BufferedReader(fileReader);
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public boolean ready() throws IOException {
            return br.ready();
        }
    }
}

/* *****************************************************************************************************************************
 * I'M NOT IN DANGER, I'M THE DANGER!!!
 * *****************************************************************************************************************************
 */