
//package C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Solution {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int n, an;
    int[][] e;
    int[] en;    
    int[] a;
    boolean[] used;
    public TreeSet<Integer>[] g;
    
    public String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }
    
    public int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
    
    boolean exist(int u, int v) {
        return (g[u].contains(v));           
    }
    
    void addEdge(int u, int v) {
        g[u].add(v); g[v].add(u);
        if (en[u] < 4) e[u][en[u]] = v;        
        if (en[v] < 4) e[v][en[v]] = u;
        ++en[u]; ++en[v];
    }
    
    void rec(int u) {
        a[an++] = u;
        used[u] = true;
        if (an == n) {
            boolean ok = true;
            for (int i = 0; i < an; ++i) {
                int x = a[i];
                int y = a[(i + 1) % n];
                if (!exist(x, y)) ok = false;
                y = a[(i + 2) % n];
                if (!exist(x, y)) ok = false;                
            }
            if (ok) {
                for (int i = 0; i < an; ++i) {
                    if (i > 0) System.out.print(' ');
                    System.out.print(a[i] + 1);
                }                    
                System.out.println();
                System.exit(0);
            } 
            --an;
            used[u] = false;
            return;
        }
        for (int i = 0; i < en[u]; ++i) {
            int v = e[u][i];
            if (!used[v]) {
                rec(v);
            }
        }
        used[u] = false;
        --an;
    }
    
    void go(int u) {
        a[an++] = u;
        used[u] = true;
        for (int i = 0; i < 2; ++i) {
            int v = e[u][i];
            if (!used[v]) {
                go(v);
                break;
            }
        }
    }
    
    void run() throws Exception {
        n = nextInt();
        e = new int[n][4];
        en = new int[n];
        g = new TreeSet[n];
        
        for (int i = 0; i < n; ++i)
            g[i] = new TreeSet();
        
        for (int i = 0; i < 2 * n; ++i) {
            int u = nextInt() - 1;
            int v = nextInt() - 1;
            addEdge(u, v);
        }
        boolean flag = true;
        for (int i = 0; i < n; ++i) if (en[i] != 4)
            flag = false;
        if (!flag) {
            System.out.println(-1);
            System.exit(0);
        }
        
        used = new boolean[n];
        a = new int[n + 1];
        if (n <= 7) {            
            rec(0);
            System.out.println(-1);
            System.exit(0);
        }
        
        for (int x = 0; x < n; ++x) {
            int y = -1, z = -1;
            for (int j = 0; j < en[x]; ++j) {
                int u = e[x][j];
                int dg = 0;
                for (int k = 0; k < en[x]; ++k) {
                    int v = e[x][k];
                    if (exist(u, v)) ++dg;
                }
                if (dg == 2) {
                    if (y == -1) y = u;
                    else z = u;
                }
            }
            if (y == -1 || z == -1) {
                System.out.println(-1);
                System.exit(0);
            }
            int k = -1, l = -1;
            for (int j = 0; j < en[x]; ++j) {
                int u = e[x][j];
                if (u != y && u != z && exist(y, u))
                    k = u;
            }
            for (int j = 0; j < en[x]; ++j) {
                int u = e[x][j];
                if (u != y && u != z && exist(z, u))
                    l = u;
            }
            if (k == -1 || l == -1) {
                System.out.println(-1);
                System.exit(0);
            }
            e[x][0] = y;
            e[x][1] = z;
            e[x][2] = k;
            e[x][3] = l;
        }
        go(0);
        if (an != n) {
            System.out.println(-1);            
        }
        else {
            boolean ok = true;
            for (int i = 0; i < an; ++i) {
                int x = a[i];
                int y = a[(i + 1) % n];
                if (!exist(x, y)) ok = false;
                y = a[(i + 2) % n];
                if (!exist(x, y)) ok = false;                
            }            
            if (!ok) {
                System.out.println(-1);
                System.exit(0);
            }
            for (int i = 0; i < an; ++i) {
                if (i > 0) System.out.print(' ');
                System.out.print(a[i] + 1);
            }
            System.out.println();
        }
    }
    public static void main(String args[]) throws Exception {
        new Solution().run();
    }
}
