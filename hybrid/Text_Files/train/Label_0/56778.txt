import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

  static final int N = 100000;
  static final int K = 50000;
  static int n, k;
  static int w[], t[];

  public static boolean check_load(int limit) {
    int i, j;

    for (i=0; i<n; i++)
      if (limit < w[i]) return false;

    Arrays.fill(t, 0);
    i = j = 0;
    while (i<n && j<k) {
      if (t[j] + w[i] < limit) 
        t[j] += w[i++];
      else if (t[j] + w[i] == limit)
        t[j++] += w[i++];
      else
        j++;
    }

    return (i==n) ? true : false;
  }

  public static void main(String[] args) {
    int i;
    Scanner sc = new Scanner(System.in); 
    n = Integer.parseInt(sc.next());
    w = new int[n];
    k = Integer.parseInt(sc.next());
    t = new int[k];
    for (i=0; i<n; i++)
      w[i] = Integer.parseInt(sc.next());

    int l = 0, u = 0;
    for (i=0; i<n; i++) u += w[i];
    while (u-l > 1) {
      int m = (l+u)/2;
      if (check_load(m))
        u = m;
      else
        l = m;
    }
    System.out.println(u);
  }
}