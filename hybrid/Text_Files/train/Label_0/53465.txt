import java.util.*;
import java.io.*;
import java.math.BigInteger;
import java.text.*;
public class Main {
    static long mod = (long)1e9 + 7;
    static long mod1 = 998244353;
    static FastScanner f;
    static PrintWriter pw = new PrintWriter(System.out);
    static Scanner S = new Scanner(System.in);
    static long x0; static long y0;
    public static void solve()throws IOException {
        int n = f.nextInt(); int k = f.nextInt();
        String str = f.next();
        int freq[] = new int[26];
        int dp[] = new int[26];
        char c[] = str.toCharArray();
        for(int i = 0; i < n; ++i) {
            ++freq[c[i] - 'a'];
        }
        int sum = 0;
        int i = 0;
        while(sum < k) {
            if(freq[i] > 0) {
                dp[i] = Math.min(k - sum , freq[i]);
                sum += Math.min(k - sum , freq[i]);
            }
            ++i;
        }
        //StringBuffer sb = new StringBuffer(str);
        i = 0;
        sum = 0;
        /* Gotta TLE
        while(sum < k) {
            int j = 0;
            while(j < dp[i]) {
                char tt = (char)(i + 97);
                String cc = Character.toString(tt);
                sb.deleteCharAt(sb.indexOf(cc));
                ++j;
            }
            sum += dp[i];
            ++i;
        }
        */
        HashMap<Character , ArrayList<Integer>> h = new HashMap<Character , ArrayList<Integer>>();
        for(i = 0; i < n; ++i) {
            char cc = c[i];
            if(h.containsKey(cc)) h.get(cc).add(i);
            else {h.put(cc , new ArrayList<Integer>()); h.get(cc).add(i);}
        }
        HashSet<Integer> del = new HashSet<Integer>();
        for(i = 0; i < 26; ++i) {
            int j = 0;
            char y = (char)(i + 97);
            ArrayList<Integer> idxx = h.get(y);
            while(j < dp[i]) {
                del.add(idxx.get(j));
                ++j;
            }
        }
        for(i = 0; i < n; ++i) {
            if(!del.contains(i)) p(c[i]);
        }
    }
    public static void main(String[] args)throws IOException {
        init();
        int t = 1;
        while(t --> 0) {solve();}
        pw.flush(); 
        pw.close();  
    }
        
/******************************END OF MAIN PROGRAM*******************************************/
    public static void init()throws IOException{if(System.getProperty("ONLINE_JUDGE")==null){f=new FastScanner("");}else{f=new FastScanner(System.in);}}
    public static class FastScanner {
        BufferedReader br;StringTokenizer st;
        FastScanner(InputStream stream){try{br=new BufferedReader(new InputStreamReader(stream));}catch(Exception e){e.printStackTrace();}}
        FastScanner(String str){try{br=new BufferedReader(new FileReader("!a.txt"));}catch(Exception e){e.printStackTrace();}}
        String next(){while(st==null||!st.hasMoreTokens()){try{st=new StringTokenizer(br.readLine());}catch(IOException e){e.printStackTrace();}}return st.nextToken();}
        String nextLine()throws IOException{return br.readLine();}int nextInt(){return Integer.parseInt(next());}long nextLong(){return Long.parseLong(next());}double nextDouble(){return Double.parseDouble(next());}
    }
    public static void pn(Object o){pw.println(o);}
    public static void p(Object o){pw.print(o);}
    public static void pni(Object o){pw.println(o);pw.flush();}
    static class Point implements Comparator<Point>{int x;int y;Point(int x,int y){this.x=x;this.y=y;}Point(){}public int compare(Point a, Point b){if(a.x==b.x)return a.y-b.y;return a.x-b.x;}}
    static int gcd(int a,int b){if(b==0)return a;else{return gcd(b,a%b);}}
    static long gcd(long a,long b){if(b==0)return a;else{return gcd(b,a%b);}}
    static long exgcd(long a,long b){if(b==0){x0=1;y0=0;return a;}long temp=exgcd(b,a%b);long t=x0;x0=y0;y0=t-a/b*y0;return temp;}
    static long pow(long a,long b){long res=1;while(b>0){if((b&1)==1)res=res*a;b>>=1;a=a*a;}return res;}
    static long mpow(long a,long b){long res=1;while(b>0){if((b&1)==1)res=((res%mod)*(a%mod))%mod;b>>=1;a=((a%mod)*(a%mod))%mod;}return res;}
    static boolean isPrime(long n){if(n<=1)return false;if(n<=3)return true;if(n%2==0||n%3==0)return false;for(long i=5;i*i<=n;i=i+6)if(n%i==0||n%(i+2)==0)return false;return true;}
    static HashSet<Long> factors(long n){HashSet<Long> hs=new HashSet<Long>();for(long i=1;i<=(long)Math.sqrt(n);i++){if(n%i==0){hs.add(i);hs.add(n/i);}}return hs;}
    static int[] inpint(int n){int arr[]=new int[n];for(int i=0;i<n;i++){arr[i]=f.nextInt();}return arr;}
    static long[] inplong(int n){long arr[] = new long[n];for(int i=0;i<n;i++){arr[i]=f.nextLong();}return arr;}
    static boolean ise(int x){return ((x&1)==0);}static boolean ise(long x){return ((x&1)==0);}
    static int gnv(char c){return Character.getNumericValue(c);}
    static int log(long x){return x == 1?0:(1+log(x/2));} static int log(int x){return x == 1?0:(1+log(x/2));}
    static void sort(int[] a){ArrayList<Integer> l=new ArrayList<>();for(int i:a)l.add(i);Collections.sort(l);for(int i=0;i<a.length;++i)a[i]=l.get(i);}
    static void sort(long[] a){ArrayList<Long> l=new ArrayList<>();for(long i:a)l.add(i);Collections.sort(l);for(int i=0;i<a.length;++i)a[i]=l.get(i);}
    static void sort(ArrayList<Integer> a){Collections.sort(a);}
}