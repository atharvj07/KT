import java.util.*;
import java.io.*;
 
public class B {
    static class Pair {
        int a, b;

        public Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }

        public String toString() {
            return "(" + a + ", " + b + ")";
        }
    }
    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner(System.in);
        // Scanner input = new Scanner(new File("input.txt"));
        PrintWriter output = new PrintWriter(System.out);

        int t = input.nextInt();
        for (int q = 0; q < t; q++) {
            int n = input.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = input.nextLong();
            }
            Arrays.sort(a);

            long a1 = a[0] * a[1] * a[2] * a[3] * a[4];
            long a2 = a[0] * a[1] * a[2] * a[3] * a[n - 1];
            long a3 = a[0] * a[1] * a[2] * a[n - 2] * a[n - 1];
            long a4 = a[0] * a[1] * a[n - 3] * a[n - 2] * a[n - 1];
            long a5 = a[0] * a[n - 4] * a[n - 3] * a[n - 2] * a[n - 1];
            long a6 = a[n - 5] * a[n - 4] * a[n - 3] * a[n - 2] * a[n - 1];

            long ans = Math.max(a1, a2);
            ans = Math.max(ans, a3);
            ans = Math.max(ans, a4);
            ans = Math.max(ans, a5);
            ans = Math.max(ans, a6);

            output.println(ans);
        }        

        output.close();
    }
 
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
 
        FastScanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }
 
        FastScanner(FileReader s) {
            br = new BufferedReader(s);
        }
 
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
 
        String nextLine() throws IOException {
            return br.readLine();
        }
 
        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
 
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
 
        long nextLong() throws IOException {
            return Long.parseLong(next());
        }
    }
}
