import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt(), m = s.nextInt();
    int[] f = new int[n], count = new int[n], min = new int[n];
    Vertex[] vs = new Vertex[n];
    for (int i = 0; i < n; i++) {
      f[i] = i;
      min[i] = i;
      count[i] = 1;
      vs[i] = new Vertex();
    }
    int[] a = new int[m], b = new int[m];
    for (int i = 0; i < m; i++) {
      a[i] = s.nextInt() - 1; 
      b[i] = s.nextInt() - 1;
      vs[a[i]].next.add(vs[b[i]]);
      vs[b[i]].d++;
    }
    for (int i = 0; i < m; i++) {
      union(f, count, a[i], b[i], vs);
    }
    int ans = 0;
    Vertex[] us = new Vertex[n];
    for (int i = 0; i < n; i++) {
      us[i] = new Vertex();
    }
    for (int i = 0; i < n; i++) {
      if (vs[i].d == 0) {
        us[getFather(f, i)].next.add(vs[i]);
      }
    }
    for (int i = 0; i < n; i++) {
      if (count[i] != 0) {
        ans += count[i];
        List<Vertex> q = us[i].next;
        int k = 0;
        while (k < q.size()) {
          Vertex u = q.get(k++);
          for (Vertex v : u.next) {
            v.d--;
            if (v.d == 0) {
              q.add(v);
            }
          }
        }
        if (count[i] == q.size()) {
          ans--;
        }
      }
    }
    System.out.println(ans);
  }

  public static class Vertex {
    public int d;
    public List<Vertex> next;
    public Vertex() {
      next = new ArrayList<Vertex>();
      d = 0;
    }
  }

  public static int getFather(int[] f, int u) {
    if (f[u] == u) {
      return u;
    } else {
      int v = getFather(f, f[u]);
      f[u] = v;
      return v;
    }
  }

  public static void union(int[] f, int[] count, int a, int b, Vertex[] vs) {
    int fa = getFather(f, a), fb = getFather(f, b);
    if (fa != fb) {
      if (count[fa] < count[fb]) {
        f[fa] = fb;
        count[fb] += count[fa]; 
        count[fa] = 0;
      } else {
        f[fb] = fa;
        count[fa] += count[fb];
        count[fb] = 0;
      } 
    }
  }
}