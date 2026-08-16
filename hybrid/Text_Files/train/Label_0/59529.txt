/*
 *  Date: 5/10/12
 *   Time: 12:23
 *   Author: 
 *      Alexander Marchuk
 *      aamarchuk@gmail.com
 */

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class AutoProgramming {

    static int N = 3000;

    public class Edge {
        int x, y, cost;
        int f, c;
    }

    public static class Task {
        int t;
        int s;
        int c;
    }

    int n, m, inf = (int) 1e9, nn, k;
    int[] d = new int[N];
    int[] u = new int[N];
    int[] phi = new int[N];
    int[] from = new int[N];
    int[] times = new int[N];
    ArrayList<Integer>[] g = new ArrayList[N];

    Task[] task = new Task[N];
    Edge[] a = new Edge[10 * N];

    public void addEdge(int x, int y, int z, int c) {
        a[m] = new Edge();
        a[m].x = x;
        a[m].y = y;
        a[m].cost = z;
        a[m].c = c;
        a[m].f = 0;
        g[x].add(m);
        m++;
        a[m] = new Edge();
        a[m].x = y;
        a[m].y = x;
        a[m].cost = -z;
        a[m].c = 0;
        a[m].f = 0;
        g[y].add(m);
        m++;
    }

    public boolean dijkstra(int s, int t) {
        for (int i = 0; i < n; i++) {
            u[i] = 0;
            d[i] = inf;
            from[i] = -1;
        }

        d[s] = 0;
        while (true) {
            int v = -1;
            for (int i = 0; i < n; i++) {
                boolean uu = false;
                if (u[i] > 0) {
                    uu = true;
                }
                if (!uu && (v == -1 || d[v] > d[i])) {
                    v = i;
                }
            }
            if (v == -1 || d[v] == inf) {
                break;
            }
            u[v] = 1;
            for (int i = 0; i < (int) g[v].size(); i++) {
                int to = g[v].get(i);
                int x = v, y = a[to].y, z = a[to].cost,
                        f = a[to].f, c = a[to].c;
                if (c <= f)
                    continue;
                if (d[y] > d[x] + phi[x] - phi[y] + z) {
                    d[y] = d[x] + phi[x] - phi[y] + z;
                    from[y] = to;
                }
            }
        }
        return (d[t] < inf);
    }

    public void fordBellman(int s) {
        for (int i = 0; i < n; i++)
            phi[i] = inf;
        phi[s] = 0;

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < m; i++) {
                if (phi[a[i].y] > phi[a[i].x] + a[i].cost && a[i].c > 0) {
                    phi[a[i].y] = phi[a[i].x] + a[i].cost;
                }
            }
        }
    }

    int minCostMaxFlow(int s, int t) {
        int flow, cost;
        flow = cost = 0;

        fordBellman(s);
        while (true) {
            if (!dijkstra(s, t))
                break;
            for (int i = 0; i < n; i++)
                phi[i] += d[i];
            int v = t, mx = inf, u, k;
            for (; v != s; v = u) {
                k = from[v];
                u = a[k].x;
                mx = Math.min(mx, a[k].c - a[k].f);
            }

            for (v = t; v != s; v = u) {
                k = from[v];
                u = a[k].x;
                cost += a[k].cost * mx;
                a[k].f += mx;
                a[k ^ 1].f -= mx;
            }
            flow += mx;
        }
        return cost;
    }

    public int readTasks(InputStream input) {
        for (int i = 0; i < N; i++) {
            this.g[i] = new ArrayList<Integer>();
        }

        Scanner in = new Scanner(input);
        int nn = in.nextInt();
        this.k = in.nextInt();
        this.n = nn * 2 + 2;

        for (int i = 0; i < nn; i++) {
            this.task[i] = new Task();
            this.task[i].s = in.nextInt();
            this.task[i].t = in.nextInt();
            this.task[i].c = in.nextInt();
            this.times[i * 2] = this.task[i].s;
            this.times[i * 2 + 1] = this.task[i].s + this.task[i].t;
        }

        ArrayList al = new ArrayList();
        for (int i = 0; i < this.times.length; i++) {
            al.add(this.times[i]);
        }

        HashSet hs = new HashSet();
        hs.addAll(al);
        al.clear();
        al.addAll(hs);

        this.n = al.size() - 1;

        for (int j = 0; j < this.n; j++) {
            this.times[j] = (Integer) al.get(j + 1);
        }

        Arrays.sort(this.times, 0, this.n);

        int s = this.n + 1, t = this.n;
        for (int i = 0; i < this.n; i++)
            this.addEdge(i, i + 1, 0, this.k);
        this.addEdge(s, 0, 0, this.k);
        return nn;
    }

    public void findOptimum(int nn) {
        int s = this.n + 1, t = this.n;
        for (int i = 0; i < nn; i++) {
            int f = 0;
            int q = 0;
            for (int j = 0; j < this.n; j++) {
                if (this.times[j] >= this.task[i].s) {
                    f = j;
                    break;
                }
            }
            for (int j = 0; j < this.n; j++) {
                if (this.times[j] >= (this.task[i].s + this.task[i].t)) {
                    q = j;
                    break;
                }
            }
            this.addEdge(f, q, -this.task[i].c, 1);
        }
        this.n += 2;
        this.minCostMaxFlow(s, t);
    }

    public void printAnswer() {
        for (int i = 0; i < this.m; i += 2)
            if (this.a[i].cost < 0) {
                System.out.print((this.a[i].f > 0 ? 1 : 0) + " ");
            }
    }

    public static void main(String[] args) {
        AutoProgramming ap = new AutoProgramming();
        int taskCount = ap.readTasks(System.in);
        ap.findOptimum(taskCount);
        ap.printAnswer();
    }
}