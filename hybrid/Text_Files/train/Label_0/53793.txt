import java.io.*;
import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.*;

public class Main {
    void solve() {
        int n = in.nextInt();
        String a = in.nextLine();
        String b = in.nextLine();
        List<Boolean> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                list.add(a.charAt(i) == '1');
            }
        }
        int evenOdd = 0;
        for (Boolean el : list) {
            if (el) evenOdd++;
            else evenOdd--;
        }
        if (evenOdd != 0) {
            out.println(-1);
            return;
        }
        if (list.isEmpty()) {
            out.println(0);
            return;
        }
        List<Boolean> list2 = new ArrayList<>(list);
        list2.addAll(list);

        List<Integer> list3 = new ArrayList<>();
        list3.add(list2.get(0) ? 1 : -1);
        for (int i = 1; i < list2.size(); i++) {
            list3.add(list3.get(i - 1) + (list2.get(i) ? 1 : -1));
        }

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (Integer el : list3) {
            min = Math.min(min, el);
            max = Math.max(max, el);
        }
        out.println(max - min);
    }

    static final boolean MULTI_TEST = false;

    // --------------------------------------------------------------------------------------------------------------
    // --------------------------------------------------HELPER------------------------------------------------------
    // --------------------------------------------------------------------------------------------------------------


    void solve2() {
//        init();
        if (MULTI_TEST) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                solve();
            }
        } else {
            solve();
        }
    }

    // --------------------ALGORITHM-------------------------

    public void sort(int[] arr) {
        List<Integer> tmp = Arrays.stream(arr).boxed().sorted().collect(Collectors.toList());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = tmp.get(i);
        }
    }

    // --------------------SCANNER-------------------------
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner(boolean debug) {
            if (debug) {
                try {
                    br = new BufferedReader(new FileReader("input.txt"));
                } catch (FileNotFoundException e) {
                    throw new RuntimeException(e);
                }
            } else {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                st = new StringTokenizer(nextLine());
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] nextInts(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }
            return arr;
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        public long[] nextLongs(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLong();
            }
            return arr;
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            try {
                String line = br.readLine();
                if (line == null) {
                    throw new RuntimeException("empty line");
                }
                return line;
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

    }

    // --------------------WRITER-------------------------
    public static class MyWriter extends PrintWriter {

        public MyWriter(OutputStream out) {
            super(out);
        }

        void println(int[] arr) {
            String line = Arrays.stream(arr).mapToObj(String::valueOf).collect(joining(" "));
            println(line);
        }

    }
    // --------------------MAIN-------------------------

    public MyScanner in;
    public MyWriter out;

    public static void main(String[] args) {
        Main m = new Main();
        m.in = new MyScanner(args.length > 0);
        m.out = new MyWriter(new BufferedOutputStream(System.out));
        m.solve2();
        m.out.close();
    }
}
