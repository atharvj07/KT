/**
 * Created by Baelish on 5/29/2018.
 */

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Stream;

import static java.lang.Math.*;

public class D {
    public static void main(String[] args) throws Exception {
        FastReader in = new FastReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int n = in.nextInt(), m = in.nextInt(), s = in.nextInt(), k = in.nextInt();

        int from[] = new int[m], to[] = new int[m];
        vis = new int[n+1];
        q = new int[n+1];

        list = genArrayList(s+1);
        cost = new int[n+1][s+1];
        int inf = (int)1e8;

        for (int i = 1; i <= n; i++) {
            int c = in.nextInt();
            list[c].add(i);
            Arrays.fill(cost[i], inf);
        }

        for (int i = 0; i < m; i++) {
            int u = in.nextInt();
            int v = in.nextInt();
            from[i] = u; to[i] = v;
        }

        g = packU(n+1, from, to);

        for(int i = 1; i <= s; i++){
            bfs(i, n);
        }

        for(int i = 1; i <= n; i++){
            Arrays.sort(cost[i]);
            long ans = 0;
            for(int j = 0; j < k; j++){
                ans += cost[i][j];
            }
            pw.print(ans+" ");
        }
        pw.println();


        pw.close();
    }

    static List<Integer> list[];
    static int g[][];
    static int cost[][];


    static int vis[], q[];
    static void bfs(int color, int n){
        Arrays.fill(vis, -1);
        int qs = 0, qe = 0;
        for(int i : list[color]){
            vis[i] = 0;
            q[qe++] = i;
            cost[i][color] = 0;
        }

        while (qs < qe){
            int p = q[qs++];
            for(int u : g[p]){
                if(vis[u] == -1){
                    vis[u] = vis[p]+1;
                    cost[u][color] = vis[u];
                    q[qe++] = u;
                }
            }
        }
    }


    static int[][] packU(int n, int[] from, int[] to) {
        int[][] g = new int[n][];
        int[] p = new int[n];
        for (int f : from)
            p[f]++;
        for (int t : to)
            p[t]++;
        for (int i = 0; i < n; i++)
            g[i] = new int[p[i]];
        for (int i = 0; i < from.length; i++) {
            g[from[i]][--p[from[i]]] = to[i];
            g[to[i]][--p[to[i]]] = from[i];
        }
        return g;
    }

    public static <E> List<E>[] genArrayList(int size) {
        return Stream.generate(ArrayList::new).limit(size).toArray(List[]::new);
    }

    static void debug(Object... obj) {
        System.err.println(Arrays.deepToString(obj));
    }

    static class FastReader {
        InputStream is;
        private byte[] inbuf = new byte[1024];
        private int lenbuf = 0, ptrbuf = 0;
        static final int ints[] = new int[128];

        public FastReader(InputStream is) {
            for (int i = '0'; i <= '9'; i++) ints[i] = i - '0';
            this.is = is;
        }

        public int readByte() {
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

        public boolean isSpaceChar(int c) {
            return !(c >= 33 && c <= 126);
        }

        public int skip() {
            int b;
            while ((b = readByte()) != -1 && isSpaceChar(b)) ;
            return b;
        }

        public String next() {
            int b = skip();
            StringBuilder sb = new StringBuilder();
            while (!(isSpaceChar(b))) { // when nextLine, (isSpaceChar(b) && b != ' ')
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }

        public int nextInt() {
            int num = 0, b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + ints[b];
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public long nextLong() {
            long num = 0;
            int b;
            boolean minus = false;
            while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
            if (b == '-') {
                minus = true;
                b = readByte();
            }

            while (true) {
                if (b >= '0' && b <= '9') {
                    num = (num << 3) + (num << 1) + ints[b];
                } else {
                    return minus ? -num : num;
                }
                b = readByte();
            }
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
       /* public char nextChar() {
            return (char)skip();
        }*/

        public char[] next(int n) {
            char[] buf = new char[n];
            int b = skip(), p = 0;
            while (p < n && !(isSpaceChar(b))) {
                buf[p++] = (char) b;
                b = readByte();
            }
            return n == p ? buf : Arrays.copyOf(buf, p);
        }

        /*private char buff[] = new char[1005];
        public char[] nextCharArray(){
            int b = skip(), p = 0;
            while(!(isSpaceChar(b))){
                buff[p++] = (char)b;
                b = readByte();
            }
            return Arrays.copyOf(buff, p);
        }*/
    }
}