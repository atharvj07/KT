import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.io.FilterInputStream;
import java.io.BufferedInputStream;
import java.util.Set;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author nirav
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scan in = new Scan(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BChemicalTable solver = new BChemicalTable();
        solver.solve(1, in, out);
        out.close();
    }

    static class BChemicalTable {
        static int[] parent;

        public void solve(int testNumber, Scan in, PrintWriter out) {
            int n = in.scanInt(), m = in.scanInt(), q = in.scanInt();
            parent = new int[n + m];
            for (int i = 0; i < n + m; i++) parent[i] = i;
            while (q-- > 0) {
                int a = in.scanInt();
                int b = in.scanInt();
                a--;
                b--;
                b += n;
                if (parent[b] != b) {
                    parent[a] = findParentof(a);
                    parent[b] = findParentof(b);
                    parent[findParentof(a)] = findParentof(b);
                } else {
                    parent[a] = findParentof(a);
                    parent[b] = findParentof(b);
                    parent[findParentof(b)] = findParentof(a);
                }
            }
            Set<Integer> set = new HashSet<>();
            for (int i = 0; i < n + m; i++) set.add(findParentof(i));
            out.println(set.size() - 1);

        }

        static int findParentof(int k) {
            if (parent[k] == k) return k;
            while (parent[k] != k) k = parent[k];
            return k;

        }

    }

    static class Scan {
        private byte[] buf = new byte[4 * 1024];
        private int INDEX;
        private BufferedInputStream in;
        private int TOTAL;

        public Scan(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }

        private int scan() {
            if (INDEX >= TOTAL) {
                INDEX = 0;
                try {
                    TOTAL = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (TOTAL <= 0) return -1;
            }
            return buf[INDEX++];
        }

        public int scanInt() {
            int I = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    I *= 10;
                    I += n - '0';
                    n = scan();
                }
            }
            return neg * I;
        }

        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }

    }
}

