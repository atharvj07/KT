import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        in = new BufferedReader(new InputStreamReader(System.in, "ISO-8859-1"));
        out = new PrintWriter(System.out);

        solve();

        in.close();
        out.close();
    }

    private static void solve() throws Exception {
        int N = nextInt();
        ArrayList<Integer>[] gr = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            gr[i] = new ArrayList<Integer>();
        }
        int[] cnt = new int[N];
        for (int i = 0; i < N - 1; i++) {
            int a = nextInt() - 1, b = nextInt() - 1;
            gr[a].add(b);
            gr[b].add(a);
            cnt[a]++;
            cnt[b]++;
        }
        int leafCount = 0;
        for (int i = 1; i < N; i++) {
            if (cnt[i] == 1)
                leafCount++;
        }
        int[] order = new int[leafCount];
        for (int i = 0; i < leafCount; i++) {
            order[i] = nextInt() - 1;
        }
        HashSet<Integer>[] leafs = new HashSet[N];
        dfs(0, gr, leafs);
        ArrayList<Integer> way = new ArrayList<Integer>();
        dfs2(0, -1, gr, leafs, order, 0, leafCount - 1, way);
        if (way.size() == 2 * N - 1) {
            for (int v : way) {
                out.print(v);
                out.print(' ');
            }
            out.println();
        } else {
            out.println("-1");
        }
    }


    private static void dfs2(int i, int prev, ArrayList<Integer>[] gr,
            HashSet<Integer>[] leafs, int[] order, int from, int to, ArrayList<Integer> way) {
        way.add(i + 1);
        HashSet<Integer> set = new HashSet<Integer>();
        for (int k = from; k <= to; k++) {
            set.add(order[k]);
            for (int j : gr[i]) {
                if (j != prev) {
                    if (leafs[j].equals(set)) {
                        dfs2(j, i, gr, leafs, order, from, k, way);
                        way.add(i + 1);
                        set.clear();
                        from = k + 1;
                    }
                }
            }
        }
    }

    private static void dfs(int i, ArrayList<Integer>[] gr,
            HashSet<Integer>[] leafs) {
        leafs[i] = new HashSet<Integer>();
        boolean was = false;
        int parent = -1;
        for (int j : gr[i]) {
            if (leafs[j] == null) {
                was = true;
                dfs(j, gr, leafs);
            } else {
                parent = j;
            }
        }
        if (!was) {
            leafs[i].add(i);
        } else {
            for (int j : gr[i]) {
                if (j != parent) {
                    leafs[i].addAll(leafs[j]);
                }
            }
        }
        
    }


    private static BufferedReader in;
    private static PrintWriter out;
    private static StringTokenizer st;

    static String nextString() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(nextString());
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble(nextString());
    }
}
