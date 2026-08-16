import com.sun.org.apache.xml.internal.utils.StringComparable;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) {
//     Test.testing();
        ConsoleIO io = new ConsoleIO();
        new Main(io).solve();
        io.flush();
    }

    ConsoleIO io;

    Main(ConsoleIO io) {
        this.io = io;
    }

    ArrayList<ArrayList<Integer>> gr;
    boolean[] visit;

    class Pair {
        public Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }

        public int a; // index
        public int b; // cost
    }

    class Edge {
        public Edge(int u, int v, int c) {
            this.u = u;
            this.v = v;
            this.c = c;
        }

        public int u;
        public int v;
        public int c;
    }

    long MOD = 1_000_000_007;
    int n, m, k;
    int[][] map;
    int move, change, time;

    public void solve() {
        int[] l = io.readIntArray();
        n = l[0];
        k = l[1];
        l = io.readIntArray();
        int a = l[0],b = l[1],c = l[2], d = l[3];
        if (n == 4 || k < n + 1) {
            io.writeLine("-1");
            return;
        }

        int[] res = new int[n];
        res[0] = a;
        res[1] = c;
        res[n-2] = d;
        res[n-1] = b;
        boolean[] used = new boolean[n+1];
        used[a]=used[b] = used[c] = used[d] = true;
        for(int i = 2;i<n-2;i++) {
            for (int j = 1; j < used.length; j++)
                if (!used[j]) {
                    res[i] = j;
                    used[j] = true;
                    break;
                }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0;i<res.length;i++){
            if(sb.length()>0)sb.append(' ');
            sb.append(res[i]);
        }
        io.writeLine(sb.toString());

        res[0] = c;
        res[1] = a;
        res[n-2] = b;
        res[n-1] = d;
        sb = new StringBuilder();
        for(int i = 0;i<res.length;i++){
            if(sb.length()>0)sb.append(' ');
            sb.append(res[i]);
        }
        io.writeLine(sb.toString());

    }

    class Brack{
        public Brack(int d){
            this.dir = d;
        }
        public int dir;
        public Brack left;
        public Brack right;
    }

    long gcd(long a, long b) {
        if (a < b) return gcd(b, a);
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}

class ConsoleIO {
    BufferedReader br;
    PrintWriter out;
    public ConsoleIO(){br = new BufferedReader(new InputStreamReader(System.in));out = new PrintWriter(System.out);}
    public void flush(){this.out.close();}
    public void writeLine(String s) {this.out.println(s);}
    public void writeInt(int a) {this.out.print(a);this.out.print(' ');}
    public void writeWord(String s){
        this.out.print(s);
    }
    public int read(char[] buf, int len){try {return br.read(buf,0,len);}catch (Exception ex){ return -1; }}
    public String readLine() {try {return br.readLine();}catch (Exception ex){ return "";}}
    public long readLong() {
        return Long.parseLong(this.readLine());
    }
    public int readInt() {
        return Integer.parseInt(this.readLine().trim());
    }
    public long[] readLongArray() {
        String[]n=this.readLine().trim().split("\\s+");long[]r=new long[n.length];
        for(int i=0;i<n.length;i++)r[i]=Long.parseLong(n[i]);
        return r;
    }
    public int[] readIntArray() {
        String[]n=this.readLine().trim().split("\\s+");int[]r=new int[n.length];
        for(int i=0;i<n.length;i++)r[i]=Integer.parseInt(n[i]);
        return r;
    }
    public void writeIntArray(int[] a) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {if (i > 0) sb.append(' ');sb.append(a[i]);}
        this.writeLine(sb.toString());
    }
}


