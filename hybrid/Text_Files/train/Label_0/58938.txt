import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BFixATree solver = new BFixATree();
        solver.solve(1, in, out);
        out.close();
    }

    static class BFixATree {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int[] arr = new int[n + 1];
            ArrayList<Integer> roots = new ArrayList<>();
            ArrayList<Integer> loops = new ArrayList<>();
            BFixATree.DisjointSet ds = new BFixATree.DisjointSet(n);
            for (int i = 1; i <= n; i++) {
                arr[i] = in.nextInt();
                if (arr[i] == i) roots.add(i);
                else {
                    if (ds.isInSameSet(arr[i], i)) {
                        loops.add(i);
                    } else ds.union(arr[i], i);
                }
            }
            if (roots.size() == 0 && loops.size() == 0) {
                out.printf("%d\n", 0);
                for (int i = 1; i <= n; i++) out.printf("%d ", arr[i]);
                return;
            }
            int changes = 0;
            int top;
            if (roots.size() != 0) top = roots.get(0);
            else top = loops.get(0);
            for (int x : loops) {
                if (arr[x] != top) changes++;
                arr[x] = top;
            }
            for (int x : roots) {
                if (arr[x] != top) changes++;
                arr[x] = top;
            }
            out.printf("%d\n", changes);
            for (int i = 1; i <= n; i++) out.printf("%d ", arr[i]);
        }

        static class DisjointSet {
            private int[] parent;
            private int[] setSize;
            private int numOfSets;

            private DisjointSet(int n) {
                parent = new int[n + 1];
                setSize = new int[n + 1];
                for (int i = 1; i <= n; i++) {
                    parent[i] = i;
                    setSize[i] = i;
                }
            }

            private int root(int x) {
                if (x == parent[x]) return x;
                return parent[x] = root(parent[x]);
            }

            private boolean union(int n1, int n2) {
                return _union(root(n1), root(n2));
            }

            private boolean _union(int n1, int n2) {
                if (n1 == n2) return false;
                if (setSize[n1] > setSize[n2]) {
                    parent[n2] = parent[n1];
                    setSize[n1] += setSize[n2];
                } else {
                    parent[n1] = parent[n2];
                    setSize[n2] += setSize[n1];
                }
                numOfSets--;
                return true;
            }

            private boolean isInSameSet(int n1, int n2) {
                return root(n1) == root(n2);
            }

        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public InputReader(FileInputStream file) {
            this.stream = file;
        }

        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res = (res << 3) + (res << 1) + c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }
}

