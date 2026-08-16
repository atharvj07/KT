import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) {new Main().run();}

    FastReader in = new FastReader();
    PrintWriter out = new PrintWriter(System.out);
    long[] rec=new long[200005];
    long[] inv=new long[200005];
    void run() {
        rec[0]=1;
        for(int i=1;i<200005;i++){
            rec[i]=rec[i-1]*i%mod;
        }
        inv[200004]=pow(rec[200004],mod-2);
        for(int i=200003;i>=0;i--){
            inv[i]=inv[i+1]*(i+1)%mod;
        }
        for(int q=ni();q>0;q--){
            work();
        }
        out.flush();
    }
    long mod=1000000007;
    long gcd(long a,long b) {
        return a==0?b:gcd(b%a,a);
    }
    void work() {
        long n=ni(),s=nl(),e=nl();
        long ret=count(n/2,n-n/2,s,e)%mod;
        if(n%2==1){
            ret=(ret+count(n/2+1,n-n/2-1,s,e))%mod;
        }
        out.println(ret);
    }

    private long count(long c1, long c2, long s, long e) {
        long n=c1+c2;
        long ret=0;
        long d=Math.min(1-s,e-n);
        ret=d*C(n,c1)%mod;
        for(d++;;d++){
            long v2=Math.max(s+d-1,0),v1=Math.max(n-(e-d),0);
            if(v1>c1||v2>c2){
                break;
            }
            ret=(ret+C(n-v1-v2,c1-v1))%mod;
        }
        return ret;
    }

    private long C(long c, long a) {
        if(c<0||a<0||c-a<0){
            int g=1;
        }
        return rec[(int)c]*inv[(int)a]%mod*inv[(int)(c-a)]%mod;
    }

    long pow(long a,long b){
        long ret=1;
        while(b>0){
            if(b%2==1){
                ret=ret*a%mod;
            }
            b/=2;
            a=a*a%mod;
        }
        return ret;
    }
    //input
    @SuppressWarnings("unused")
    private ArrayList<Integer>[] ng(int n, int m) {
        ArrayList<Integer>[] graph=(ArrayList<Integer>[])new ArrayList[n];
        for(int i=0;i<n;i++) {
            graph[i]=new ArrayList<>();
        }
        for(int i=1;i<=m;i++) {
            int s=in.nextInt()-1,e=in.nextInt()-1;
            graph[s].add(e);
            graph[e].add(s);
        }
        return graph;
    }

    private ArrayList<long[]>[] ngw(int n, int m) {
        ArrayList<long[]>[] graph=(ArrayList<long[]>[])new ArrayList[n];
        for(int i=0;i<n;i++) {
            graph[i]=new ArrayList<>();
        }
        for(int i=1;i<=m;i++) {
            long s=in.nextLong()-1,e=in.nextLong()-1,w=in.nextLong();
            graph[(int)s].add(new long[] {e,w});
            graph[(int)e].add(new long[] {s,w});
        }
        return graph;
    }

    private int ni() {
        return in.nextInt();
    }

    private long nl() {
        return in.nextLong();
    }
    private double nd() {
        return in.nextDouble();
    }
    private String ns() {
        return in.next();
    }

    private long[] na(int n) {
        long[] A=new long[n];
        for(int i=0;i<n;i++) {
            A[i]=in.nextLong();
        }
        return A;
    }

    private int[] nia(int n) {
        int[] A=new int[n];
        for(int i=0;i<n;i++) {
            A[i]=in.nextInt();
        }
        return A;
    }
}

class FastReader
{
    BufferedReader br;
    StringTokenizer st;
    InputStreamReader input;//no buffer
    public FastReader()
    {
        br=new BufferedReader(new InputStreamReader(System.in));
    }

    public FastReader(boolean isBuffer)
    {
        if(!isBuffer){
            input=new InputStreamReader(System.in);
        }else{
            br=new BufferedReader(new InputStreamReader(System.in));
        }
    }

    public boolean hasNext(){
        try{
            String s=br.readLine();
            if(s==null){
                return  false;
            }
            st=new StringTokenizer(s);
        }catch(IOException e){
            e.printStackTrace();
        }
        return true;
    }

    public String next()
    {   
        if(input!=null){
            try {
                StringBuilder sb=new StringBuilder();
                int ch=input.read();
                while(ch=='\n'||ch=='\r'||ch==32){
                    ch=input.read();
                }
                while(ch!='\n'&&ch!='\r'&&ch!=32){
                    sb.append((char)ch);
                    ch=input.read();
                }
                return sb.toString();
            }catch (Exception e){
                e.printStackTrace();
            }
        }
        while(st==null || !st.hasMoreElements())//回车，空行情况
        {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    public int nextInt()
    {
        return (int)nextLong();
    }

    public long nextLong() {
        try {
            if(input!=null){
                long ret=0;
                int b=input.read();
                while(b<'0'||b>'9'){
                    b=input.read();
                }
                while(b>='0'&&b<='9'){
                    ret=ret*10+b;
                    b=input.read();
                }
                return ret;
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        return Long.parseLong(next());
    }

    public double nextDouble()
    {
        return Double.parseDouble(next());
    }
}