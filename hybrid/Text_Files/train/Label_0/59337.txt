import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class C {
    static class BIT {
        int size;
        long[] tree;

        public BIT(int size) {
            this.size = size + 1;
            this.tree = new long[this.size];
        }

        public void update(int x, long val) {
            while (x < this.size) {
                this.tree[x] += val;
                x += (x & -x);
            }
        }

        public long read(int x) {
            long s = 0L;
            while (x > 0) {
                s += this.tree[x];
                x -= (x & -x);
            }
            return s;
        }
    }
    
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
        
        double nextDouble(){
            return Double.parseDouble(next());
        }
    }

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        
        int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt();
        
        long[] arr = new long[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextLong();

        int[][] operations = new int[m][3];
        for (int i = 0; i < m; i++) {
            operations[i][0] = sc.nextInt();
            operations[i][1] = sc.nextInt();
            operations[i][2] = sc.nextInt();
        }

        BIT operBit = new BIT(m + 1);
        for (int i = 0; i < k; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            operBit.update(a, 1);
            operBit.update(b + 1, -1);
        }

        BIT arrBit = new BIT(n + 1);
        for (int i = 1; i <= m; i++) {
            long times = operBit.read(i);
            if (times > 0) {
                int l = operations[i-1][0];
                int r = operations[i-1][1];
                long d = operations[i-1][2];
                
                arrBit.update(l, times * d);
                arrBit.update(r + 1, -times * d);
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (i + 1 == n)
                System.out.printf("%d", arr[i] + arrBit.read(i + 1));
            else
                System.out.printf("%d ", arr[i] + arrBit.read(i + 1));
        }
    }
}