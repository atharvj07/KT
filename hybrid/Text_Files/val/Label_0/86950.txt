
import java.io.*;
import java.lang.*;
import java.util.*;

public class Solver {
    public static void main(String[] args) {
        FastReader in = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        TaskC solver = new TaskC(in, out);
        solver.solve();
        out.close();
    }

    static class TaskC {
        FastReader in;
        PrintWriter out;

        public TaskC(FastReader in, PrintWriter out) {
            this.in = in;
            this.out = out;
        }

        public void solve() {
            solveA();
        }

        public void solveA() {
            int n = in.nextInt();
            int[] inputColors = in.nextIntArray(n);

            int colors = 0;

            Arrays.sort(inputColors);

            for (int i = 0; i < inputColors.length; i++) {
                if (inputColors[i] == -1) {
                    continue;
                }

                int colorCode = inputColors[i];
                boolean colorFound = false;
                for (int j = i; j < inputColors.length; j++) {
                    if (inputColors[j] != -1 && inputColors[j] % colorCode == 0) {
                        if (!colorFound) {
                            colorFound = true;
                            colors++;
                        }
                        inputColors[j] = -1;
                    }
                }
            }

            out.println(colors);
        }

        public void solveB() {

        }

        public void solveC() {

        }

        public void solveD() {

        }

        public void solveE() {

        }

        public void solveF() {

        }

        public void solveG() {

        }

        public void solveH() {

        }
    }

    private static long gcd(long a, long b) {
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }

    private static long lcm(long a, long b) {
        return (a * b) / gcd(a, b);
    }

    private static int min(int a, int b) {
        return a < b ? a : b;
    }

    private static int max(int a, int b) {
        return a > b ? a : b;
    }

    private static int min(ArrayList<Integer> list) {
        int min = Integer.MAX_VALUE;
        for (int el : list) {
            if (el < min) {
                min = el;
            }
        }
        return min;
    }

    private static int max(ArrayList<Integer> list) {
        int max = Integer.MIN_VALUE;
        for (int el : list) {
            if (el > max) {
                max = el;
            }
        }
        return max;
    }

    private static int min(int[] list) {
        int min = Integer.MAX_VALUE;
        for (int el : list) {
            if (el < min) {
                min = el;
            }
        }
        return min;
    }

    private static int max(int[] list) {
        int max = Integer.MIN_VALUE;
        for (int el : list) {
            if (el > max) {
                max = el;
            }
        }
        return max;
    }

    private static void fill(int[] array, int value) {
        for (int i = 0; i < array.length; i++) {
            array[i] = value;
        }
    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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

        int[] nextIntArray(int n) {
            int[] array = new int[n];
            for (int i = 0; i < n; i++) {
                array[i] = nextInt();
            }
            return array;
        }
    }
}