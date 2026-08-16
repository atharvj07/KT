import java.util.*;

public class Main {
  // inner classes

  static class Icicle implements Comparable<Icicle> {
    int t, i;

    Icicle(int t, int i) {
      this.t = t;
      this.i = i;
    }

    public int compareTo(Icicle ic) {
      return this.t - ic.t;
    }
  }

  // main
  public static final void main(String[] args) throws Exception {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int l = sc.nextInt();

    int[] tis = new int[n];
    for (int i = 0; i < n; i++)
      tis[i] = sc.nextInt();

    PriorityQueue<Icicle> q = new PriorityQueue<Icicle>();
    boolean[] broken = new boolean[n];
    Arrays.fill(broken, false);

    for (int i = 0; i < n; i++)
      if ((i == 0 || tis[i] > tis[i - 1]) &&
          (i == n - 1 || tis[i] > tis[i + 1])) {
        q.add(new Icicle(l - tis[i], i));
        broken[i] = true;
      }

    int time = 0;

    while (! q.isEmpty()) {
      Icicle ic0 = q.poll();
      //System.out.println("t=" + ic0.t + ",i=" + ic0.i);

      time = ic0.t;
      tis[ic0.i] = 0;

      if (ic0.i > 0) {
        int i1 = ic0.i - 1;
        if (! broken[i1] &&
            (i1 == 0 || tis[i1] > tis[i1 - 1])) {
          q.add(new Icicle(time + l - tis[i1], i1));
          broken[i1] = true;
        }
      }

      if (ic0.i < n - 1) {
        int i2 = ic0.i + 1;
        if (! broken[i2] &&
            (i2 == n - 1 || tis[i2] > tis[i2 + 1])) {
          q.add(new Icicle(time + l - tis[i2], i2));
          broken[i2] = true;
        }
      }
    }

    System.out.println(time);
  }
}