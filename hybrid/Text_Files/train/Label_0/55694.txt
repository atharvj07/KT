import java.util.*;
import java.io.*;
import java.lang.*;
import java.math.*;
public class F {
    public static int r;
    public static int m;
    public static int[][] b;
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        // int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // int[] a = new int[n]; for(int i=0; i<n; i++) a[i] = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        int ans = 0;
        int[][] a = new int[n][2];
        for(int i=0; i<n; i++) {
          st = new StringTokenizer(bf.readLine());
          a[i][0] =  Integer.parseInt(st.nextToken());
          a[i][1] =  Integer.parseInt(st.nextToken());
        }
        for(int i=0; i<n; i++) {
          for(int j=0; j<n; j++) {
            if(a[j][1] >= 0) {
              if(a[j][0] <= r) {
                ans += 1;
                r += a[j][1];
                a[j][0] = -1;
                a[j][1] = -1;
              }
            }
          }
        }
        m = 0;
        for(int i=0; i<n; i++) {
          if((a[i][1] < 0) && (a[i][0] != -1)) m++;
        }
        b = new int[m][2]; int c = 0;
        for(int i=0; i<n; i++) {
          if((a[i][1] < 0) && (a[i][0] != -1)) {
            b[c][0] = a[i][0] + a[i][1];
            b[c][1] = a[i][1];
            c++;
          }
        }
        Arrays.sort(b, new Comparator<int[]>() {
          @Override
          public int compare(int[] o1, int[] o2) {
            return Integer.compare(o1[0], o2[0]);
          }
        });

        int low = 0;
        int high = m;
        while(low < high) {
          int mid = (low+high+1)/2;
          if(test(mid)) low=mid;
          else high=mid-1;
        }
        out.println((low+ans));
        //if((low+ans)==n) out.println("YES");
      //  else out.println("NO");

        out.close(); System.exit(0);
    }
    public static boolean test(int sz) {
      int low = 0;
      int high = 60000;
      for(int i=0; i<30001; i++) {
        int mid = i;
        int result = extra(mid, sz);
        if(result == -1) low = mid+1;
        else if(result == 1) high = mid-1;
        else return true;
      }
      return false;

    }
    public static int extra(int amt, int sz) {
      int cur = amt;
      int num = 0;
      if(sz==0) {
        if(amt > r) return 0;
        else return 0;
      }
      int idx = 0;
      Map<Integer, Integer> vals = new HashMap<Integer, Integer>();
      TreeSet<Integer> st = new TreeSet<Integer>();
      while(true) {
        while((idx < m) && (b[idx][0] <= cur)) {
          if(!vals.containsKey(-1*b[idx][1])) vals.put(-1*b[idx][1], 0);
          vals.put(-1*b[idx][1], vals.get(-1*b[idx][1]) + 1);
          st.add(-1*b[idx][1]);
          idx++;
        }
        if(st.size() > 0) {
          int p = st.first();
          vals.put(p, vals.get(p)-1);
          if(vals.get(p)==0) st.remove(p);
          cur += p;
          num++;
          if(num == sz) {
            if(cur > r) return 1;
            else return 0;
          }
        }
        else break;
      }
      return -1;
    }
}
class Pair implements Comparable<Pair> {
  public int a;
  public int b;
  public Pair(int a, int b) {
    this.a = a;
    this.b = b;
  }
  @Override
  public boolean equals(Object o) {
    Pair p = (Pair)o;
    return (this.compareTo(p) == 0);
  }

  @Override
  public int hashCode() {
    return (int)((1L*a*103948902382L+b) % 1000000007);
  }

  @Override
  public int compareTo(Pair p) {
    if(this.b < p.b) return -1;
    if(this.b > p.b) return 1;
    if(this.a < p.a) return -1;
    if(this.a > p.a) return 1;
    return 0;
  }
}
