import java.io.*;
import java.util.*;

public class Main implements Runnable{
    private ArrayList<ArrayList<Integer>> graph;
    private int clock = 0;
    public static void main(String[] args) throws Exception {
        new Thread(null, new Main(), "bridge", 16 * 1024 * 1024).start();
    }

    @Override
    public void run() {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void solve() throws Exception{
        FastScanner scanner = new FastScanner(System.in);

        int V = scanner.nextInt();
        int E = scanner.nextInt();

        graph = new ArrayList<>(V);

        for(int i = 0; i < V; ++i){
            graph.add(new ArrayList<Integer>());
        }

        for(int i = 0; i < E; ++i){
            int u = scanner.nextInt();
            int v = scanner.nextInt();

            graph.get(u).add(v);
        }

        boolean[] visited = new boolean[V];
        int[] disc = new int[V];
        int[] low = new int[V];
        int[] result = new int[V];

        Stack<Integer> stack = new Stack<>();
        boolean[] inStack = new boolean[V];

        for(int i = 0; i < V; ++i){
            if(!visited[i]){
                dfsUtil(i, visited, disc, low, result, stack, inStack);
            }
        }

        int Q = scanner.nextInt();
        PrintWriter printWriter = new PrintWriter(System.out);
        for(int i = 0; i < Q; ++i){
            int u = scanner.nextInt();
            int v = scanner.nextInt();

            printWriter.println(result[u] == result[v] ? "1" : "0");
        }

        printWriter.flush();
    }

    private void dfsUtil(int u, boolean[] visited, int[] disc, int[] low, int[] result, Stack<Integer> stack, boolean[] inStack){
        visited[u] = true;
        disc[u] = low[u] = ++clock;
        stack.push(u);
        inStack[u] = true;

        for(int v : graph.get(u)){
            if(!visited[v]){
                dfsUtil(v, visited, disc, low, result, stack, inStack);

                low[u] = Math.min(low[u], low[v]);
            }
            else if(inStack[v]){
                low[u] = Math.min(low[u], disc[v]);
            }
        }

        if(disc[u] == low[u]){
            while(!stack.isEmpty()){
                int v = stack.pop();
                inStack[v] = false;
                result[v] = low[u];

                if(v == u){
                    break;
                }
            }
        }
    }

    static class FastScanner {
        private InputStream in;
        private final byte[] buffer = new byte[1024 * 8];
        private int ptr = 0;
        private int buflen = 0;

        public FastScanner(InputStream in){
            this.in = in;
        }

        private boolean hasNextByte() {
            if (ptr < buflen) {
                return true;
            } else {
                ptr = 0;
                try {
                    buflen = in.read(buffer);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (buflen <= 0) {
                    return false;
                }
            }
            return true;
        }

        private int readByte() {
            if (hasNextByte()) return buffer[ptr++];
            else return -1;
        }

        private static boolean isPrintableChar(int c) {
            return 33 <= c && c <= 126;
        }

        private void skipUnprintable() {
            while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
        }

        public boolean hasNext() {
            skipUnprintable();
            return hasNextByte();
        }

        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while (isPrintableChar(b)) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}