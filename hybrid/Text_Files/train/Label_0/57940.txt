import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.Vector;

public class Solution {
    static class TreeNode {
        int l;
        int r;
        int m;
        int v;
        TreeNode le;
        TreeNode ri;

        public TreeNode(int lb, int rb) {
            l = lb;
            r = rb;
            m = (lb + rb) / 2;

            if (l == r) {
                v = 1;
                le = ri = null;
            } else {
                le = new TreeNode(lb, m);
                ri = new TreeNode(m + 1, rb);
                v = le.v + ri.v;
            }
        }

        public void set(int i, int val) {
            if (l == r)
                v = val;
            else {
                if (i <= m)
                    le.set(i, val);
                else
                    ri.set(i, val);

                v = le.v + ri.v;
            }
        }

        public int get(int lb, int rb) {
            if (l == lb && r == rb)
                return v;
            else if (rb <= m)
                return le.get(lb, rb);
            else if (lb > m)
                return ri.get(lb, rb);
            else
                return le.get(lb, m) + ri.get(m + 1, rb);
        }
    }

    static class PairV implements Comparable<PairV> {
        int a;
        int b;

        public PairV(int A, int B) {
            a = A;
            b = B;
        }

        @Override
        public int compareTo(PairV p) {
            return a != p.a ? a - p.a : b - p.b;
        }
    }

    static Vector<Vector<Integer>> G;
    static int[] colsE;
    static int[] indE;
    static int[] colsV;
    static int[] indV;
    static TreeMap<PairV, Integer> map;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(in.readLine());
        G = new Vector<Vector<Integer>>();

        for (int i = 0; i < n; i++)
            G.add(new Vector<Integer>());

        colsE = new int[n - 1];
        indE = new int[n - 1];
        colsV = new int[n];
        indV = new int[n];
        map = new TreeMap<Solution.PairV, Integer>();

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine());

            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;

            G.elementAt(from).add(to);
            G.elementAt(to).add(from);

            PairV p1 = new PairV(from, to);
            PairV p2 = new PairV(to, from);

            map.put(p1, i);
            map.put(p2, i);
        }

        int maxI = -1;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            if (G.elementAt(i).size() > max) {
                maxI = i;
                max = G.elementAt(i).size();
            }
        }

        Vector<TreeNode> roots = new Vector<Solution.TreeNode>();

        Vector<Integer> adj = G.elementAt(maxI);
        for (int i = 0; i < adj.size(); i++) {
            int to = adj.elementAt(i);
            int size = dfs(to, maxI, i, 1);

            TreeNode root = new TreeNode(0, size);
            roots.add(root);
        }

        int m = Integer.parseInt(in.readLine());

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int t = Integer.parseInt(st.nextToken());

            switch (t) {
            case 1:
            case 2: {
                int edgeI = Integer.parseInt(st.nextToken()) - 1;
                int col = colsE[edgeI];
                int ind = indE[edgeI];
                TreeNode root = roots.elementAt(col);
                root.set(ind, t == 1 ? 1 : 0);
                break;
            }
            case 3: {
                int a = Integer.parseInt(st.nextToken()) - 1;
                int b = Integer.parseInt(st.nextToken()) - 1;

                if (a == b)
                    out.println(0);
                else {
                    if (a == maxI || b == maxI) {
                        if (b == maxI) {
                            int tmp = b;
                            b = a;
                            a = tmp;
                        }

                        int cnt = getCntToRoot(roots, b);
                        out.println(cnt);
                    } else {
                        int colA = colsV[a];
                        int colB = colsV[b];

                        if (colA == colB) {
                            if (indV[a] > indV[b]) {
                                int tmp = a;
                                a = b;
                                b = tmp;
                            }

                            TreeNode root = roots.elementAt(colA);
                            int cnt = root.get(indV[a], indV[b] - 1);
                            if (cnt != indV[b] - indV[a])
                                out.println(-1);
                            else
                                out.println(cnt);
                        } else {
                            int cntA = getCntToRoot(roots, a);
                            int cntB = getCntToRoot(roots, b);

                            if (cntA == -1 || cntB == -1)
                                out.println(-1);
                            else
                                out.println(cntA + cntB);
                        }
                    }
                }
            }
            }
        }

        out.close();
    }

    private static int getCntToRoot(Vector<TreeNode> roots, int b) {
        int colB = colsV[b];
        TreeNode root = roots.elementAt(colB);
        int cnt = root.get(0, indV[b] - 1);
        if (cnt != indV[b])
            return -1;
        else
            return cnt;
    }

    private static int dfs(int v, int from, int col, int d) {
        colsV[v] = col;
        indV[v] = d;

        int edgeI = map.get(new PairV(from, v));

        colsE[edgeI] = col;
        indE[edgeI] = d - 1;

        int ret = 1;

        Vector<Integer> adj = G.elementAt(v);

        for (int i = 0; i < adj.size(); i++) {
            int to = adj.elementAt(i);

            if (to == from)
                continue;

            ret += dfs(to, v, col, d + 1);
        }

        return ret;
    }
}