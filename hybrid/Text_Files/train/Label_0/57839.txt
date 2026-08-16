import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Edge>[] graph;
    public static void main(String[] args) {
        FastScanner scanner = new FastScanner();
        PrintWriter out = new PrintWriter(System.out,false);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] weights= new int[n][2];
        int[] unsorted = new int[n];
        int[] rev = new int[n];
        for(int i = 0; i < n; i++) {
            weights[i][0] = scanner.nextInt();
            weights[i][1] = i;
            unsorted[i] = weights[i][0];
        }
        Arrays.sort(weights, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        for(int i = 0; i < n; i++) {
            rev[weights[i][1]] = i;
        }
        Edge[] edges = new Edge[m];
        graph = new ArrayList[n];
        for(int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for(int i = 0; i < m; i++) {
            int u = scanner.nextInt()-1;
            int v = scanner.nextInt()-1;
            edges[i] = new Edge(u,v,i);
            graph[u].add(edges[i]);
            graph[v].add(edges[i]);
        }
        Boolean[] cols = new Boolean[n];
        //for(Edge edge: graph[weights[0][1]]) {
        //    int o = edge.u == weights[0][1] ? edge.v: edge.u;
        //    //System.out.println(o + " " + weights[0][1]);
        //    if (unsorted[o] == weights[0][0]) {
        //        cols[weights[0][1]] = true;
        //        cols[o] = false;
        //        //System.out.println(0);
        //        edge.w = weights[0][0];
        //        break;
        //    }
        //}
        //if (cols[weights[0][1]] == null) {
        //    System.out.println(-1);
        //    return;
        //}
top:
        for(int i = 0; i < n; i++) {
            //System.out.println(Arrays.toString(cols));
            int cur = weights[i][1];
            if (cols[cur]!=null)continue;
            int ww = weights[i][0];
            //System.out.println("cur: " + cur + " ww: " + ww);
            for(Edge edge: graph[cur]) {
                int o = edge.u == cur ? edge.v: edge.u;
               // System.out.println(edge.u + " " + edge.v);
                if (cols[o] != null) {
                    //if (ww == unsorted[o]) {
                        cols[cur] = !cols[o];
                        edge.w = ww;
                   // }
                    //else {
                     //   cols[cur] = cols[o];
                      //  edge.w = ww - unsorted[o];
                   // }
                    continue top;
                } else if (unsorted[o] == ww) {
                    cols[cur] = true;
                    cols[o] = false;
                    edge.w = ww;
                    continue top;
                }
            }
            System.out.println(-1);
            return;
        }
        //System.out.println(Arrays.toString(cols));
        for(int i = 0; i < n; i++) {
            out.print(cols[i] ? 'B' : 'W'); 
        }
        out.println();
        for(int i = 0; i < m; i++) {
            //out.print((edges[i].u+1) + " " + (edges[i].v+1) + " " );
            out.println(edges[i].w);
        }
        out.flush();
    }
    static class Edge {
        int u,v,ind,w;
        public Edge(int uu, int vv, int ii) {
            u = uu; v = vv; ind = ii;
            w = 1_000_000_000;
        }
    }
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        public FastScanner(Reader in) {
            br = new BufferedReader(in);
        }
        public FastScanner() {
            this(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String readNextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
