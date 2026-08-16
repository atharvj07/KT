import java.io.*;
import java.util.Arrays;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int Q = sc.nextInt();
        for (int i = 0; i < Q; i++) {
            String s = sc.next();
            pw.println( solve(s) );
        }
        pw.flush();
    }

    static String solve(String s) {
        Context context = new Context(s);
        Node node = parse(context);

        for (int i = 0; i < s.length(); i++) {
            int min = node.getMin(i);
            int max = node.getMax(i);
            if( min == max ) {
                return min + " " + (i+1);
            }
        }
        throw new IllegalArgumentException("wtf");
    }

    static Node parse(Context context) {
        if( context.peek() == '^' || context.peek() == '_' ) {
            char f = context.poll();
            context.poll(); // L
            Node l = parse(context);
            context.poll(); // comma
            Node r = parse(context);
            context.poll(); // R
            return new Func(f, l, r);

        } else {
            int from = context.index();
            context.poll(); // digit
            if( Character.isDigit(context.peek()) ) {
                int to = context.index();
                context.poll(); // digit
                return new Number(context.s, from, to);

            } else {
                return new Number(context.s, from, from);
            }
        }
    }

    interface Node {
        int getMin(int idx);
        int getMax(int idx);
    }

    static class Number implements Node {

        String s;
        int from, to; // [from, to]

        public Number(String s, int from, int to) {
            this.s = s;
            this.from = from;
            this.to = to;
        }

        public int getMin(int idx) {
            if( idx < from ) {
                return 0;

            } else if( idx == from ) {
                char c = s.charAt(from);
                if( c == '0' ) {
                    // 03とかそういうのがないので0が確定する
                    return 0;
                } else {
                    return (c - '0');
                }

            } else {
                // 確定
                char c = s.charAt(from);
                if( from != to ) {
                    char d = s.charAt(to);
                    return (c - '0') * 10 + (d - '0');
                } else {
                    return (c - '0');
                }
            }
        }

        public int getMax(int idx) {
            if( idx < from ) {
                return 99;

            } else if( idx == from ) {
                char c = s.charAt(from);
                if( c == '0' ) {
                    // 03とかそういうのがないので0が確定する
                    return 0;
                } else {
                    // 3?の可能性
                    return (c - '0') * 10 + 9;
                }

            } else {
                // 確定
                char c = s.charAt(from);
                if( from != to ) {
                    char d = s.charAt(to);
                    return (c - '0') * 10 + (d - '0');
                } else {
                    return (c - '0');
                }
            }
        }
    }

    static class Func implements Node {

        private char f;
        private Node l;
        private Node r;

        public Func(char f, Node l, Node r) {
            this.f = f;
            this.l = l;
            this.r = r;
        }

        public int getMin(int idx) {
            int lv = l.getMin(idx);
            int rv = r.getMin(idx);
            if( f == '^' ) {
                return Math.max(lv, rv);

            } else {
                return Math.min(lv, rv);
            }
        }

        public int getMax(int idx) {
            int lv = l.getMax(idx);
            int rv = r.getMax(idx);
            if( f == '^' ) {
                return Math.max(lv, rv);

            } else {
                return Math.min(lv, rv);
            }
        }
    }

    static class Context {

        private String s;
        private int i;

        public Context(String s) {
            this.s = s;
        }

        public char peek() {
            return s.charAt(i);
        }

        public int index() {
            return i;
        }

        public char poll() {
            return s.charAt(i++);
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
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        int[] nextIntArray(int n, int delta) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt() + delta;
            return a;
        }

        long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = nextLong();
            return a;
        }
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

    static void writeSingleLine(int[] as) {
        PrintWriter pw = new PrintWriter(System.out);
        for (int i = 0; i < as.length; i++) {
            if (i != 0) pw.print(" ");
            pw.print(as[i]);
        }
        pw.println();
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
            if (arg == null) j.add("null");
            else if (arg instanceof int[]) j.add(Arrays.toString((int[]) arg));
            else if (arg instanceof long[]) j.add(Arrays.toString((long[]) arg));
            else if (arg instanceof double[]) j.add(Arrays.toString((double[]) arg));
            else if (arg instanceof Object[]) j.add(Arrays.toString((Object[]) arg));
            else j.add(arg.toString());
        }
        System.err.println(j.toString());
    }

    static void printSingleLine(int[] array) {
        PrintWriter pw = new PrintWriter(System.out);
        for (int i = 0; i < array.length; i++) {
            if (i != 0) pw.print(" ");
            pw.print(array[i]);
        }
        pw.println();
        pw.flush();
    }

    static int lowerBound(int[] array, int value) {
        int lo = 0, hi = array.length, mid;
        while (lo < hi) {
            mid = (hi + lo) / 2;
            if (array[mid] < value) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static int upperBound(int[] array, int value) {
        int lo = 0, hi = array.length, mid;
        while (lo < hi) {
            mid = (hi + lo) / 2;
            if (array[mid] <= value) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
