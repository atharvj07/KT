import java.util.*;
import java.io.*;
import java.math.*;

public class Main {

    final int mod = 1000000007;
    static FastReader sc;

    public static void solution() {
        int n = sc.nextInt();
        int a[] = new int[n];
        for(int i=0; i<n; i++) a[i] = sc.nextInt();
        int[] temp = new int[n];
        for(int i = n-1; i>=0; i--) {
            if(i + a[i] >= n) temp[i] = a[i];
            else temp[i] = a[i] + temp[i + a[i]];
        }
        int max = Integer.MIN_VALUE;
        for(int i=0; i<n; i++ ) {
            if(max< temp[i]) max = temp[i];
        }
        System.out.println(max);
    }

    // Fast IO
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() throws FileNotFoundException {
            File in = new File("input.txt");
            if (in.exists()) {
                br = new BufferedReader(new InputStreamReader(new FileInputStream("input.txt")));
            } else {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
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

        float nextFloat() {
            return Float.parseFloat(next());
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
    }

    // GCD
    public static int __gcd(int a, int b) {
        BigInteger n1 = BigInteger.valueOf(a);
        BigInteger n2 = BigInteger.valueOf(b);
        BigInteger gcd = n1.gcd(n2);
        return gcd.intValue();
    }

    public static long __gcd(long a, long b) {
        BigInteger n1 = BigInteger.valueOf(a);
        BigInteger n2 = BigInteger.valueOf(b);
        BigInteger gcd = n1.gcd(n2);
        return gcd.longValue();
    }

    public static void main(String args[]) throws FileNotFoundException {
        try {
            File out = new File("output.txt");
            sc = new FastReader();
            if (out.exists()) {
                System.setOut(new PrintStream(out));
            }

            int test_cases = 1;
             test_cases = sc.nextInt();
            while (test_cases-- > 0) {
                solution();
            }
        } catch (Exception e) {
            return;
        }
    }
}