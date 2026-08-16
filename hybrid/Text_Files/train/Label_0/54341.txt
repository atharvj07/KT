//package com.company;
import java.util.*;

public class Main {
    static ArrayList<Edge>[] gr;
    static boolean[] mark;
    static int[] cover;

    static class Edge {
        int to, num;
        Edge(int to, int num) {
            this.to = to;
            this.num = num;
        }
    }

    static boolean DFS(int x, int y, int p) {
        if (x == y) return true;
        for (Edge e : gr[x]) {
            if (e.to == p) continue;
            if (DFS(e.to, y, x)) {
                mark[e.num] = true;
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        gr = new ArrayList[n];
        for (int i = 0; i < n; i++)
            gr[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++)
        {
            int u = sc.nextInt(), v = sc.nextInt();
            u--;
            v--;
            gr[u].add(new Edge(v, i));
            gr[v].add(new Edge(u, i));
        }
        int m = sc.nextInt();
        cover = new int[n];
        for (int i = 0; i < m; i++)
        {
            int u = sc.nextInt(), v = sc.nextInt();
            u--;
            v--;

            mark = new boolean[n];
            for (int j = 0; j < n; j++)
                mark[j] = false;

            DFS(u, v, -1);

            for (int j = 0; j < n - 1; j++)
                if (mark[j])
                    cover[j] |= (1 << i);
        }

        long d[] = new long[1 << m];
        d[0] = 1;

        for (int i = 0; i < n - 1; i++)
            for (int x = (1 << m) - 1; x >= 0; x--) {
                long q = d[x];
                //d[x] += q;
                d[x | cover[i]] += q;
            }

        System.out.println(d[(1 << m) - 1]);
    }
}
