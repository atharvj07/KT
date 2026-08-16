import java.util.*;
import java.io.*;
import java.math.*;

public class main {
    public static void main(String[] args) throws Exception {
        Reader in = new Reader(System.in);
        PrintWriter out = Writer.writer(System.out);                

        int n = in.nextInt();
        int a[] = new int[350];
        int pre = 1;
        for (int i = 0; i < n; i++) {
            int x = in.nextInt();
            boolean found = false;
            build:
            for (int j = 0; j <= pre; j++) {
                int cur = 9 - a[j];
                if (cur == 0) continue;
                int sum = 0;
                for (int k = j + 1; k < pre; k++) {
                    sum += a[k];
                }
                for (int k = a[j] + 1; k <= 9; k++) {
                    if (x - sum - k <= j * 9 && x - sum - k >= 0) {
                        for (int q = pre - 1; q > j; q--)
                            out.print(a[q]);
                        a[j] = k;
                        out.print(k);
                        int ost = x - sum - k;
                        for (int q = 0; q < j; q++) {
                            if (ost > 9) {
                                ost -= 9;
                                a[q] = 9;
                            }
                            else {
                                a[q] = ost;
                                ost -= ost;
                            }
                        }
                        for (int q = j - 1; q >= 0; q--)
                            out.print(a[q]);
                        out.println();
                        if (j == pre) pre++;
                        found = true;
                        break build;
                    }
                }
            }
            if (found == false) {
                Arrays.fill(a, 0);
                pre = 0;
                while (x > 0) {
                    int d = Math.min(9, x);
                    a[pre] = d;
                    x -= d;
                    pre++;
                }
                for (int j = pre - 1; j >= 0; j--)
                    out.print(a[j]);
                out.println();
            }
        }
        out.close();
    }
}

class Reader {
    BufferedReader reader;
    StringTokenizer str;
    Reader(String filename) throws Exception {
        reader = new BufferedReader(new FileReader(filename));
    }
    Reader(InputStream input) throws Exception {
        reader = new BufferedReader(new InputStreamReader(input));
    }
    public String next() throws Exception {
        while (str == null || str.hasMoreTokens() == false) {
            str = new StringTokenizer(reader.readLine());
        }
        return str.nextToken();
    }
    public long nextLong() throws Exception {
        return Long.parseLong(next());
    }
    public int nextInt() throws Exception {
        return Integer.parseInt(next());
    }
    public double nextDouble() throws Exception {
        return Double.parseDouble(next());
    }
}

class Writer {
    public static PrintWriter writer(String filename) throws Exception {
        return new PrintWriter(new File(filename));
    }
    public static PrintWriter writer(OutputStream output) throws Exception {
        return new PrintWriter(output);
    }
}