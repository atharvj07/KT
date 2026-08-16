import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class C1320E {
    public static void main(String[] args) {
        var scanner = new BufferedScanner();
        var writer = new PrintWriter(new BufferedOutputStream(System.out));

        var n = scanner.nextInt();
        // edges
        var edges = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < n - 1; i++) {
            var x = scanner.nextInt();
            var y = scanner.nextInt();
            edges.putIfAbsent(x, new ArrayList<>());
            edges.get(x).add(y);
            edges.putIfAbsent(y, new ArrayList<>());
            edges.get(y).add(x);
        }
        var order = new int[n + 1]; // 原编号->新编号
        var orig = new int[n + 1]; // 新编号->原编号
        var depth = new int[n + 1]; // 下标是原编号
        var jump = new int[n + 1][(int) (Math.log(n + 1) / Math.log(2)) + 2]; // 第1维下标是原编号
        prepare(n, edges, order, orig, depth, jump);

        var q = scanner.nextInt();
        var virusInit = new int[n + 1];
        var spread = new int[n + 1];
        for (int i = 0; i < q; i++) {
            var k = scanner.nextInt();
            var m = scanner.nextInt();
            // virus
            var cs = new HashSet<Integer>();
            var infected = new HashMap<Integer, Integer>();
            for (int j = 1; j <= k; j++) {
                // start city
                var v = scanner.nextInt(); // all different
                // spreading speed
                var s = scanner.nextInt();
                virusInit[j] = v;
                spread[j] = s;
                infected.put(v, j);
                cs.add(v);
            }
            // important cities
            var important = new ArrayList<Integer>();
            for (int j = 0; j < m; j++) {
                int u = scanner.nextInt();
                important.add(u);
            }
            cs.addAll(important);
            var cities = new ArrayList<>(cs);
            cities.sort(Comparator.comparingInt(o -> order[o]));

            hardcore(depth, jump, virusInit, cities, spread, infected);

            for (int j = 0; j < m; j++) {
                writer.print(infected.get(important.get(j)) + " ");
            }
            writer.println();
        }

        scanner.close();
        writer.flush();
        writer.close();
    }

    private static void hardcore(int[] depth, int[][] jump, int[] virusInit, List<Integer> cities, int[] spread,
            Map<Integer, Integer> infected) {
        if (cities.size() == 1) {
            return;
        }
        // 从下到上来一遍
        var lcaFrom = new HashMap<Integer, Set<Integer>>();
        var stack = new LinkedList<int[]>();
        stack.push(new int[]{cities.get(0), cities.get(1), lca(cities.get(0), cities.get(1), depth, jump)});
        for (int i = 2; i < cities.size(); i++) {
            var lca = lca(cities.get(i - 1), cities.get(i), depth, jump);
            var c = cities.get(i - 1);
            // 确保栈中lca深度是递增的
            while (stack.size() > 0 && depth[lca] <= depth[stack.peek()[2]]) {
                var top = stack.pop();
                infectUp(top[0], c, top[2], depth, virusInit, spread, infected);
//                infect(top[0], c, top[2], depth, jump, virusInit, spread, infected);
                lcaFrom.putIfAbsent(top[2], new HashSet<>());
                lcaFrom.get(top[2]).add(top[0]);
                lcaFrom.get(top[2]).add(c);
                c = top[2];
            }
            stack.push(new int[]{c, cities.get(i), lca});
        }
        if (stack.size() > 0) {
            var c = stack.peek()[1];
            while (stack.size() > 0) {
                var top = stack.pop();
                infectUp(top[0], c, top[2], depth, virusInit, spread, infected);
//                infect(top[0], c, top[2], depth, jump, virusInit, spread, infected);
                lcaFrom.putIfAbsent(top[2], new HashSet<>());
                lcaFrom.get(top[2]).add(top[0]);
                lcaFrom.get(top[2]).add(c);
                c = top[2];
            }
        }
        // 从上到下来一遍
        var lcaList = new ArrayList<>(lcaFrom.keySet());
        lcaList.sort(Comparator.comparingInt(o -> depth[o]));
        for (var lca : lcaList) {
            for (var child : lcaFrom.get(lca)) {
                if (lca.equals(child)) {
                    continue;
                }
                infect(lca, child, child, depth, jump, virusInit, spread, infected);
            }
        }
    }

    static int infinite = Integer.MAX_VALUE;

    private static void infect(int a, int b, int target, int[] depth, int[][] jump, int[] virusInit, int[] spread,
            Map<Integer, Integer> infected) {
        var va = infected.getOrDefault(a, 0);
        var vb = infected.getOrDefault(b, 0);
        var turnsA = turns(dist(virusInit[va], target, depth, jump), spread[va]);
        var turnsB = turns(dist(virusInit[vb], target, depth, jump), spread[vb]);
        if (turnsA == infinite && turnsB == infinite) {
            // 什么都不做
        } else if (better(turnsA, va, turnsB, vb)) {
            infected.put(target, va);
        } else {
            infected.put(target, vb);
        }
    }

    private static boolean better(int turnsA, int va, int turnsB, int vb) {
        return turnsA < turnsB || turnsA == turnsB && va < vb;
    }

    private static int dist(int a, int b, int[] depth, int[][] jump) {
        var lca = lca(a, b, depth, jump);
        return depth[a] - depth[lca] + depth[b] - depth[lca];
    }

    private static void infectUp(int a, int b, int lca, int[] depth, int[] virusInit, int[] spread,
            Map<Integer, Integer> infected) {
        var va = infected.getOrDefault(a, 0);
        var vb = infected.getOrDefault(b, 0);
        // 在沿着树向根走的过程中，initA和initB分别是a和b的孩子，所以也都是lca的孩子。
        var turnsA = turns(depth[virusInit[va]] - depth[lca], spread[va]);
        var turnsB = turns(depth[virusInit[vb]] - depth[lca], spread[vb]);
        if (turnsA == infinite && turnsB == infinite) {
            // 什么都不做
        } else if (better(turnsA, va, turnsB, vb)) {
            infected.put(lca, va);
        } else {
            infected.put(lca, vb);
        }
    }

    private static int turns(int dist, int speed) {
        return speed == 0 ? infinite : Math.floorDiv(dist - 1, speed) + 1;
    }

    private static int lca(int a, int b, int[] depth, int[][] jump) {
        if (depth[a] < depth[b]) {
            return lca(b, a, depth, jump);
        }
        // 先保持depth一致
        {
            var i = jump[a].length - 1;
            while (depth[a] > depth[b]) {
                while (jump[a][i] == 0 || depth[jump[a][i]] < depth[b]) {
                    i--;
                }
                a = jump[a][i];
            }
        }
        // 再开始找lca
        {
            var i = jump[a].length - 1;
            while (a != b) {
                while (i > 0 && jump[a][i] == jump[b][i]) {
                    i--;
                }
                a = jump[a][i];
                b = jump[b][i];
            }
        }
        return a;
    }

    /**
     * 做4件事：
     * <p>
     * 1）确定节点1为根。
     * <p>
     * 2）重新给节点排序，使得同一颗子树的节点彼此紧挨着，可以用一个区间表示；任何子树的根一定在子树其他节点的前面。
     * <p>
     * 3）计算每个节点的深度。
     * <p>
     * 4）计算每个节点往根节点方向的跳跃表。
     */
    private static void prepare(int n, Map<Integer, List<Integer>> edges, int[] order, int[] orig, int[] depth,
            int[][] jump) {
        var q = new LinkedList<Integer>();
        var parent = new int[n + 1];
        q.add(1);
        depth[1] = 0;
        parent[1] = 0;
        var o = 1;
        while (q.size() > 0) {
            var h = q.poll();
            order[h] = o++;
            orig[order[h]] = h;
            var children = edges.get(h);
            if (children == null) {
                continue;
            }
            for (var next : children) {
                if (order[next] == 0) {
                    q.addFirst(next);
                    depth[next] = depth[h] + 1;
                    parent[next] = h;
                    calcJump(next, parent, jump);
                }
            }
        }
    }

    private static void calcJump(int start, int[] parent, int[][] jump) {
        var i = 0;
        jump[start][i] = parent[start];
        var x = parent[start];
        while (x > 0) {
            i++;
            jump[start][i] = jump[x][i - 1];
            x = jump[x][i - 1];
        }
    }

    public static class BufferedScanner {
        BufferedReader br;
        StringTokenizer st;

        public BufferedScanner(Reader reader) {
            br = new BufferedReader(reader);
        }

        public BufferedScanner() {
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

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

        void close() {
            try {
                br.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    static long gcd(long a, long b) {
        if (a < b) {
            return gcd(b, a);
        }
        while (b > 0) {
            long tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

    static long inverse(long a, long m) {
        long[] ans = extgcd(a, m);
        return ans[0] == 1 ? (ans[1] + m) % m : -1;
    }

    private static long[] extgcd(long a, long m) {
        if (m == 0) {
            return new long[]{a, 1, 0};
        } else {
            long[] ans = extgcd(m, a % m);
            long tmp = ans[1];
            ans[1] = ans[2];
            ans[2] = tmp;
            ans[2] -= ans[1] * (a / m);
            return ans;
        }
    }

    private static List<Integer> primes(double upperBound) {
        var limit = (int) Math.sqrt(upperBound);
        var isComposite = new boolean[limit + 1];
        var primes = new ArrayList<Integer>();
        for (int i = 2; i <= limit; i++) {
            if (isComposite[i]) {
                continue;
            }
            primes.add(i);
            int j = i + i;
            while (j <= limit) {
                isComposite[j] = true;
                j += i;
            }
        }
        return primes;
    }


}
