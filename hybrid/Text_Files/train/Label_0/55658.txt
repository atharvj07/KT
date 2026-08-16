
import java.io.*;
import java.util.*;

public class Main {
    private static final boolean N_CASE = false;

    private static class MultiSet<T extends Comparable<T>> {
        private final TreeMap <T, Integer> map;

        public MultiSet() {
            map = new TreeMap<>();
        }

        public void add(T x) {
            map.put(x, map.getOrDefault(x, 0) + 1);
        }

        public void remove(T x) {
            map.put(x, map.getOrDefault(x, 0) - 1);
            if (map.get(x) <= 0) {
                map.remove(x);
            }
        }

        public T min() {
            return map.firstKey();
        }

        public T max() {
            return map.lastKey();
        }

        public boolean isEmpty() {
            return map.isEmpty();
        }
    }

    private static class Range {
        int st, ed, v;

        public Range(int st, int ed, int v) {
            this.st = st;
            this.ed = ed;
            this.v = v;
        }
    }

    private void solve() {
        int H = sc.nextInt();
        int W = sc.nextInt();

        MultiSet<Integer> s = new MultiSet<>();
        TreeMap<Integer, Range> m = new TreeMap<>();
        for (int i = 1; i <= W; ++i) {
            m.put(i, new Range(i, i, 0));
            s.add(0);
        }

        for (int i = 0; i < H; ++i) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            int st = A, ed = B;
            Integer left = m.lowerKey(A);
            if (left == null) left = 0;
            SortedMap<Integer, Range> sub = m.subMap(left, B + 1);
            List<Integer> rm = new ArrayList<>();
            for (Map.Entry<Integer, Range> e : sub.entrySet()) {
                Range range = e.getValue();
                st = Math.min(st, range.st);
                ed = Math.max(ed, range.ed);
                rm.add(e.getKey());
            }

            Range merged = null;
            if (st < A) {
                int v = sub.get(sub.firstKey()).v;
                merged = new Range(st, B, v);
            }

            Range tail = null;
            if (ed > B) {
                Range last = sub.get(sub.lastKey());
                tail = new Range(B + 1, ed, last.v + B + 1 - last.st);
            }

            for (int x : rm) {
                s.remove(m.get(x).v);
                m.remove(x);
            }

            if (merged != null) {
                m.put(merged.st, merged);
                s.add(merged.v);
            }

            if (tail != null) {
                m.put(tail.st, tail);
                s.add(tail.v);
            }

            if (s.isEmpty()) {
                out.println(-1);
            } else {
                out.println(s.min() + i + 1);
            }
        }
    }

    private void run() {
        int T = N_CASE ? sc.nextInt() : 1;
        for (int t = 0; t < T; ++t) {
            solve();
        }
    }

    private static MyWriter out;
    private static MyScanner sc;

    private static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        private MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
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

        int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextInt();
            }
            return a;
        }

        int[][] nextIntArray(int n, int m) {
            int[][] a = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    a[i][j] = sc.nextInt();
                }
            }
            return a;
        }

        long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextLong();
            }
            return a;
        }

        long[][] nextLongArray(int n, int m) {
            long[][] a = new long[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    a[i][j] = nextLong();
                }
            }
            return a;
        }

        List<Integer> nextList(int n) {
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(nextInt());
            }
            return list;
        }

        List<Long> nextLongList(int n) {
            List<Long> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(nextLong());
            }
            return list;
        }

        char[] nextCharArray(int n) {
            return sc.next().toCharArray();
        }

        char[][] nextCharArray(int n, int m) {
            char[][] c = new char[n][m];
            for (int i = 0; i < n; i++) {
                String s = sc.next();
                for (int j = 0; j < m; j++) {
                    c[i][j] = s.charAt(j);
                }
            }
            return c;
        }
    }

    private static class MyWriter extends PrintWriter {
        private MyWriter(OutputStream outputStream) {
            super(outputStream);
        }

        void printArray(int[] a) {
            for (int i = 0; i < a.length; ++i) {
                print(a[i]);
                print(i == a.length - 1 ? '\n' : ' ');
            }
        }

        void printArray(long[] a) {
            for (int i = 0; i < a.length; ++i) {
                print(a[i]);
                print(i == a.length - 1 ? '\n' : ' ');
            }
        }

        void println(int[] a) {
            for (int v : a) {
                println(v);
            }
        }

        void print(List<Integer> list) {
            for (int i = 0; i < list.size(); ++i) {
                print(list.get(i));
                print(i == list.size() - 1 ? '\n' : ' ');
            }
        }

        void println(List<Integer> list) {
            list.forEach(this::println);
        }
    }

    private <T> List<List<T>> createGraph(int n) {
        List<List<T>> g = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            g.add(new ArrayList<>());
        }
        return g;
    }

    private void fill(int[][] a, int value) {
        for (int[] row : a) {
            fill(row, value);
        }
    }

    private void fill(int[] a, int value) {
        Arrays.fill(a, value);
    }

    public static void main(String[] args) {
        out = new MyWriter(new BufferedOutputStream(System.out));
        sc = new MyScanner();
        new Main().run();
        out.close();
    }
}