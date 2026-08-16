import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.io.PrintWriter;

public class Main {
    static class Scanner {
        BufferedReader br;
        StringTokenizer tk = new StringTokenizer("");

        public Scanner(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        public int nextInt() throws IOException {
            if (tk.hasMoreTokens())
                return Integer.parseInt(tk.nextToken());
            tk = new StringTokenizer(br.readLine());
            return nextInt();
        }

        public long nextLong() throws IOException {
            if (tk.hasMoreTokens())
                return Long.parseLong(tk.nextToken());
            tk = new StringTokenizer(br.readLine());
            return nextLong();
        }

        public String next() throws IOException {
            if (tk.hasMoreTokens())
                return (tk.nextToken());
            tk = new StringTokenizer(br.readLine());
            return next();
        }

        public String nextLine() throws IOException {
            tk = new StringTokenizer("");
            return br.readLine();
        }

        public double nextDouble() throws IOException {
            if (tk.hasMoreTokens())
                return Double.parseDouble(tk.nextToken());
            tk = new StringTokenizer(br.readLine());
            return nextDouble();
        }

        public char nextChar() throws IOException {
            if (tk.hasMoreTokens())
                return (tk.nextToken().charAt(0));
            tk = new StringTokenizer(br.readLine());
            return nextChar();
        }

        public int[] nextIntArray(int n) throws IOException {
            int a[] = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        public long[] nextLongArray(int n) throws IOException {
            long a[] = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }

        public int[] nextIntArrayOneBased(int n) throws IOException {
            int a[] = new int[n + 1];
            for (int i = 1; i <= n; i++)
                a[i] = nextInt();
            return a;
        }

        public long[] nextLongArrayOneBased(int n) throws IOException {
            long a[] = new long[n + 1];
            for (int i = 1; i <= n; i++)
                a[i] = nextLong();
            return a;
        }


    }

    public static void main(String args[]) throws IOException {
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    solve();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();

    }
    static class Pair{
        long f;
        long s;
        Pair(long key, long value){
            f=key;
            s=value;
        }
        void add(Pair p){
            f+=p.f;
            s+=p.s;
        }
        void subtract(Pair p){
            f-=p.f;
            s-=p.s;
        }
    }
    static class BIT{
        HashMap<Integer, Pair> t;
        int n;
        BIT(int n){
            this.n=n+100;
            t=new HashMap<>();
        }
        void add(int i,Pair v){
            for(;i<n;i+=i&-i){
                Pair np=new Pair(0,0);
                Pair x=t.putIfAbsent(i,np);
                if(x==null)
                    x=np;
                x.add(v);
            }
        }
        Pair sum(int i){
            Pair sum=new Pair(0,0);
            for(;i>0;i-=i&-i){
                Pair xu=t.get(i);
                if(xu!=null)
                    sum.add(xu);
            }
            return sum;
        }
        Pair sum(int l, int r){
            Pair p=sum(r);
            p.subtract(sum(l-1));
            return p;
        }

    }
    static void solve() throws IOException {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int n=in.nextInt();
        int a[]=in.nextIntArrayOneBased(n);
        int pm[]=new int[n+1];
        pm[1]=0;
        for(int i=1;i<=n;i++){
            if(a[i]>a[pm[i-1]])
                pm[i]=i;
            else
                pm[i]=pm[i-1];
        }
        long count=0;
        int lst=n;
        int vp=pm[n];
        long ans[]=new long[n+1];
        BIT b1=new BIT(1000000000);
        do{
            while (lst>=vp){
               b1.add(a[lst],new Pair(1,a[lst]));
               lst--;
            }
            Pair pv=b1.sum(a[pm[vp-1]],1000000001);
            long vpz=pv.s-pv.f*a[pm[vp-1]]-count;
            ans[vp]+=vpz;
            count+=vpz;
            vp=pm[vp-1];



        }while (vp>0);
        for(int i=1;i<=n;i++)
            out.println(ans[i]);

        out.close();

    }
}
