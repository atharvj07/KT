import java.util.*;import java.io.*;import java.math.*;
public class SymmetricArray
{
    static final Random random=new Random();
    
    static void ruffleSort(int[] a) {
        int n = a.length; 
        for (int i=0; i<n; i++) {
            int oi=random.nextInt(n), temp=a[oi];
            a[oi]=a[i]; a[i]=temp;
        }
        ArrayList<Integer> lst = new ArrayList<>();
        for(int i : a)
            lst.add(i);
        Collections.sort(lst);
        for(int i = 0; i < n; i++)
            a[i] = lst.get(i);
    }

    static void ruffleSort(long[] a) {
        int n = a.length; 
        for (int i=0; i<n; i++) {
            int oi=random.nextInt(n);
            long temp=a[oi];
            a[oi]=a[i]; a[i]=temp;
        }
        ArrayList<Long> lst = new ArrayList<>();
        for(long i : a)
            lst.add(i);
        Collections.sort(lst);
        for(int i = 0; i < n; i++)
            a[i] = lst.get(i);
    }

    public static void process()throws IOException
    {
        int n = ni();
        long[] d = nal(2*n);
        ruffleSort(d);
        TreeSet<Long> st = new TreeSet<>();
        for(long l : d)
            st.add(l);
        if(st.size() != n){
            pn("NO");
            return;
        }
        for(int i = 1; i < 2*n; i+=2){
            if(d[i] != d[i-1]){
                pn("NO");
                return;
            }
        }
        long[] a = new long[n];
        int c = 0;
        for(long l : st){
            a[c] = l;
            c++;
        }
        long sum = 0;
        for(int i = n-1; i >= 0; i--){
            long ans = a[i]-sum;
            if(ans > 0 && ans%(2*(i+1)) == 0){
                ans = ans/(2*(i+1));
                sum += 2*ans;
                continue;
            }
            pn("NO");
            return;
        }
        pn("YES");
    }
   
    static AnotherReader sc;
    static PrintWriter out;
    public static void main(String[]args)throws IOException
    {
        boolean oj = System.getProperty("ONLINE_JUDGE") != null;
        if(oj){sc=new AnotherReader();out=new PrintWriter(System.out);}
        else{sc=new AnotherReader(100);out=new PrintWriter("output.txt");}
        long s = System.currentTimeMillis();
        int t=1;
        t=ni();
        //int k = t;
        while(t-->0) {/*p("Case #"+ (k-t) + ": ")*/;process();}
        out.flush();
        System.err.println(System.currentTimeMillis()-s+"ms");
        out.close();
    }

    static long power(long k, long c, long mod){
        long y = 1;
        while(c > 0){
            if(c%2 == 1)
                y = y * k % mod;
            c = c/2;
            k = k * k % mod;
        }
        return y;
    }

 
    static void pn(Object o){out.println(o);}
    static void p(Object o){out.print(o);}
    static void pni(Object o){out.println(o);out.flush();}
    static int ni()throws IOException{return sc.nextInt();}
    static long nl()throws IOException{return sc.nextLong();}
    static double nd()throws IOException{return sc.nextDouble();}
    static String nln()throws IOException{return sc.nextLine();}
    static int[] nai(int N)throws IOException{int[]A=new int[N];for(int i=0;i!=N;i++){A[i]=ni();}return A;}
    static long[] nal(int N)throws IOException{long[]A=new long[N];for(int i=0;i!=N;i++){A[i]=nl();}return A;}
    static long gcd(long a, long b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int gcd(int a, int b)throws IOException{return (b==0)?a:gcd(b,a%b);}
    static int bit(long n)throws IOException{return (n==0)?0:(1+bit(n&(n-1)));}
    
/////////////////////////////////////////////////////////////////////////////////////////////////////////
 
    static class AnotherReader{BufferedReader br; StringTokenizer st;
    AnotherReader()throws FileNotFoundException{
    br=new BufferedReader(new InputStreamReader(System.in));}
    AnotherReader(int a)throws FileNotFoundException{
    br = new BufferedReader(new FileReader("input.txt"));}
    String next()throws IOException{
    while (st == null || !st.hasMoreElements()) {try{
    st = new StringTokenizer(br.readLine());}
    catch (IOException  e){ e.printStackTrace(); }}
    return st.nextToken(); } int nextInt() throws IOException{
    return Integer.parseInt(next());}
    long nextLong() throws IOException
    {return Long.parseLong(next());}
    double nextDouble()throws IOException { return Double.parseDouble(next()); }
    String nextLine() throws IOException{ String str = ""; try{
    str = br.readLine();} catch (IOException e){
    e.printStackTrace();} return str;}}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
}