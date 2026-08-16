import java.io.*;
import java.util.*;
import java.math.BigDecimal;

@SuppressWarnings("unused")
public class Main {
    FastScanner in;
    PrintWriter out;
    final static int MOD = (int)1e9+7;
    
    void solve(){
        int N = in.nextInt(), Q = in.nextInt();
        int[] c = in.nextIntArray1Index(N);
        int[][] lr = new int[Q][3];
        int[] ans = new int[Q];
        for(int i = 0; i < Q; i++){
            lr[i][0] = in.nextInt();
            lr[i][1] = in.nextInt();
            lr[i][2] = i;
        }
        
        Arrays.sort(lr, (e1, e2)->Integer.compare(e1[1], e2[1]));
        DualSegmentTree tree = new DualSegmentTree(N+1, 0);
        int[] p = new int[N+1];
        int idx = 0;
        for(int i = 1; i <= N && idx < Q; i++){
            tree.setSegment(p[c[i]] + 1, i + 1, 1);
            p[c[i]] = i;
            
            while(idx < Q && lr[idx][1] == i){
                ans[lr[idx][2]] = (int)tree.getPoint(lr[idx][0]);
                idx++;
            }
        }
        
        for(int v : ans){
            out.println(v);
        }
    }
    
    class DualSegmentTree{
        int d;
        long[] node;
        
        /*作用素で使える単位元*/
        private long e = 0;
        
        /*結合律が成り立ち、更新が可換であるような、各要素への作用素*/
        private long f(long nodeVal, long val){
            return nodeVal + val;
        }
        
        /* 単位元で初期化 */
        public DualSegmentTree(int sz, long e){
            long[] v = new long[sz];
            Arrays.fill(v, e);
            init(v, e);
        }
        
        /* 配列vで初期化 */
        public DualSegmentTree(long[] v, long e){
            init(v, e);
        }
        
        private void init(long[] v, long e){
            this.e = e;
            d = 1;
            while(d < v.length) d *= 2;
            node = new long[2*d];
            Arrays.fill(node, e);
            for(int i = 0; i < v.length; i++)
                node[i+d] = v[i];
        }
        
        /* 0-indexed:xの要素を取得する */
        public long getPoint(int x){
            x += d;
            long res = node[x];
            while(x > 1){
                x = x / 2;
                res = f(res, node[x]);
            }
            return res;
        }
        
        /* 指定した区間[L,R)に含まれるすべての要素に作用素を適用するクエリ */
        public void setSegment(int L, int R, long val){
            L += d;
            R += d;
            while (L < R) {
                if ((L & 1) != 0){
                    node[L] = f(node[L], val);
                    L++;
                }
                if ((R & 1) != 0){
                    --R;
                    node[R] = f(node[R], val);
                }
                L >>= 1;
                R >>= 1;
            }
        }
    }
    
    public static void main(String[] args) {
        new Main().m();
    }
    
    private void m() {
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);
        /*
        try {
            String path = "input.txt";
            out = new PrintWriter(new BufferedWriter(new FileWriter(new File(path))));
        }catch (IOException e){
            e.printStackTrace();
        }
        */
        solve();
        out.flush();
        in.close();
        out.close();
    }
    
    static class FastScanner {
        private Reader input;
        
        public FastScanner() {this(System.in);}
        public FastScanner(InputStream stream) {this.input = new BufferedReader(new InputStreamReader(stream));}
        public void close() {
            try {
                this.input.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        public int nextInt() {
            long nl = nextLong();
            if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
            return (int) nl;
        }
        
        public long nextLong() {
            try {
                int sign = 1;
                int b = input.read();
                while ((b < '0' || '9' < b) && b != '-' && b != '+') {
                    b = input.read();
                }
                if (b == '-') {
                    sign = -1;
                    b = input.read();
                } else if (b == '+') {
                    b = input.read();
                }
                long ret = b - '0';
                while (true) {
                    b = input.read();
                    if (b < '0' || '9' < b) return ret * sign;
                    ret *= 10;
                    ret += b - '0';
                }
            } catch (IOException e) {
                e.printStackTrace();
                return -1;
            }
        }
        
        public double nextDouble() {
            try {
                double sign = 1;
                int b = input.read();
                while ((b < '0' || '9' < b) && b != '-' && b != '+') {
                    b = input.read();
                }
                if (b == '-') {
                    sign = -1;
                    b = input.read();
                } else if (b == '+') {
                    b = input.read();
                }
                double ret = b - '0';
                while (true) {
                    b = input.read();
                    if (b < '0' || '9' < b) break;
                    ret *= 10;
                    ret += b - '0';
                }
                if (b != '.') return sign * ret;
                double div = 1;
                b = input.read();
                while ('0' <= b && b <= '9') {
                    ret *= 10;
                    ret += b - '0';
                    div *= 10;
                    b = input.read();
                }
                return sign * ret / div;
            } catch (IOException e) {
                e.printStackTrace();
                return Double.NaN;
            }
        }
        
        public char nextChar() {
            try {
                int b = input.read();
                while (Character.isWhitespace(b)) {
                    b = input.read();
                }
                return (char) b;
            } catch (IOException e) {
                e.printStackTrace();
                return 0;
            }
        }
        
        public String nextStr() {
            try {
                StringBuilder sb = new StringBuilder();
                int b = input.read();
                while (Character.isWhitespace(b)) {
                    b = input.read();
                }
                while (b != -1 && !Character.isWhitespace(b)) {
                    sb.append((char) b);
                    b = input.read();
                }
                return sb.toString();
            } catch (IOException e) {
                e.printStackTrace();
                return "";
            }
        }
        
        public String nextLine() {
            try {
                StringBuilder sb = new StringBuilder();
                int b = input.read();
                while (b != -1 && b != '\n') {
                    sb.append((char) b);
                    b = input.read();
                }
                return sb.toString();
            } catch (IOException e) {
                e.printStackTrace();
                return "";
            }
        }
        
        public int[] nextIntArray(int n) {
            int[] res = new int[n];
            for (int i = 0; i < n; i++) {
                res[i] = nextInt();
            }
            return res;
        }
        
        public int[] nextIntArrayDec(int n) {
            int[] res = new int[n];
            for (int i = 0; i < n; i++) {
                res[i] = nextInt() - 1;
            }
            return res;
        }
        
        public int[] nextIntArray1Index(int n) {
            int[] res = new int[n + 1];
            for (int i = 0; i < n; i++) {
                res[i + 1] = nextInt();
            }
            return res;
        }
        
        public long[] nextLongArray(int n) {
            long[] res = new long[n];
            for (int i = 0; i < n; i++) {
                res[i] = nextLong();
            }
            return res;
        }
        
        public long[] nextLongArrayDec(int n) {
            long[] res = new long[n];
            for (int i = 0; i < n; i++) {
                res[i] = nextLong() - 1;
            }
            return res;
        }
        
        public long[] nextLongArray1Index(int n) {
            long[] res = new long[n + 1];
            for (int i = 0; i < n; i++) {
                res[i + 1] = nextLong();
            }
            return res;
        }
        
        public double[] nextDoubleArray(int n) {
            double[] res = new double[n];
            for (int i = 0; i < n; i++) {
                res[i] = nextDouble();
            }
            return res;
        }
    }
}