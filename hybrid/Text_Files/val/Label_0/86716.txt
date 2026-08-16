import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

import static java.lang.Math.min;

public class Solution {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static PrintWriter pw;

    private static String nextToken() {
        try {
            while (st == null || !st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return st.nextToken();
    }

    private static int nextInt() {
        return Integer.parseInt(nextToken());
    }

    static long nextLong() {
        return Long.parseLong(nextToken());
    }

    static double nextDouble() {
        return Double.parseDouble(nextToken());
    }

    static char nextChar() throws IOException {
        return (char) br.read();
    }

    static String next() throws IOException {
        return nextToken();
    }

    static String nextLine() throws IOException {
        return br.readLine();
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        pw = new PrintWriter(System.out);
        run();
        pw.close();
    }

    static int V, E, N, K;

    private static void run() {
        V = nextInt();
        E = nextInt();
        N = nextInt();
        K = nextInt();

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = nextInt() - 1;
        }

        long[][] nD = new long[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (i != j)
                    nD[i][j] = Long.MAX_VALUE / 2 - 1;
            }
        }
        for (int i = 0; i < E; i++) {
            int a = nextInt() - 1;
            int b = nextInt() - 1;
            int t = nextInt();
            nD[a][b] = min (nD[a][b], t);
            nD[b][a] = min (nD[b][a], t);
        }


        for (int k = 0; k < V; ++k)
            for (int i = 0; i < V; ++i)
                for (int j = 0; j < V; ++j)
                    nD[i][j] = min(nD[i][j], nD[i][k] + nD[k][j]);

        int l = -1, r = 1731312;

        while (r - l > 1) {
            int m = l + ((r - l) >> 1);
            if (check(m, nD, arr, K)) r = m;
            else
                l = m;
        }
        if (r < 1731312) {
            pw.println(r);
        } else {
            pw.println(-1);
        }
    }

    static boolean[] used;
    static int[] mt;

    static boolean check(int time, long[][] d, int[] arr, int K) {

        int res = 0;

        mt = new int[d.length];

        used = new boolean[arr.length];

        ArrayList<Integer>[] g = new ArrayList[arr.length];

        for (int i = 0; i < arr.length; i++) {
            g[i] = new ArrayList<>();

            for (int j = 0; j < d.length; j++) {
                if (d[arr[i]][j] <= time)
                    g[i].add(j);
            }
        }

        Arrays.fill(mt, -1);

        parsoch(g);

        for (int value : mt) {
            if (value != -1)
                res++;
        }
        return res >= K;
    }

    private static boolean inc(int v, ArrayList<Integer>[] g) {
        if (used[v]) return false;
        used[v] = true;
        for (int i = 0; i < g[v].size(); i++) {
            int to = g[v].get(i);
            if (mt[to] == -1) {
                mt[to] = v;
                return true;
            }
        }
        for (int i = 0; i < g[v].size(); i++) {
            int to = g[v].get(i);
            if (inc(mt[to], g)) {
                mt[to] = v;
                return true;
            }
        }
        return false;
    }

    private static void parsoch(ArrayList<Integer>[] g) {
//        boolean[] matched = new boolean[N];
//
//        Arrays.fill(matched, false);

//        while (true) {
//            boolean tr = false;
        for (int i = 0; i < g.length; i++) {
            Arrays.fill(used, false);
            inc(i, g);
            //              if (!matched[i] && inc(i, g)) {
            //              tr = true;
            //                matched[i] = true;
        }
        //}
        //    if (!tr) break;
        //}
    }
}
/*

 */