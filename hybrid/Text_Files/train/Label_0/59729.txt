import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        Task6665 solver = new Task6665();
        try {
            int testNumber = 1;
            while (true)
                solver.solve(testNumber++, in, out);
        } catch (UnknownError e) {
            out.close();
        }
    }
}

class Task6665 {
    static final int INF = (int) 1e9;

    static class Vertex {
        int[] adj = new int[2];
    }

    Vertex[][] g;
    Map<Integer, Integer> tmp;

    {
        int[] perm = new int[9];
        g = new Vertex[362880][2];
        tmp = new HashMap<Integer, Integer>();
        for (int i = 0; i < perm.length; i++) {
            perm[i] = i;
        }
        for (int i = 0; i < g.length; i++) {
            for (int j = 0; j < 2; j++) {
                g[i][j] = new Vertex();
            }
        }
        for (int i = 0;; i++) {
            int s = 0;
            for (int j = 0; j < perm.length; j++) {
                s = s * 10 + perm[j];
            }
            tmp.put(s, i);
            if (!nextPermutation(perm)) {
                break;
            }
        }
        for (int i = 0; i < perm.length; i++) {
            perm[i] = i;
        }
        for (int cur = 0;; cur++) {
            for (int i = 0; i < 9; i++) {
                if (perm[i] == 0) {
                    for (int j = -1, l = 0; j <= 1; j += 2, l++) {
                        int k = i + j;
                        int now = 0;
                        if (k < 0) {
                            k += 9;
                        }
                        if (k >= 9) {
                            k -= 9;
                        }
                        for (int x = 0; x < 9; x++) {
                            if (x == i) {
                                now = now * 10 + perm[k];
                            } else if (x == k) {
                                now = now * 10 + perm[i];
                            } else {
                                now = now * 10 + perm[x];
                            }
                        }
                        g[cur][0].adj[l] = tmp.get(now);
                    }
                    for (int j = -3, l = 0; j <= 3; j += 6, l++) {
                        int k = i + j;
                        int now = 0;
                        if (k < 0) {
                            k += 9;
                        }
                        if (k >= 9) {
                            k -= 9;
                        }
                        for (int x = 0; x < 9; x++) {
                            if (x == i) {
                                now = now * 10 + perm[k];
                            } else if (x == k) {
                                now = now * 10 + perm[i];
                            } else {
                                now = now * 10 + perm[x];
                            }
                        }
                        g[cur][1].adj[l] = tmp.get(now);
                    }
                    break;
                }
            }
            if (!nextPermutation(perm)) {
                break;
            }
        }
    }

    public void solve(int testNumber, InputReader in, OutputWriter out) {
        int s = 0;
        int t = 0;
        int[] cost = new int[2];
        int[] best = new int[]{0, 1};
        final int[] res = new int[g.length];
        boolean[] mark = new boolean[g.length];
        TreeSet<Integer> set = new TreeSet<Integer>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (o1.equals(o2))
                    return 0;
                else if (res[o1] == res[o2])
                    return -1;
                else
                    return res[o1] - res[o2];
            }
        });
        for (int i = 0; i < 2; i++) {
            cost[i] = in.readInt();
        }
        if (cost[0] + cost[1] == 0)
            throw new UnknownError();
        for (int i = 0; i < 9; i++) {
            s = s * 10 + in.readInt();
        }
        for (int i = 0; i < 9; i++) {
            t = t * 10 + in.readInt();
        }
        Arrays.fill(res, INF);
        res[tmp.get(s)] = 0;
        mark[tmp.get(s)] = true;
        set.add(tmp.get(s));
        if (cost[0] > cost[1]) {
            best[0] = 1;
            best[1] = 0;
        }
        int target = tmp.get(t);
        while (!set.isEmpty()) {
            int x = set.pollFirst();
            if (x == target) {
                break;
            }
            mark[x] = false;
            for (int k = 0; k < 2; k++) {
                int i = best[k];
                for (int j : g[x][i].adj) {
                    int y = res[x] + cost[i];
                    if (res[j] > y && y < res[target]) {
                        if (mark[j])
                            set.remove(j);
                        res[j] = y;
                        mark[j] = true;
                        set.add(j);
                    }
                }
            }
        }
        out.printLine(res[target]);
    }

    private boolean nextPermutation(int[] perm) {
        for (int i = perm.length - 2; i >= 0; i--) {
            if (perm[i] < perm[i + 1]) {
                int tmp = perm[i + 1];
                for (int j = i + 1; j < perm.length; j++) {
                    if (perm[j] > perm[i]) {
                        tmp = Math.min(tmp, perm[j]);
                    }
                }
                for (int j = i + 1; j < perm.length; j++) {
                    if (tmp == perm[j]) {
                        perm[j] = perm[i];
                        perm[i] = tmp;
                        break;
                    }
                }
                Arrays.sort(perm, i + 1, perm.length);
                return true;
            }
        }
        return false;
    }
}

class InputReader {

    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;

    public InputReader(InputStream stream) {
        this.stream = stream;
    }

    public int read() {
        if (numChars == -1)
            throw new InputMismatchException();
        if (curChar >= numChars) {
            curChar = 0;
            try {
                numChars = stream.read(buf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (numChars <= 0)
                return -1;
        }
        return buf[curChar++];
    }

    public int readInt() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        int res = 0;
        do {
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        } while (!isSpaceChar(c));
        return res * sgn;
    }

    public boolean isSpaceChar(int c) {
        if (filter != null)
            return filter.isSpaceChar(c);
        return isWhitespace(c);
    }

    public static boolean isWhitespace(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public interface SpaceCharFilter {
        public boolean isSpaceChar(int ch);
    }
}

class OutputWriter {
    private final PrintWriter writer;

    public OutputWriter(OutputStream outputStream) {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public void close() {
        writer.close();
    }

    public void printLine(int i) {
        writer.println(i);
    }
}