import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class MainD
{

    static int mod = (int) (1e9+7);
    static InputReader in;
    static PrintWriter out;
    
    static class SegmentTree {
        long st[];
        long lazy[];
 
        SegmentTree(int n)  {
            st = new long[4*n];
            lazy = new long[4*n];
            build(0, n - 1, 1);
        }
        
        int getMid(int s, int e) {
            return (s+e)>>1;
        }
        
        void lazyupdate(int ss,int ee,int si){
            if(lazy[si] != 0){
                if(ss != ee){
                    lazy[2*si] += lazy[si];
                    lazy[2*si+1] += lazy[si];
                }
                st[si] += (ee-ss+1) * lazy[si];
                lazy[si] = 0;
            }
        }

        long merge(long a,long b){
            return a + b;
        }
        
        void update(int s, int e, int x, int y, long c, int si){
            if(s == x && e == y){
                lazy[si] += c;
            }
            else{
                lazyupdate(s, e, si);
                int mid = getMid(s, e);
                if(y <= mid)    
                    update(s, mid, x, y, c, 2*si);
                else if(x > mid)
                    update(mid + 1, e, x ,y ,c ,2*si + 1);
                else{
                    update(s, mid, x, mid, c, 2*si);
                    update(mid + 1, e, mid + 1, y, c, 2*si + 1);
                }
                lazyupdate(s, mid, 2*si);
                lazyupdate(mid + 1, e, 2*si + 1);
                st[si] = merge(st[2*si],st[2*si+1]);
            }
        }

        long  get(int s, int e, int x, int y, int si){

            lazyupdate(s, e,si);
            if(s == x && e == y){
                return st[si];
            }
            int mid = getMid(s, e);
            if(y <= mid)
                return get(s, mid, x, y, 2*si);
            else if(x > mid)
                return get(mid + 1, e, x, y, 2*si + 1);
            return merge(get(s, mid, x, mid, 2*si), get(mid + 1, e, mid + 1, y, 2*si + 1));
        }

        void build(int ss, int se, int si){
            if (ss == se) {
                st[si] = 0;
                lazy[si] = 0;
                return;
            }

            int mid = getMid(ss, se);
            build(ss, mid, si * 2 );
            build(mid + 1, se, si * 2 + 1);
            lazy[si] = 0;
            st[si] = merge(st[2*si],st[2*si+1]);
        }
        
        void build(int ss, int se, int si,int[] arr){
            if (ss == se) {
                st[si] = arr[ss];
                lazy[si] = 0;
                return;
            }

            int mid = getMid(ss, se);
            build(ss, mid, si * 2 ,arr);
            build(mid + 1, se, si * 2 + 1,arr);
            lazy[si] = 0;
            st[si] = merge(st[2*si],st[2*si+1]);
        }
    }
    
    static ArrayList<Integer>[] g;
    static int t,time;    
    static int[] chainHead;
    static int[][] up;
    static int[] tin;
    static int[] tout;
    static int[] st;
    static int[] et;
    static int len; 
    static int[] depth;
    static SegmentTree seg;
    
    static void dfs(int u,int p){
        tin[u] = time++;
        st[u] = t++;
        up[0][u] = p;
        for (int i = 1; i < len; i++)
          up[i][u] = up[i - 1][up[i - 1][u]];

        for(int v : g[u]){
            if(v != p) {
                depth[v] = depth[u] + 1;
                dfs(v,u);
            }
        }
        tout[u] = time++;
        et[u] = t - 1;
    }
    
    static boolean isParent(int parent, int child) {
        return tin[parent] <= tin[child] && tout[child] <= tout[parent];
    }

    static int lca(int a, int b) {
        if (isParent(a, b))
            return a;
        if (isParent(b, a))
            return b;
        for (int i = len - 1; i >= 0; i--)
            if (!isParent(up[i][a], b))
                a = up[i][a];
        return up[0][a];
    }
    
    static int get(int u, int x){
        
        for(int i = len - 1; i >= 0; i--){
            if(x >= (1 << i)){
                u = up[i][u];
                x -= 1 << i;
            }
        }
        
        return u;
    }
    
    static int dis(int u, int v){
        return depth[u] + depth[v] - 2 * depth[lca(u,v)];
    }
    
    public static void main(String[] args)
    {

        in = new InputReader(System.in);
        out = new PrintWriter(System.out);       
        
        int n = in.nextInt();
        int q = in.nextInt();
        long[] arr = new long[n];
        g = new ArrayList[n];
        len = 18;
        up = new int[len][n];
        st = new int[n];
        et = new int[n];
        tin = new int[n];
        tout = new int[n];
        chainHead = new int[n];
        depth = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = in.nextLong();
            g[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < n - 1; i++){
            int u = in.nextInt() - 1;
            int v = in.nextInt() - 1;
            g[u].add(v);
            g[v].add(u);
        }
        int root = 0;
        dfs(root, root);
        seg = new SegmentTree(t);
        
        for(int i = 0; i < n; i++){
            seg.update(0, t - 1, st[i], st[i], arr[i], 1);
        }
        
        while(q-- > 0){
            int k = in.nextInt();
            if(k == 1){
                root = in.nextInt() - 1;
            }
            else if(k == 2){
                int u = in.nextInt() - 1;
                int v = in.nextInt() - 1;
                long x = in.nextInt();
                int luv = lca(u, v);
                int lur = lca(u, root);
                int lvr = lca(v, root);
                int com = luv ^ lur ^ lvr;
                if(com == root){
                    seg.update(0, t - 1, 0, t - 1, x, 1);
                }
                else if(isParent(com, root)){
                    seg.update(0, t - 1, 0, t - 1, x, 1);
                    int y = get(root, dis(com, root) - 1);
                    seg.update(0, t - 1, st[y], et[y], -x, 1);
                }
                else{
                    seg.update(0, t - 1, st[com], et[com], x, 1);
                }
            }
            else{
                int u = in.nextInt() - 1;
                long ans = 0;
                if(isParent(u, root) && u != root){
                    ans = seg.get(0, t - 1, 0, t - 1, 1);
                    int y = get(root, dis(u, root) - 1);
                    ans -= seg.get(0, t - 1, st[y], et[y], 1);
                }
                else if(u == root)
                    ans = seg.get(0, t - 1, 0, t - 1, 1);
                else
                    ans = seg.get(0, t - 1, st[u], et[u], 1);
                out.println(ans);
            }
            //debug(root);
        }
        
        out.close();        
    }
    
    static class Pair implements Comparable<Pair>
    {

        int x,y,k,i;

        Pair (int x,int y, int k)
        {
                this.x = x;
                this.y = y;
                this.k = k;
        }

        Pair (int x,int y, int k, int i)
        {
                this.x = x;
                this.y = y;
                this.k = k;
                this.i = i;
        }
        
        public int compareTo(Pair o)
        {
            return Integer.compare(this.k,o.k);
                //return 0;
        }

        public boolean equals(Object o)
        {
            if (o instanceof Pair)
            {
                Pair p = (Pair)o;
                return p.x == x && p.y==y;
            }
            return false;
        }

        @Override
        public String toString()
        {
            return x + " "+ y + " "+k;
        }

        /*public int hashCode()
        {
            return new Long(x).hashCode() * 31 + new Long(y).hashCode();
        }*/

    } 

    static long add(long a,long b){
        long x=(a+b);
        while(x>=mod) x-=mod;
        return x;
    }

    static long sub(long a,long b){
        long x=(a-b);
        while(x<0) x+=mod;
        return x;
    }
    
    static long mul(long a,long b){
        long x=(a*b);
        while(x>=mod) x-=mod;
        return x;
    }
    
    static String rev(String s){
        StringBuilder sb=new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }
    
    static long gcd(long x,long y)
    {
        if(y==0)
                return x;
        else
                return gcd(y,x%y);
    }

    static int gcd(int x,int y)
    {
        if(y==0)
                return x;
        else 
                return gcd(y,x%y);
    }

    static long pow(long n,long p,long m)
    {
         long  result = 1;
          if(p==0){
            return 1;
          }
          
        while(p!=0)
        {
            if(p%2==1)
                result *= n;
            if(result >= m)
               result %= m;
            p >>=1;
            n*=n;
            if(n >= m)
                n%=m;
        }
        
        return result;
    }

    static long pow(long n,long p)
    {
        long  result = 1;
          if(p==0)
            return 1;

        while(p!=0)
        {
            if(p%2==1)
                result *= n;	    
            p >>=1;
            n*=n;	    
        }
        return result;
    }

    static void debug(Object... o)
    {
            System.out.println(Arrays.deepToString(o));
    }

    static class InputReader
    {

        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
                this.stream = stream;
        }

        public int snext()
        {
                if (snumChars == -1)
                        throw new InputMismatchException();
                if (curChar >= snumChars)
                {
                        curChar = 0;
                        try
                        {
                                snumChars = stream.read(buf);
                        } catch (IOException e)
                        {
                                throw new InputMismatchException();
                        }
                        if (snumChars <= 0)
                                return -1;
                }
                return buf[curChar++];
        }

        public int nextInt()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                int res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public long nextLong()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                long res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public int[] nextIntArray(int n)
        {
                int a[] = new int[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextInt();
                }
                return a;
        }

        public long[] nextLongArray(int n)
        {
                long a[] = new long[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextLong();
                }
                return a;
        }

        public String readString()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isSpaceChar(c));
                return res.toString();
        }

        public String nextLine()
        {
                int c = snext();
                while (isSpaceChar(c))
                        c = snext();
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isEndOfLine(c));
                return res.toString();
        }

        public boolean isSpaceChar(int c)
        {
                if (filter != null)
                        return filter.isSpaceChar(c);
                return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c)
        {
                return c == '\n' || c == '\r' || c == -1;
        }

        public interface SpaceCharFilter
        {
                public boolean isSpaceChar(int ch);
        }

    }
}    
