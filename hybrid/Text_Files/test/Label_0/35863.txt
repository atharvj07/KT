import java.io.*;
import java.util.*;
import java.util.function.IntConsumer;
import java.util.stream.Stream;

public class Solution {


    static MyScanner sc;
    private static PrintWriter out;
    static long M2 = 1_000_000_000L + 7;

    private static HashMap<Long, Long>[] mods;

    public static void main(String[] s) throws Exception {
        StringBuilder stringBuilder = new StringBuilder();
//        stringBuilder.append(" 10 1 1 ");
//        stringBuilder.append("7 3\n" +
//                "1 5 2 6 3 7 4\n" +
//                "2 5 3\n" +
//                "4 4 1\n" +
//                "1 7 3");

//
//        Random r = new Random(5);
//        stringBuilder.append("100000 5000 ");
//        for (int i = 0; i < 100000; i++) {
//            stringBuilder.append(" " + (r.nextInt(2000000000) - 1000000000) + " ");
//
//        }
//        for (int k = 0; k < 5000; k++) {
//            stringBuilder.append(" 1 100000 777 ");
//        }

        if (stringBuilder.length() == 0) {
            sc = new MyScanner(System.in);
        } else {
            sc = new MyScanner(new BufferedReader(new StringReader(stringBuilder.toString())));
        }

        out = new PrintWriter(new OutputStreamWriter(System.out));

        initData();
        solve();
        out.flush();
    }


    private static void initData() {


    }

    private static void solve() throws IOException {
        int s1 = sc.nextInt();
        int s2 = sc.nextInt();
        int s3 = sc.nextInt();
        int s4 = sc.nextInt();

        int l1 = s1 * 2;
        int l2 = s2 * 2;
        int l3 = Math.min(s3 * 2, s4 * 2);
        if (s4 * 2 >= l2 || s4 > l3 || s3 > l3) {
            out.println(-1);
            return;
        }
        out.println(l1);
        out.println(l2);
        out.println(l3);

    }

    private static final class AList {
        int[] data;
        int c = 0;

        public AList(int n) {
            this.data = new int[Math.max(Integer.highestOneBit(n - 1) << 1, 4)];
        }

        public AList() {
            this(4);
        }

        public AList(int[] data) {
            this(data.length);
            System.arraycopy(data, 0, this.data, 0, data.length);
        }

        public void sort() {
            if (c < 2) return;
            Arrays.sort(data, 0, c);
        }

        public void work(IntConsumer intConsumer) {
            for (int i = 0; i < c; i++) {
                intConsumer.accept(data[i]);
            }
        }

        public void add(int k) {
            if (c == data.length) {
                data = Arrays.copyOf(data, data.length << 1);
            }
            data[c++] = k;
        }


    }

    private static final class SparseMatrix {
        AList[] init;

        public SparseMatrix(int n) {
            init = new AList[n + 1];
            for (int i = 1; i <= n; i++) {
                init[i] = new AList();
            }
        }

        void sort() {
            for (AList l : init) {
                if (l != null)
                    l.sort();
            }
        }

        public void add(int row, int column) {
            while (row < init.length) {
                init[row].add(column);
                row += row & (-row);
            }
        }


        private long sum(int x, int y) {
            if (x >= init.length) x = init.length - 1;
            long sum = 0;
            while (x > 0) {
                sum += r(x, y);
                x -= x & (-x);
            }
            return sum;
        }

        private long r(int x, int y) {
            return biSearch(init[x].data, 0, init[x].c, y);
        }
    }

    static int biSearch(int[] k, int from, int to, int val) {
        int r = Arrays.binarySearch(k, from, to, val + 1);
        if (r < 0) r = -r - 1;
        return r;
    }


    private static boolean isset(long i, int k) {
        return (i & (1 << k)) > 0;
    }

    private static void solveT() throws IOException {
        int t = sc.nextInt();
        while (t-- > 0) {
            solve();
        }
    }


    private static long gcd(long l, long l1) {
        if (l > l1) return gcd(l1, l);
        if (l == 0) return l1;
        return gcd(l1 % l, l);
    }

    private static long pow(long a, long b, long m) {
        if (b == 0) return 1;
        if (b == 1) return a;
        long pp = pow(a, b / 2, m);
        pp *= pp;
        pp %= m;
        return (pp * (b % 2 == 0 ? 1 : a)) % m;
    }


    static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        MyScanner(BufferedReader br) {
            this.br = br;
        }

        public MyScanner(InputStream in) {
            this(new BufferedReader(new InputStreamReader(in)));
        }

        void findToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        String next() {
            findToken();
            return st.nextToken();
        }

        Integer[] nab(int n) {
            Integer[] k = new Integer[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.fi();
            }
            return k;
        }

        int[] na(int n) {
            int[] k = new int[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.fi();
            }
            return k;
        }

        long[] nl(int n) {
            long[] k = new long[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.nextLong();
            }
            return k;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int fi() {
            String t = next();
            int cur = 0;
            boolean n = t.charAt(0) == '-';
            for (int a = n ? 1 : 0; a < t.length(); a++) {
                cur = cur * 10 + t.charAt(a) - '0';
            }
            return n ? -cur : cur;
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }


}