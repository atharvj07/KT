import java.io.*;
import java.util.*;

class Main {
    static class Pair {
        int to;
        long w;
        Pair(int t, long wt) {
            to = t;
            w = wt;
        }
    }
    static long[] depth;
    static ArrayList<Pair>[] v;
    static boolean[] visited;
    public static void main(String[] args) {
        InputReader in = new InputReader();
        PrintWriter out = new PrintWriter(System.out);
        int n = in.nextInt();
        depth = new long[n];
        v = new ArrayList[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) v[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            int x = in.nextInt() - 1;
            int y = in.nextInt() - 1;
            long w = in.nextLong();
            v[x].add(new Pair(y, w));
            v[y].add(new Pair(x, w));
        }
        int q = in.nextInt();
        int k = in.nextInt() - 1;
        dfs(k, -1, 0);
        for (int i = 0; i < q; i++) {
            int x = in.nextInt() - 1;
            int y = in.nextInt() - 1;
            out.println(depth[x] + depth[y]);
        }
        out.close();
    }

    static void dfs(int source, int parent, long d) {
        visited[source] = true;
        depth[source] = d;
        for (Pair a : v[source]) {
            if (!visited[a.to]) {
                dfs(a.to, source, d + a.w);
            }
        }
    }

    static class InputReader {
        BufferedReader br;
        StringTokenizer st;

        public InputReader()
        {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt()
        {
            return Integer.parseInt(next());
        }

        long nextLong()
        {
            return Long.parseLong(next());
        }

        double nextDouble()
        {
            return Double.parseDouble(next());
        }

        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
}

