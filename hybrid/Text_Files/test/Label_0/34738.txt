import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.NoSuchElementException;
public class Main implements Runnable{
	int N;
    double P,memo;
    boolean[] used;
    ArrayList<Edge>[] graph;
    private class Edge{
        int to,cost;
        public Edge(int to,int cost){
            this.to = to;
            this.cost = cost;
        }
    }

    public double dfs_T(int v){
        double ret = 0.0;

        for(Edge e : graph[v]){
            if(used[e.to])continue;
            used[e.to] = true;
            ret += (dfs_T(e.to) + e.cost) * P;
            used[e.to] = false;
        }
        return ret;
    }

    public double dfs(int v){

        double ret = memo;

        for(Edge e : graph[v]){
            if(used[e.to])continue;
            used[e.to] = true;
            ret += (dfs(e.to) + e.cost) * P;
            used[e.to] = false;
        }
        return ret;
    }

    @SuppressWarnings("unchecked")
    public void solve() {
        P = nextDouble();
        N = nextInt();

        graph = new ArrayList[N];
        for(int i = 0;i < N;i++){
            graph[i] = new ArrayList<Edge>();
        }

        for(int i = 0;i < N-1;i++){

            int x = nextInt()-1;
            int y = nextInt()-1;
            int c = nextInt();

            graph[x].add(new Edge(y,c));
            graph[y].add(new Edge(x,c));
        }

        used = new boolean[N];
        used[0] = true;
        memo = dfs_T(0);
        out.println(String.format("%.09f",dfs(0)));
    }

    public static void main(String[] args) {
        new Thread(null,new Main(),"",64 * 1024 * 1024).start();
    }

    /* Input */
    private static final InputStream in = System.in;
    private static final PrintWriter out = new PrintWriter(System.out);
    private final byte[] buffer = new byte[2048];
    private int p = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
        if (p < buflen)
            return true;
        p = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (buflen <= 0)
            return false;
        return true;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrint(buffer[p])) {
            p++;
        }
        return hasNextByte();
    }

    private boolean isPrint(int ch) {
        if (ch >= '!' && ch <= '~')
            return true;
        return false;
    }

    private int nextByte() {
        if (!hasNextByte())
            return -1;
        return buffer[p++];
    }

    public String next() {
        if (!hasNext())
            throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = -1;
        while (isPrint((b = nextByte()))) {
            sb.appendCodePoint(b);
        }
        return sb.toString();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }

    @Override
    public void run() {
        out.flush();
        new Main().solve();
        out.close();

    }
}