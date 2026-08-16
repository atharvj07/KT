import java.io.*;
import java.util.*;

public class E {
    public static void main(String[] args) {
        FastScannerE fs = new FastScannerE();
        PrintWriter out = new PrintWriter(System.out);

        int n = fs.nextInt();
        int m = fs.nextInt();
        ArrayList<Edge>[] adj = new ArrayList[n];
        for(int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for(int i = 0; i < m; i++) {
            int u = fs.nextInt(), v = fs.nextInt(), it = fs.nextInt();
            boolean bad = it != 1;
            u--; v--;
            adj[u].add(new Edge(u, v, bad));
            adj[v].add(new Edge(v, u, bad));
        }
        for(ArrayList<Edge> set : adj) {
            Collections.sort(set);
        }

        int[] maxBad = new int[n];
        int[] parent = new int[n];
        int[] shortest = new int[n];
        int[] fix = new int[n];
        boolean[] V = new boolean[n];
        boolean[] ignore = new boolean[n];
        Arrays.fill(maxBad, (int)2e9);
        Arrays.fill(shortest, (int)2e9);

        ArrayDeque<Integer> bfs = new ArrayDeque<>();
        bfs.addLast(0);
        shortest[0] = 0;
        maxBad[0] = 0;
        V[0] = true;
        while(!bfs.isEmpty()) {
            int now = bfs.pollFirst();
            for(Edge e : adj[now]) {
                int add = e.bad ? 1 : 0;
                if(maxBad[now] + add < maxBad[e.v] && shortest[now] + 1 <= shortest[e.v]) {
                    parent[e.v] = now;
                    maxBad[e.v] = maxBad[now] + add;
                    fix[e.v] = add;
                }
                if(!V[e.v]) {
                    V[e.v] = true;
                    bfs.addLast(e.v);
                    parent[e.v] = now;
                    maxBad[e.v] = maxBad[now] + add;
                    fix[e.v] = add;
                    shortest[e.v] = shortest[now] + 1;
                }
            }
        }

        //System.out.println(Arrays.toString(shortest));
        //System.out.println(Arrays.toString(maxBad));
        //System.out.println(Arrays.toString(parent));

        ArrayList<String> res = new ArrayList<>();
        int at = n-1;
        ignore[n-1] = true;
        while(at != 0) {
            if(fix[at] > 0) {
                res.add((at+1) + " " + (parent[at]+1) + " " + 1);
            }
            ignore[parent[at]] = true;
            at = parent[at];
        }

        for(ArrayList<Edge> list : adj) {
            for(Edge e : list) {
                if(e.bad) continue;
                if(ignore[e.v] && ignore[e.u]) continue;
                if(e.u > e.v) continue;
                res.add((e.v+1) + " " + (e.u+1) + " " + 0);
            }
        }

        out.println(res.size());
        for(String s : res) out.println(s);
        out.close();
    }
}

class Edge implements Comparable<Edge> {
    int u, v;
    boolean bad;

    public Edge(int a, int b, boolean bad) {
        u = a; v = b;
        this.bad = bad;
    }

    public int compareTo(Edge e) {
        if(e.bad && bad) return 0;
        else if(e.bad) return -1;
        else if(bad) return 1;
        if(u == e.u) return v - e.v;
        return u - e.u;
    }

    public String toString() {
        return u + " " + v + " " + bad;
    }
}


class FastScannerE {
    BufferedReader br;
    StringTokenizer st;

    public FastScannerE() {
        try {
            br = new BufferedReader(new InputStreamReader(System.in));
            st = new StringTokenizer("");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public String next() {
        if (st.hasMoreTokens()) return st.nextToken();
        try {
            st = new StringTokenizer(br.readLine());
        } catch (Exception e) {
            e.printStackTrace();
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    public String nextLine() {
        String line = "";
        try {
            line = br.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return line;
    }

    public Integer[] nextIntegerArray(int n) {
        Integer[] a = new Integer[n];
        for (int i = 0; i < n; i++) a[i] = nextInt();
        return a;
    }

    public int[] nextIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = nextInt();
        return a;
    }

    public char[] nextCharArray() {
        return nextLine().toCharArray();
    }
}
