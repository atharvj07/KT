
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.PrintWriter;

public class Main {

    static long binary_search(long A[], int n, long x) {
        int l = 0, r = n - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (A[m] < x) {
                l = m + 1;
            } else if (A[m] > x) {
                r = m - 1;
            } else {
                return m;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner();
        PrintWriter pw = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.next());
        if (n == 1) {
            System.out.println(0);
        } else {
            long a[] = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(sc.next());
            }
            int i = 0;
            int j = n - 1;
            long sum1[] = new long[n - 1];
            long sum2[] = new long[n - 1];
            sum1[0] = a[0];
            sum2[0] = a[n - 1];
            for (int k = 1; k < n - 1; k++) {
                sum1[k] = a[k] + sum1[k - 1];
//            System.out.println(sum1[k]);
            }
            for (int k = 1; k < n - 1; k++) {
                sum2[k] = a[n - k - 1] + sum2[k - 1];
//            System.out.println(sum2[k]);
            }
            long max = 0;
            for (int k = 0; k < n - 1; k++) {
//            System.out.println(sum1[k]);
                long index = binary_search(sum2, n - 1, sum1[k]);
                if (index != -1 && index < n - k - 1) {
                    max = Math.max(sum1[k], max);
//                System.out.println(k);
                }
            }
            System.out.println(max);
        }
    }

    static class Scanner {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        int spaces = 0;

        public String nextLine() throws IOException {
            if (spaces-- > 0) {
                return "";
            } else if (st.hasMoreTokens()) {
                return new StringBuilder(st.nextToken("\n")).toString();
            }
            return br.readLine();
        }

        public String next() throws IOException {
            spaces = 0;
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            return st.nextToken();
        }

        public boolean hasNext() throws IOException {
            while (!st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) {
                    return false;
                }
                if (line.equals("")) {
                    spaces = Math.max(spaces, 0) + 1;
                }
                st = new StringTokenizer(line);
            }
            return true;
        }
    }
}