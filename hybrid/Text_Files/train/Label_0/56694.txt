import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.abs;
import java.util.*;
import java.io.*;

public class A
{
    static int n;
    static int[] arr;
    static char[] s;
    static int[][] dp;
    public static void main(String[] args) throws IOException
    {
        f = new Flash();
        out = new PrintWriter(System.out);

        int T = 1; //ni();
        for(int tc = 1; tc <= T; tc++){
            n = ni(); s = nc();
            arr = new int[n];
            for(int i = 0; i < n; i++) arr[i] = s[i]-'0';
            sop(fn());
        }

        out.flush(); out.close();
    }

    static long fn()
    {
        dp = new int[n][1<<20];
        for(int i = 0; i < n; i++) Arrays.fill(dp[i], -1);
        long ans = 0l;
        for(int pref = 0; pref < n; pref++) {
            //donot consider this prefix
            ans += dfs(pref, 0);
            if(ans >= mod) ans -= mod;
        }

        return ans;
    }

    static int dfs(int i, int mask) {
        if(i == n) {
            int cnt = Integer.bitCount(mask);
            if(cnt != 0 && (1<<cnt)-1 == mask) return 1;
            return 0;
        }

        if(dp[i][mask] != -1) return dp[i][mask];

        int ret = 0;
        int num = 0;
        for(int j = i; j < n; j++) {
            num *= 2; num += arr[j];
            if(num > 20) break;
            if(num == 0) continue;
            ret += dfs(j+1, mask|(1<<(num-1)));
            if(ret >= mod) ret -= mod;
        }

        //donot consider this suffix
        int cnt = Integer.bitCount(mask);
        if(cnt != 0 && (1<<cnt)-1 == mask) ret++;

        return dp[i][mask] = ret;
    }

    static Flash f;
    static PrintWriter out;
    static final long mod = (long)1e9+7;
    static final long inf = (long)1e18;
    static final int _inf = (int)1e9;
    static final int maxN = (int)1e6;
    static long[] fact, inv;

    static class cpr implements Comparator<int[]>{
        public int compare(int[] a, int[] b) {
            return Integer.compare(a[0], b[0]);
        }
    }

    static void sort(int[] a){
        List<Integer> A = new ArrayList<>();
        for(int i : a) A.add(i);
        Collections.sort(A);
        for(int i = 0; i < A.size(); i++) a[i] = A.get(i);
    }

    static void sort(long[] a){
        List<Long> A = new ArrayList<>();
        for(long i : a) A.add(i);
        Collections.sort(A);
        for(int i = 0; i < A.size(); i++) a[i] = A.get(i);
    }

    static void print(int[] a){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < a.length; i++) sb.append(a[i] + " ");
        sop(sb);
    }

    static void print(long[] a){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < a.length; i++) sb.append(a[i] + " ");
        sop(sb);
    }

    static int swap(int itself, int dummy){return itself;}
    static long swap(long itself, long dummy){return itself;}
    static char swap(char itself, char dummy){return itself;}
    static void sop(Object o){out.println(o);}
    static int ni(){return f.ni();}
    static long nl(){return f.nl();}
    static double nd(){return f.nd();}
    static String next(){return f.next();}
    static String ns(){return f.ns();}
    static String yes = "YES", no = "NO";
    static char[] nc(){return f.nc();}
    static int[] arr(int len){return f.arr(len);}
    static int gcd(int a, int b){if(b == 0) return a; return gcd(b, a%b);}
    static long gcd(long a, long b){if(b == 0) return a; return gcd(b, a%b);}
    static int fcm(int a, int b){return (a*b)/gcd(a, b);}
    static long fcm(long a, long b){return (a*b)/gcd(a, b);}
    static double log2(long N) {return Math.log(N) / Math.log(2);}
    static void debug(int[] a) {sop(Arrays.toString(a));}
    static void debug(long[] a) {sop(Arrays.toString(a));}

    static class Flash
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next(){
            while(!st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch(IOException e){
                    e.printStackTrace();
                }
            }

            return st.nextToken();
        }

        String ns(){
            String s = new String();
            try{
                s = br.readLine().trim();
            }catch(IOException e){
                e.printStackTrace();
            }

            return s;
        }

        int[] arr(int n){
            int[] a = new int[n];
            for(int i = 0; i < n; i++) a[i] = ni();
            return a;
        }

        char[] nc(){return ns().toCharArray();}
        int ni(){return Integer.parseInt(next());}
        long nl(){return Long.parseLong(next());}
        double nd(){return Double.parseDouble(next());}
    }
}