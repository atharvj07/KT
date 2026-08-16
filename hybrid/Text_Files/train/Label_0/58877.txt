import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int M;
    static Edge[] E;

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        E = new Edge[M];
        for (int i = 0; i < M; i++) {
            E[i] = new Edge(sc.nextInt()-1, sc.nextInt()-1, sc.nextInt());
        }

        System.out.println( solve() );
    }

    static long solve() {
        List<Edge>[] rin = new List[N];
        for (int i = 0; i < N; i++) {
            rin[i] = new ArrayList<>();
        }
        for (Edge e : E) {
            rin[e.a].add(e);
            rin[e.b].add(e);
        }

        Node[] nodes = new Node[N];

        ArrayDeque<State> q = new ArrayDeque<>();
        q.add( new State(0) );
        nodes[0] = new Node(true, 0);

        long fixed = -1;
        while(!q.isEmpty()) {
            State state = q.poll();
            Node node = nodes[state.a];

            for (Edge e : rin[state.a]) {
                int to = state.a == e.a ? e.b : e.a;
                Node other = node.other(e.s);
                Node other_old = nodes[to];

                if( other_old == null ) {
                    nodes[to] = other;
                    q.add(new State(to));
                    continue;
                }

                if( other_old.equals(other) ) {
                    continue;
                }

                if( node.sign == other_old.sign ) {
                    long fixed_now = calcFixed(node, other_old, e);

                    if( fixed_now == -1 ) return 0;

                    if( fixed == -1 ) {
                        fixed = fixed_now;
                        continue;
                    }

                    if( fixed != fixed_now ) {
                        return 0;
                    } else {
                        continue;
                    }

                } else {
                    return 0;
                }
            }
        }

        // System.out.println("fixed=" + fixed);
        // System.out.println(Arrays.toString(nodes));

        if( fixed != -1 ) {
            for (Node node : nodes) {
                if( !node.isOk(fixed) ) {
                    return 0;
                }
            }
            return 1;

        } else {
            long min = 1;
            long max = Long.MAX_VALUE;
            for (Node node : nodes) {

                if( node.sign ) {
                    // x + a > 0
                    // => a > -x

                    min = Math.max(-1 * node.x+1, min);

                } else {
                    // x - a > 0
                    // => a < x
                    max = Math.min(node.x-1, max);
                }
            }

            // System.out.println("min=" + min + " max=" + max);

            return Math.max(0L, max-min+1);
        }
    }

    static long calcFixed(Node n1, Node n2, Edge e) {
        if( n1.sign ) {
            // s = (x1 + a) + (x2 + a)
            // => s - x1 - x2 = 2 * a

            long a2 = e.s - n1.x - n2.x;

            if( a2 <= 0 ) return -1;

            if( a2 % 2 == 0 ) {
                return a2 / 2;
            } else {
                return -1;
            }

        } else {
            // s = (x1 - a) + (y2 - a)
            // 2*a = x1 + y1 - s
            long a2 = n1.x + n2.x - e.s;

            if( a2 <= 0 ) return -1;

            if( a2 % 2 == 0 ) {
                return a2 / 2;
            } else {
                return -1;
            }
        }


    }

    static class State {
        int a;

        public State(int a) {
            this.a = a;
        }
    }

    static class Edge {
        int a;
        int b;
        int s;

        public Edge(int a, int b, int s) {
            this.a = a;
            this.b = b;
            this.s = s;
        }
    }

    static class Node {

        final boolean sign;
        final long x;

        public Node(boolean sign, long x) {
            this.sign = sign;
            this.x = x;
        }

        boolean isOk(long a) {
            if( !sign ) a *= -1;
            return x + a > 0;
        }

        Node other(int s) {
            // s - (x + sign*a)
            return new Node(!sign, s - x);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return sign == node.sign &&
                    x == node.x;
        }

        @Override
        public int hashCode() {
            return Objects.hash(sign, x);
        }

        public String toString() {
            char sign_c = sign ? '+' : '-';
            return "(" + x + " " + sign_c + ")";
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

        double nextDouble() {
            return Double.parseDouble(next());
        }

        int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }
    }
}

