    import java.lang.reflect.Array;
    import java.math.BigDecimal;
    import java.math.BigInteger;
    import java.math.RoundingMode;
    import java.util.*;
    import java.io.*;
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////                                                                                                               /////////
    ////////                                                                                                               /////////
    ////////   HHHH        HHHH  EEEEEEEEEEEEE   MMMM          MMMM         OOOOOO             SSSSSSS      EEEEEEEEEEEEE  /////////
    ////////   HHHH        HHHH  EEEEEEEEEEEEE   MMMMMM      MMMMMM      OOO      OOO        SSSS   SSS     EEEEEEEEEEEEE  /////////
    ////////   HHHH        HHHH  EEEEE           MMMM MMM  MMM MMMM    OOO          OOO    SSSS       SSS   EEEEE          /////////
    ////////   HHHH        HHHH  EEEEE           MMMM  MMMMMM  MMMM   OOO            OOO   SSSS             EEEEE          /////////
    ////////   HHHH        HHHH  EEEEE           MMMM          MMMM  OOO              OOO   SSSSSSS         EEEEE          /////////
    ////////   HHHHHHHHHHHHHHHH  EEEEEEEEEEE     MMMM          MMMM  OOO              OOO      SSSSSS       EEEEEEEEEEE    /////////
    ////////   HHHHHHHHHHHHHHHH  EEEEEEEEEEE     MMMM          MMMM  OOO              OOO         SSSSSSS   EEEEEEEEEEE    /////////
    ////////   HHHH        HHHH  EEEEE           MMMM          MMMM   OOO            OOO              SSSS  EEEEE          /////////
    ////////   HHHH        HHHH  EEEEE           MMMM          MMMM    OOO          OOO     SSS       SSSS  EEEEE          /////////
    ////////   HHHH        HHHH  EEEEEEEEEEEEE   MMMM          MMMM      OOO      OOO        SSS    SSSS    EEEEEEEEEEEEE  /////////
    ////////   HHHH        HHHH  EEEEEEEEEEEEE   MMMM          MMMM         OOOOOO             SSSSSSS      EEEEEEEEEEEEE  /////////
    ////////                                                                                                               /////////
    ////////                                                                                                               /////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    public class Contest1 {
        static int[]calc;
        static HashMap<Long, Long>calcc;
        static void  get(int x){
            if (x==0)return;
            calc[x]++;
            if (x%2==0){
                get(x/2);
            }
            else {
                get(x-1);
            }
        }
        static long n;
        static long getit(long z){
            if (z<=0)return 0l;
            if (z==n)return 1;
            if (z>n)return 0l;
            String ns = Long.toBinaryString(n);
            String ths= Long.toBinaryString(z);
            String diff=ns.substring(0,ths.length());
            int x = ns.length()-ths.length();
            long ans =(long)Math.pow(2,x)-1;
            Long dd= Long.parseLong(diff,2);
            if (dd>z){
                ans+=(long)Math.pow(2,x);
            }
            else if (dd==z){
                String zz = ns.substring(ths.length(),ns.length());
                ans+=Long.parseLong(zz,2)+1;
            }
            return ans;
        }
        public static void main(String[] args) throws IOException {
            Scanner sc = new Scanner(System.in);
            PrintWriter pw = new PrintWriter(System.out);
            int  t = sc.nextInt();
            while (t-->0){
                int n = sc.nextInt();
                int[]a=new int[n];
                int[]b = new int[n];
                for (int i =0;i<n;i++)a[i]=sc.nextInt();
                for (int i =0;i<n;i++)b[i]=sc.nextInt();
                HashMap<Integer,Integer>diff=new HashMap<>();
              int c =0;
                for (int i =0;i<n;i++){
                    diff.put(c,i);
                    if (a[i]==1)c++;
                    else c--;
                    diff.put(c,i+1);
                }
                c=0;
                for (int i =0;i<n;i++){
                    if (b[i]==1)c++;
                    else c--;
                }
                int ans=2*n;
                for (int i =0;i<n;i++){
                    if (diff.containsKey(-c)){
                        ans=Math.min(ans,n-diff.get(-c)+i);
                    }
                    if (b[i]==1)c--;
                    else c++;
                    if (diff.containsKey(-c)){
                        ans=Math.min(ans,n-diff.get(-c)+i+1);
                    }
                }
                pw.println(ans);
            }
            pw.flush();
        }
        static class Edge{
            int v,c;
            Edge(int a,int b){
                v=a;c=b;
            }
        }
        static class UnionFind {
            int[] p, rank, setSize;
            int numSets;
            int []mx;
            public UnionFind(int N)
            {
                mx=new int[N];
                p = new int[numSets = N];
                rank = new int[N];
                setSize = new int[N];
                for (int i = 0; i < N; i++) {
                    p[i] = i; setSize[i] = 1;
                    mx[i]=i;
                }
            }

            public int findSet(int i) { return p[i] == i ? i : (p[i] = findSet(p[i])); }

            public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

            public void unionSet(int i, int j)
            {
                if (isSameSet(i, j))
                    return;
                numSets--;
                int x = findSet(i), y = findSet(j);
                if(rank[x] > rank[y]) {
                    mx[y]=Math.max(mx[x],mx[y]);
                    p[y] = x; setSize[x] += setSize[y]; }
                else
                {	mx[x]=Math.max(mx[x],mx[y]);
                    p[x] = y; setSize[y] += setSize[x];
                    if(rank[x] == rank[y]) rank[y]++;
                }
            }

            public int numDisjointSets() { return numSets; }

            public int sizeOfSet(int i) { return setSize[findSet(i)]; }
        }
        static long gcd(long a, long b) {
            if (a == 0) return b;
            return gcd(b % a, a);
        }

        static class Scanner {
            StringTokenizer st;
            BufferedReader br;

            public Scanner(FileReader r) {
                br = new BufferedReader(r);
            }

            public Scanner(InputStream s) {
                br = new BufferedReader(new InputStreamReader(s));
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

            public double nextDouble() throws IOException {
                String x = next();
                StringBuilder sb = new StringBuilder("0");
                double res = 0, f = 1;
                boolean dec = false, neg = false;
                int start = 0;
                if (x.charAt(0) == '-') {
                    neg = true;
                    start++;
                }
                for (int i = start; i < x.length(); i++)
                    if (x.charAt(i) == '.') {
                        res = Long.parseLong(sb.toString());
                        sb = new StringBuilder("0");
                        dec = true;
                    } else {
                        sb.append(x.charAt(i));
                        if (dec)
                            f *= 10;
                    }
                res += Long.parseLong(sb.toString()) / f;
                return res * (neg ? -1 : 1);
            }

            public boolean ready() throws IOException {
                return br.ready();
            }
        }

    }