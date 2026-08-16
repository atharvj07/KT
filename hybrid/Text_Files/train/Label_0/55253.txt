import java.io.*;
import java.text.DecimalFormat;
import java.util.*;

public class Main {

    public static final DecimalFormat DF_3 = new DecimalFormat("0.000");


    static int[] readArray(int size, InputReader in, boolean subOne) {
        int[] a = new int[size];
        for (int i = 0; i < size; i++) {
            a[i] = in.nextInt() + (subOne ? -1 : 0);
        }
        return a;
    }

    static long[] readLongArray(int size, InputReader in) {
        long[] a = new long[size];
        for (int i = 0; i < size; i++) {
            a[i] = in.nextLong();
        }
        return a;
    }

    static void sortArray(int[] a) {
        Random random = new Random();

        for (int i = 0; i < a.length; i++) {
            int randomPos = random.nextInt(a.length);
            int t = a[i];
            a[i] = a[randomPos];
            a[randomPos] = t;
        }
        Arrays.sort(a);
    }


    public static void main(String[] args) throws FileNotFoundException {
//        InputReader in = new InputReader(new FileInputStream("input.txt"));
//        PrintWriter out = new PrintWriter(new BufferedOutputStream(new FileOutputStream("milkvisits.out")));
//
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

//        long start = System.currentTimeMillis();

        int n = in.nextInt();
        long k = in.nextInt();
        long[] a = readLongArray(n, in);

        long s = 0;
        int j = 2;
        int cnt = n;
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            if (s - (long) (j - 1) * (cnt - j) * a[i] < k) {
                ans.add(i + 1);
                cnt--;
            } else {
                s += a[i] * (j - 1);
                j++;
            }
        }
        for (int i = 0; i < ans.size(); i++) {
            out.println(ans.get(i));
        }


        out.close();
    }


    private static void outputArray(int[] ans, PrintWriter out, boolean addOne) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < ans.length; i++) {
            long an = ans[i] + (addOne ? 1 : 0);
            str.append(an).append(' ');
        }
        out.println(str);
    }

    private static void outputArray(List<Integer> ans, PrintWriter out, boolean addOne) {
        StringBuilder str = new StringBuilder();
        for (int j = 0; j < ans.size(); j++) {
            long i = ans.get(j);
            long an = i + (addOne ? 1 : 0);
            str.append(an);
            if (j < ans.size() - 1) {
                str.append(' ');
            }
        }
        out.println(str);
//        out.flush();
    }

    private static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public String nextString() {
            try {
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public char nextChar() {
            return next().charAt(0);
        }

        public String nextWord() {
            return next();
        }

        private List<Integer>[] readTree(int n) {
            return readGraph(n, n - 1);
        }

        private List<Integer>[] readGraph(int n, int m) {
            List<Integer>[] result = new ArrayList[n];
            for (int i = 0; i < n; i++) {
                result[i] = new ArrayList<>();
            }
            for (int i = 0; i < m; i++) {
                int u = nextInt() - 1;
                int v = nextInt() - 1;
                result[u].add(v);
                result[v].add(u);
            }
            return result;
        }

    }
}