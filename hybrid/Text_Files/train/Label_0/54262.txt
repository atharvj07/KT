import java.util.List;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.ArrayList;
import java.io.PrintStream;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
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
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }
}

class TaskD {
    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int m = in.nextInt();
        int k = in.nextInt();
        int p = in.nextInt();

        List<Integer>[] adj = new List[m];
        for (int i = 0; i < adj.length; ++i) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m - 1; ++i) {
            int a = in.nextInt() - 1;
            int b = in.nextInt() - 1;
            adj[a].add(b);
            adj[b].add(a);
        }
        int []level = new int[m];
        dfs(0, adj, level, 1);
        Arrays.sort(level);
        int lo = 0;
        int hi = Math.min(k, m - 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (cost(level, mid) <= p) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        out.println(hi);
    }

    void dfs(int at, List<Integer>[] adj, int[] level, int curLevel) {
        level[at] = curLevel;
        for (int to : adj[at]) {
            if (level[to] == 0) {
                dfs(to, adj, level, curLevel + 1);
            }
        }
    }

    long cost(int []level, int k) {
        long sum = 0;
        for (int i = 0; i < k; ++i) {
            sum += level[level.length - 1 - i];
        }
        int last = level.length - 1;
        long res = (long)level[last] * k - sum;
        while (last - k > 0) {
            sum -= level[last];
            sum += level[last - k];
            --last;
            long cost = (long)level[last] * k - sum;
            if (res > cost) {
                res = cost;
            }
        }
        System.err.printf("cost(%d) = %d\n", k, res);
        return res;
    }
}

class InputReader {
    BufferedReader bufReader;
    StringTokenizer stringTokenizer;

    public InputReader(InputStream stream) {
        bufReader = new BufferedReader(new InputStreamReader(stream));
    }

    String nextString() {
        while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
            try {
                String line = bufReader.readLine();
                if (line == null) {
                    return null;
                }
                stringTokenizer = new StringTokenizer(line);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
        }
        return stringTokenizer.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(nextString());
    }

    }
