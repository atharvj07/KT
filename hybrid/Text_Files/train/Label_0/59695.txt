import java.io.*;
import java.util.*;

public class Main {
  
  public static void main(String[] args) throws IOException {
    int n = nextInt();
    int m = nextInt();
    int [][]a = new int[n][m];
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        a[i][j] = nextInt();
      }
    }
    int biggestLength = 0;
    for (int i = 0; i < n; ++i) {
      int len = 0;
      for (int j = 0; j < m; ++j) {
        if (a[i][j] == 0) {
          len = 0;
        } else {
          if (++len > biggestLength) {
            biggestLength = len;
          }
        } 
      }
    }
    for (int j = 0; j < m; ++j) {  
      int len = 0;
      for (int i = 0; i < n; ++i) {
        if (a[i][j] == 0) {
          len = 0;
        } else {
          if (++len > biggestLength) {
            biggestLength = len;
          }
        }
      }
    }
    int maxK = biggestLength - 1;
    boolean isFirst = true;
    for (int k = 2; k <= maxK; ++k) {
      if (maxK % k == 0 && check(a, k)) {
        if (!isFirst) {
          System.out.print(" ");
        }
        isFirst = false;
        System.out.print(k);         
      }
    }
    if (isFirst) {
      System.out.print(-1);
    }
    System.out.println();
  }

  private static boolean check(int[][] a, int k) {
    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < a[i].length; ++j) {
        if (a[i][j] == 1) {
          boolean [][]used = new boolean[a.length][a[i].length];
          int oddCnt = eulerDfs(i, j, k, a, used);
          if (oddCnt == 0 || oddCnt == 2) {
            for (int ii = 0; ii < a.length; ++ii) {
              for (int jj = 0; jj < a[ii].length; ++jj) {
                if (a[ii][jj] == 1 && !used[ii][jj]) {
                  return false;
                }
              }
            }
            return true;
          }
          return false;
        }
      }
    }
    return false;
  }

  private static int eulerDfs(int i, int j, int k, int[][] a, boolean[][] used) {
    used[i][j] = true;
    int degree = 0;
    int res = 0;
    for (int di = -1; di <= 1; ++di) {
      for (int dj = -1; dj <= 1; ++dj) {
        if ((di != 0) != (dj != 0)) {
          int ni = i + di * k;
          int nj = j + dj * k;
          if (0 <= ni && ni < a.length && 0 <= nj && nj < a[i].length) {
            int cnt = 0;
            for (int t = 1; t <= k; ++t) {
              cnt += a[i + t * di][j + t * dj];
            }
            if (cnt == k) {
              ++degree;
              for (int t = 1; t < k; ++t) {
                used[i + t * di][j + t * dj] = true;
              }
              if (!used[ni][nj]) {
                res += eulerDfs(ni, nj, k, a, used);
              }
            }
          }
        }
      }
    }
    if (degree % 2 == 1) {
      ++res;
    }
    return res;
  }

  static BufferedReader bufReader = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer stringTokenizer;

  static String nextString() throws IOException {
    while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
      String line = bufReader.readLine();
      if (line == null) {
        return null;
      }
      stringTokenizer = new StringTokenizer(line);
    }
    return stringTokenizer.nextToken();
  }

  static int nextInt() throws IOException {
    return Integer.parseInt(nextString());
  }

  static long nextLong() throws IOException {
    return Long.parseLong(nextString());
  }

  static double nextDouble() throws IOException {
    return Double.parseDouble(nextString());
  }
}
