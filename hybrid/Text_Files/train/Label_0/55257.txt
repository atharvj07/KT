import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.Collection;
import java.util.InputMismatchException;
import java.util.Random;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Rustam Musin (t.me/musin_acm)
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        B2DoktorVstrechaetVeideraSrednyaya solver = new B2DoktorVstrechaetVeideraSrednyaya();
        solver.solve(1, in, out);
        out.close();
    }

    static class B2DoktorVstrechaetVeideraSrednyaya {
        List<Integer>[] g2;
        int[] parent;
        boolean[] used;
        Random rnd = new Random(239);

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.readInt();
            int m = in.readInt();
            List<Integer>[] g = new List[n];
            for (int i = 0; i < n; i++) {
                g[i] = new ArrayList<>();
            }
            for (int i = 0; i < m; i++) {
                int a = in.readInt() - 1;
                int b = in.readInt() - 1;
                g[a].add(b);
                g[b].add(a);
            }
            int[][] distances = distances(g);

            int s = in.readInt();
            int b = in.readInt();
            int k = in.readInt();
            int h = in.readInt();
            Ship[] ships = new Ship[s];
            for (int i = 0; i < s; i++) {
                int pos = in.readInt() - 1;
                int attack = in.readInt();
                int maxDist = in.readInt();
                ships[i] = new Ship(pos, attack, maxDist);
            }
            Base[] bases = new Base[b];
            for (int i = 0; i < b; i++) {
                int pos = in.readInt() - 1;
                int defence = in.readInt();
                bases[i] = new Base(pos, defence);
            }

            g2 = new List[s];
            for (int i = 0; i < s; i++) {
                g2[i] = new ArrayList<>();
                Ship ship = ships[i];
                for (int j = 0; j < b; j++) {
                    Base base = bases[j];
                    if (ship.maxDist >= distances[ship.pos][base.pos] && ship.attack >= base.defence) {
                        g2[i].add(j);
                    }
                }
            }

            for (int i = 0; i < s; i++) {
                Collections.shuffle(g2[i], rnd);
            }
            int ans = 0;
            parent = new int[b];
            Arrays.fill(parent, -1);
            int[] order = randomOrder(s);
            for (int i : order) {
                used = new boolean[s];
                if (dfs(i)) {
                    ans++;
                }
            }

            out.print(Math.min(s * (long) h, ans * (long) k));
        }

        boolean dfs(int v) {
            if (used[v]) {
                return false;
            }
            used[v] = true;
            for (int to : g2[v]) {
                if (parent[to] == -1 || dfs(parent[to])) {
                    parent[to] = v;
                    return true;
                }
            }
            return false;
        }

        int[] randomOrder(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = i;
                int at = rnd.nextInt(i + 1);
                int t = a[at];
                a[at] = a[i];
                a[i] = t;
            }
            return a;
        }

        int[][] distances(List<Integer>[] g) {
            int n = g.length;
            int[][] distances = new int[n][n];
            for (int i = 0; i < n; i++) {
                findDist(g, distances[i], i);
            }
            return distances;
        }

        void findDist(List<Integer>[] g, int[] dist, int from) {
            Arrays.fill(dist, -1);
            dist[from] = 0;
            Queue<Integer> q = new ArrayDeque<>();
            q.add(from);
            while (!q.isEmpty()) {
                int cur = q.poll();
                for (int to : g[cur]) {
                    if (dist[to] == -1) {
                        dist[to] = dist[cur] + 1;
                        q.add(to);
                    }
                }
            }
        }

        class Ship {
            int pos;
            int attack;
            int maxDist;

            Ship(int pos, int attack, int maxDist) {
                this.pos = pos;
                this.attack = attack;
                this.maxDist = maxDist;
            }

            public String toString() {
                return "Ship{" +
                  "pos=" + pos +
                  ", attack=" + attack +
                  ", maxDist=" + maxDist +
                  '}';
            }

        }

        class Base {
            int pos;
            int defence;

            Base(int pos, int defence) {
                this.pos = pos;
                this.defence = defence;
            }

            public String toString() {
                return "Base{" +
                  "pos=" + pos +
                  ", defence=" + defence +
                  '}';
            }

        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void close() {
            writer.close();
        }

        public void print(long i) {
            writer.print(i);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
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

        public int readInt() {
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
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

