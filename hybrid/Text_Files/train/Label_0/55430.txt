import java.io.*;
import java.util.*;

public class Template implements Runnable {

    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok = new StringTokenizer("");

    void init() throws FileNotFoundException {
        try {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        } catch (Exception e) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }
    }

    class GraphBuilder {
        int n, m;
        int[] x, y;
        int index;
        int[] size;


        GraphBuilder(int n, int m) {
            this.n = n;
            this.m = m;
            x = new int[m];
            y = new int[m];
            size = new int[n];
        }

        void add(int u, int v) {
            x[index] = u;
            y[index] = v;
            size[u]++;
            size[v]++;
            index++;
        }

        int[][] build() {
            int[][] graph = new int[n][];
            for (int i = 0; i < n; i++) {
                graph[i] = new int[size[i]];
            }
            for (int i = index - 1; i >= 0; i--) {
                int u = x[i];
                int v = y[i];
                graph[u][--size[u]] = v;
                graph[v][--size[v]] = u;
            }
            return graph;
        }
    }

    String readString() throws IOException {
        while (!tok.hasMoreTokens()) {
            try {
                tok = new StringTokenizer(in.readLine());
            } catch (Exception e) {
                return null;
            }
        }
        return tok.nextToken();
    }

    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    int[] readIntArray(int size) throws IOException {
        int[] res = new int[size];
        for (int i = 0; i < size; i++) {
            res[i] = readInt();
        }
        return res;
    }

    long[] readLongArray(int size) throws IOException {
        long[] res = new long[size];
        for (int i = 0; i < size; i++) {
            res[i] = readLong();
        }
        return res;
    }

    long readLong() throws IOException {
        return Long.parseLong(readString());
    }

    double readDouble() throws IOException {
        return Double.parseDouble(readString());
    }

    <T> List<T>[] createGraphList(int size) {
        List<T>[] list = new List[size];
        for (int i = 0; i < size; i++) {
            list[i] = new ArrayList<>();
        }
        return list;
    }

    public static void main(String[] args) {
        new Template().run();
        // new Thread(null, new Template(), "", 1l * 200 * 1024 * 1024).start();
    }

    long timeBegin, timeEnd;

    void time() {
        timeEnd = System.currentTimeMillis();
        System.err.println("Time = " + (timeEnd - timeBegin));
    }

    long memoryTotal, memoryFree;

    void memory() {
        memoryFree = Runtime.getRuntime().freeMemory();
        System.err.println("Memory = " + ((memoryTotal - memoryFree) >> 10)
                + " KB");
    }

    public void run() {
        try {
            timeBegin = System.currentTimeMillis();
            memoryTotal = Runtime.getRuntime().freeMemory();
            init();
            solve();
            out.close();
            if (System.getProperty("ONLINE_JUDGE") == null) {
                time();
                memory();
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }

    void solve() throws IOException {
        int n = readInt();
        int S = 1000000;
        boolean[] has = new boolean[S + 1];
        for (int i = 0; i < n; i++) {
            has[readInt()] = true;
        }
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= S; i++) {
            int opposite = S - i + 1;
            if (i >= opposite) break;
            if (!has[i] && !has[opposite]) {
                deque.add(i);
                deque.add(opposite);
            }
        }

        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i <= S; i++) {
            int opposite = S - i + 1;
            if (has[i]) {
                if (!has[opposite]) {
                    answer.add(opposite);
                } else {
                    has[i] = has[opposite] = false;
                    answer.add(deque.pollFirst());
                    answer.add(deque.pollFirst());
                }
                has[i] = false;
            }
        }

        out.println(answer.size());
        for (int x : answer) out.print(x + " ");

    }


}