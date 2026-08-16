import java.io.*;
import java.util.*;
import java.util.function.Function;

@SuppressWarnings("ALL")
public class Main {

    static int M, N;
    static int[][][] K;

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        M = sc.nextInt();
        N = sc.nextInt();

        K = new int[M][][];
        for (int i = 0; i < M; i++) {
            int k = sc.nextInt();
            K[i] = new int[k][3];
            for (int j = 0; j < k; j++) {
                int skill = sc.nextInt();
                String op = sc.next();
                int point = sc.nextInt();
                K[i][j][0] = skill;
                K[i][j][1] = ">=".equals(op) ? 0 : 1;
                K[i][j][2] = point;
            }
        }
        System.out.println(solve() ? "Yes": "No");
    }

    static boolean solve() {
        Command[] C = new Command[M];
        for (int i = 0; i < M; i++) {
            Command c = new Command();
            for (int[] input : K[i]) {
                int skill = input[0];
                String op = input[1] == 0 ? ">=" : "<=";
                int point = input[2];

                Range r;
                if( op.equals(">=") ) {
                    // 以上
                    r = new Range(point, 100);

                } else {
                    r = new Range(0, point);
                }
                boolean ok = c.add(skill, r);
                if( !ok ) return false;
            }
            C[i] = c;
        }

        // Aを取った状態ではBを取れない、というのものを A -> Bという辺にする
        // これが閉路を作ると矛盾
        List<Edge> E = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                if( i == j ) continue;

                Command c = C[i];
                Command d = C[j];

                if( !c.canReach(d) ) {
                    // debug(i, j);
                    E.add(new Edge(i, j));
                }
            }
        }

        int[][] G = adjD(M, E);
        return khan(M, G) != null;
    }

    static class Edge {
        int a, b;

        public Edge(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static int[][] adjD(int n, List<Edge> es) {
        int[][] adj = new int[n][];
        int[] cnt = new int[n];

        for (Edge e : es) {
            cnt[e.a]++;
        }
        for (int i = 0; i < n; i++) {
            adj[i] = new int[cnt[i]];
        }
        for (Edge e : es) {
            adj[e.a][--cnt[e.a]] = e.b;
        }
        return adj;
    }

    static int[] khan(int V, int[][] G) {
        int[] deg = new int[V];
        for (int[] tos : G) {
            for (int to : tos) {
                deg[to]++;
            }
        }

        int[] q = new int[V];
        int a = 0, b = 0;
        for (int v = 0; v < V; v++) {
            if( deg[v] == 0 ) q[b++] = v;
        }

        int[] ret = new int[V];
        int idx = 0;
        while( a != b ) {
            int v = q[a++];
            ret[idx++] = v;
            for (int to : G[v]) {
                deg[to]--;
                if( deg[to] == 0 ) {
                    q[b++] = to;
                }
            }
        }

        for (int v = 0; v < V; v++) {
            if( deg[v] != 0 ) return null;
        }
        return ret;
    }

    static class Command {
        Map<Integer, Range> contitions = new HashMap<>();

        boolean add(int skill, Range r) {
            if( contitions.containsKey(skill) ) {
                Range s = contitions.get(skill);
                Range t = Range.merge(r, s);
                if( t == null ) {
                    return false;
                } else {
                    contitions.put(skill, t);
                    return true;
                }


            } else {
                contitions.put(skill, r);
                return true;
            }
        }

        boolean canReach(Command c) {
            for (Integer skill : contitions.keySet()) {
                if( c.contitions.containsKey(skill) ) {
                    Range a = contitions.get(skill);
                    Range b = c.contitions.get(skill);

                    if( a.min > b.max ) return false;
                }
            }
            return true;
        }
    }

    // [min, max]
    static class Range {
        // [1, 5] [3, 7] -> [3, 5]
        public static Range merge(Range a, Range b) {
            int min = Math.max(a.min, b.min);
            int max = Math.min(a.max, b.max);
            if( min <= max ) {
                return new Range(min, max);
            } else {
                return null;
            }
        }

        int min, max;

        Range(int min, int max) {
            if( max < min ) throw new IllegalArgumentException("wtf " + min + " " + max);
            this.min = min;
            this.max = max;
        }
    }

    @SuppressWarnings("unused")
    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        FastScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }

        String next() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        String nextLine() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    return reader.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken("\n");
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        int[] nextIntArray(int n, int delta) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt() + delta;
            return a;
        }

        long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }
    }

    static <A> void writeLines(A[] as, Function<A, String> f) {
        PrintWriter pw = new PrintWriter(System.out);
        for (A a : as) {
            pw.println(f.apply(a));
        }
        pw.flush();
    }

    static void writeLines(int[] as) {
        PrintWriter pw = new PrintWriter(System.out);
        for (int a : as) pw.println(a);
        pw.flush();
    }

    static void writeLines(long[] as) {
        PrintWriter pw = new PrintWriter(System.out);
        for (long a : as) pw.println(a);
        pw.flush();
    }

    static int max(int... as) {
        int max = Integer.MIN_VALUE;
        for (int a : as) max = Math.max(a, max);
        return max;
    }

    static int min(int... as) {
        int min = Integer.MAX_VALUE;
        for (int a : as) min = Math.min(a, min);
        return min;
    }

    static void debug(Object... args) {
        StringJoiner j = new StringJoiner(" ");
        for (Object arg : args) {
            if (arg instanceof int[]) j.add(Arrays.toString((int[]) arg));
            else if (arg instanceof long[]) j.add(Arrays.toString((long[]) arg));
            else if (arg instanceof double[]) j.add(Arrays.toString((double[]) arg));
            else if (arg instanceof Object[]) j.add(Arrays.toString((Object[]) arg));
            else j.add(arg.toString());
        }
        System.err.println(j.toString());
    }
}

