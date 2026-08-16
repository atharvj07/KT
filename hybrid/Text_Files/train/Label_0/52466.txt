import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.*;


// written by luchy0120

public class Main {
    public static void main(String[] args) throws Exception {

        new Main().run();
    }


    long sum(long r,long a,long b){

        long bb = r/b;
        // [ 0, bb]
        if(bb%a!=0){
            return r +1 - (bb/a+1)*(b);
        }else{
            return r - ((bb)/a)*b  - r%b;
        }

    }

    int gcd(int a,int b){
        return b==0?a:gcd(b,a%b);
    }



    public class Solution {
        /**
         * @param position: the position of circle A,B and point P.
         * @return: if two circle intersect return 1, otherwise -1.
         */


        double dis(double x1,double y1,double x2,double y2){
            if(Math.abs(x1-x2)>10000||Math.abs(y1-y2)>10000){
                return 50000;
            }
            return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
        }



        public int IfIntersect(double[] p) {
            //

            double x = p[0];
            double y = p[1];
            double r1 = p[2];

            double x1 = p[3];
            double y1 = p[4];
            double r2 = p[5];


            double c1 = p[6];
            double c2 = p[7];





            double dis1 = dis(x1,y1,c1,c2);
            double dis2 = dis(x1,y1,x,y);



            if(dis1<=(r1+r2)*(r1+r2)){
                return 1;
            }
            if(dis2<=(r1+r2)*(r1+r2)){
                return 1;
            }

            double dx1 = x1-c1;
            double dy1 = y1-c2;
            double dx2 = x-c1;
            double dy2  =y-c2;

            double jj = dx1*dx2+dy2*dy1;


            dx1 = x1-x;
            dy1 = y1-y;
            dx2 = c1-x;
            dy2 = c2-y;

            double jj1 = dx1*dx2+dy2*dy1;

            if(jj>0&&jj1>0){





                double mj = s(x,y,c1,c2,x1,y1);

                double dis = (x-c1)*(x-c1)+(y-c2)*(y-c2);


                double ht = mj*mj/dis;

                if(ht>(r1+r2)*(r1+r2)){
                    return -1;
                }
                return 1;
            }else{

                return -1;
            }




        }


        //S=(1/2)* | (x1y2+x2y3+x3y1-x2y1-x3y2-x1y3) |

        public  double s(double x1,double y1,double x2,double y2,double x3,double y3){
            return Math.abs(x1*y2-x1*y3+x2*y3-x2*y1+x3*y1-x3*y2);
        }
    }







    int dp[] = new int[1000001];
    int mx =0 ;
    void go(int rt,int fa){
        dp[rt] = c[rt];
        List<Integer> li = new ArrayList<>();
        for(int i=h[rt];i!=-1;i=ne[i]){
            if(to[i]==fa) continue;
            go(to[i],rt);
            li.add(wt[i]+dp[to[i]]);
            mx = Math.max(mx,c[rt]+wt[i]+dp[to[i]]);
            dp[rt] = Math.max(dp[rt], wt[i]+dp[to[i]]);
        }
        Collections.sort(li);
        if(li.size()>=2){
            mx = Math.max(mx,li.get(li.size()-1)+li.get(li.size()-2));
        }
    }




    void add(int a,int b,int w){
        to[ct] = b;
        ne[ct] = h[a];
        wt[ct] = w;
        h[a] = ct++;
    }


    int[] h,wt,ne,to,c;
    int ct =0;
    long f[];


    int getId(long v){
        int lo = 0;
        int hi = p-1;
        while(lo<hi){
            int mid = (lo+hi)/2;
            if(f[mid]<v){
                lo = mid+1;
            }else{
                hi = mid;
            }
        }
        return lo;
    }
    long inv(long a, long MOD) {
        //return fpow(a, MOD-2, MOD);
        return a==1?1:(long )(MOD-MOD/a)*inv(MOD%a, MOD)%MOD;
    }

    int p  =0;
    void solve() {
        int n  = ni();
        long a[] = nal(n+1);
        if(a[0]>1){
            println(-1);return;
        }else if(a[0]==1){
            for(int j=1;j<=n;++j){
                if(a[j]!=0){
                    println(-1);return;
                }
            }
            println(1);return;
        }



        long s = 0;
        for(long u:a) s += u;


        long k = 1;
        long sum  = s;
        for(int d=1;d<=n;++d){
            sum += k;
            k = 2*k;
            if(k<a[d]){
                println(-1);return;
            }
            k -= a[d];
            s -= a[d];
            k = Math.min(k,s);
        }
        println(sum);







    }

    double dis(long x,long y,long a,long b){
        long v = (x-a)*(x-a)+(y-b)*(y-b);
        return Math.sqrt(v);
    }







    InputStream is;
    PrintWriter out;

    void run() throws Exception {
        //is = new FileInputStream(new File("C:\\Users\\Luqi\\Downloads\\P3387_9.in"));
        is = System.in;
        out = new PrintWriter(System.out);

        solve();
        out.flush();
    }

    private byte[] inbuf = new byte[1024];
    public int lenbuf = 0, ptrbuf = 0;

    private int readByte() {
        if (lenbuf == -1) throw new InputMismatchException();
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) return -1;
        }
        return inbuf[ptrbuf++];
    }

    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }

    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b)) ;
        return b;
    }

    private double nd() {
        return Double.parseDouble(ns());
    }

    private char nc() {
        return (char) skip();
    }

    private char ncc() {
        int b = readByte();
        return (char) b;
    }

    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) { // when nextLine, (isSpaceChar(b) && b != ' ')
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }

    private String nline() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!isSpaceChar(b) || b == ' ') {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[][] nm(int n, int m) {
        char[][] a = new char[n][];
        for (int i = 0; i < n; i++) a[i] = ns(m);
        return a;
    }

    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = ni();
        return a;
    }

    private long[] nal(int n) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = nl();
        return a;
    }

    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) {
        }
        ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (true) {
            if (b >= '0' && b <= '9') num = (num << 3) + (num << 1) + (b - '0');
            else return minus ? -num : num;
            b = readByte();
        }
    }

    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) {
        }
        ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (true) {
            if (b >= '0' && b <= '9') num = num * 10 + (b - '0');
            else return minus ? -num : num;
            b = readByte();
        }
    }

    void print(Object obj) {
        out.print(obj);
    }

    void println(Object obj) {
        out.println(obj);
    }

    void println() {
        out.println();
    }

    void printArray(int a[],int from){
        int l = a.length;
        for(int i=from;i<l;++i){
            print(a[i]);
            if(i!=l-1){
                print(" ");
            }
        }
        println();
    }

    void printArray(long a[],int from){
        int l = a.length;
        for(int i=from;i<l;++i){
            print(a[i]);
            if(i!=l-1){
                print(" ");
            }
        }
        println();
    }
}