import java.util.*;

public class Main {

    static int n;
    static int[] a;
    static int[][] g;
    static int[] b;
    static int[] lis;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        g = buildGraph(sc, n, n-1);
        b = new int[n];
        Arrays.fill(b, -1);
        b[0] = 1;
        lis = new int[n+1];
        Arrays.fill(lis, Integer.MAX_VALUE);
        lis[0] = 0;
        dfs(0, 0);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(b[i] + "\n");
        }
        System.out.print(sb.toString());
        sc.close();

    }

    private static void dfs(int i, int max) {
        int x = a[i];
        int l = 0, r = n;
        while(1 < r - l){
            int m = (l + r) / 2;
            if(lis[m] < x) l = m;
            else r = m;
        }
        b[i] = Math.max(r, max);
        int tmp = lis[r];
        lis[r] = x;
        for(int nv : g[i]){
            if(b[nv] < 0) dfs(nv, b[i]);
        }
        lis[r] = tmp;
    }

    public static int[][] buildGraph(Scanner sc, int n, int m) {
        int[][] graph = new int[n][];
        int[][] edges = new int[m][2];
        int[] deg = new int[n];
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            edges[i][0] = a;
            edges[i][1] = b;
            deg[a]++;
            deg[b]++;
        }
        for (int i = 0; i < n; i++) {
            graph[i] = new int[deg[i]];
        }
        for (int i = 0; i < m; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            graph[a][--deg[a]] = b;
            graph[b][--deg[b]] = a;
        }

        return graph;
    }

}
