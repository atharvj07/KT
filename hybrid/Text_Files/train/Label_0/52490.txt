import java.io.*;
import java.util.*;
import java.math.*;
// import java.awt.Point;
 
public class Main {
    InputStream is;
    PrintWriter out;
    String INPUT = "";
 
    static int mod = 1_000_000_007;
    // int mod = 998244353;
    // long inf = Long.MAX_VALUE/2;
    int inf = Integer.MAX_VALUE/2;

    void solve(){
        int n = ni();
        int k = ni();
        int[] p = new int[n];
        for(int i = 0; i < n; i++){
            p[i] = ni();
        }
        SegmentTree seg1 = new SegmentTree(n);
        SegmentTree2 seg2 = new SegmentTree2(n);
        int c = 0;
        int d = -1;
        for(int i = 0; i < k-1; i++){
            seg1.update(p[i],p[i],0);
            seg2.update(p[i],p[i],0);
            if(p[i]>d){
                c++;
                d = p[i];
            }
            else{
                c = 1;
                d = p[i];
            }
        }
        int l = n;
        int ans = 0;
        boolean flag = false;
        for(int i = k-1; i < n; i++){
            int mi = seg1.query(0,n)[0];
            int ma = seg2.query(0,n)[0];
            if(p[i]>d){
                c++;
                d = p[i];
            }
            else{
                c = 1;
                d = p[i];
            }
            if(i>=k) l = p[i-k];
            int r = p[i];
            if(l>mi||r<ma){
                if(!flag||(flag&&c<k)) ans++;
            }
            if(c>=k) flag = true;
            // System.err.println(mi+" "+ma+" "+ans+" "+c);
            seg1.update(p[i-k+1],inf,0);
            seg1.update(p[i],p[i],0);
            seg2.update(p[i-k+1],-1,0);
            seg2.update(p[i],p[i],0);
        }
        // int mi = seg1.query(0,n)[0];
        // int ma = seg2.query(0,n)[0];
        // l = p[n-k];
        // int r = n;
        // if(l>mi||r<ma) ans++;
        out.println(ans);
    }

    class SegmentTree {
        int n;
        int[][] seg;
        SegmentTree(int n) {
            this.n = Integer.highestOneBit(n) << 1;
            this.seg = new int[this.n<<1][2];
            for(int i=0;i<(this.n<<1);++i){
                seg[i][0] = inf;
                seg[i][1] = -1;
            }
        }
        int[] comb(int[] ans1, int[] ans2){
            if(ans1[0]<=ans2[0]){
                return new int[]{ans1[0], ans1[1]};
            }
            return new int[]{ans2[0], ans2[1]};
        }
        void update(int x, int value, int id) {
            x += n - 1;
            this.seg[x][0] = value;
            this.seg[x][1] = id;
            while (x > 0) {
                x = (x - 1) / 2;
                this.seg[x] = comb(this.seg[2 * x + 1], this.seg[2 * x + 2]);
            }
        }
        int[] query(int a,int b,int l,int r,int k){
            if(a<=l&&r<=b) return seg[k];
            if(b<=l||r<=a) return new int[]{inf, -1};
            int[] ans1=query(a,b,l,(l+r)/2,2*k+1);
            int[] ans2=query(a,b,(l+r)/2,r,2*k+2);
            return comb(ans1, ans2);
        }
        int[] query(int l, int r) {
            return query(l,r,0,n,0);
        }
    }

    class SegmentTree2 {
        int n;
        int[][] seg;
        SegmentTree2(int n) {
            this.n = Integer.highestOneBit(n) << 1;
            this.seg = new int[this.n<<1][2];
            for(int i=0;i<(this.n<<1);++i){
                seg[i][0] = -1;
                seg[i][1] = -1;
            }
        }
        int[] comb(int[] ans1, int[] ans2){
            if(ans1[0]>=ans2[0]){
                return new int[]{ans1[0], ans1[1]};
            }
            return new int[]{ans2[0], ans2[1]};
        }
        void update(int x, int value, int id) {
            x += n - 1;
            this.seg[x][0] = value;
            this.seg[x][1] = id;
            while (x > 0) {
                x = (x - 1) / 2;
                this.seg[x] = comb(this.seg[2 * x + 1], this.seg[2 * x + 2]);
            }
        }
        int[] query(int a,int b,int l,int r,int k){
            if(a<=l&&r<=b) return seg[k];
            if(b<=l||r<=a) return new int[]{-1, -1};
            int[] ans1=query(a,b,l,(l+r)/2,2*k+1);
            int[] ans2=query(a,b,(l+r)/2,r,2*k+2);
            return comb(ans1, ans2);
        }
        int[] query(int l, int r) {
            return query(l,r,0,n,0);
        }
    }

    void run() throws Exception
    {
        is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);
        long s = System.currentTimeMillis();
        solve();
        out.flush();
        if(!INPUT.isEmpty())tr(System.currentTimeMillis()-s+"ms");
    }
    
    public static void main(String[] args) throws Exception { new Main().run(); }
    
    private byte[] inbuf = new byte[1024];
    private int lenbuf = 0, ptrbuf = 0;
    
    private int readByte()
    {
        if(lenbuf == -1)throw new InputMismatchException();
        if(ptrbuf >= lenbuf){
            ptrbuf = 0;
            try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
            if(lenbuf <= 0)return -1;
        }
        return inbuf[ptrbuf++];
    }
    
    private boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
    private int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
    
    private double nd() { return Double.parseDouble(ns()); }
    private char nc() { return (char)skip(); }
    
    private String ns()
    {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while(!(isSpaceChar(b) && b != ' ')){
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    
    private char[] ns(int n)
    {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while(p < n && !(isSpaceChar(b))){
            buf[p++] = (char)b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }
    
    private char[][] nm(int n, int m)
    {
        char[][] map = new char[n][];
        for(int i = 0;i < n;i++)map[i] = ns(m);
        return map;
    }
    
    private int[] na(int n)
    {
        int[] a = new int[n];
        for(int i = 0;i < n;i++)a[i] = ni();
        return a;
    }
    
    private int ni()
    {
        int num = 0, b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private long nl()
    {
        long num = 0;
        int b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private static void tr(Object... o) { System.out.println(Arrays.deepToString(o)); }
 
}
