import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Stream;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    // TODO あとでマイナス１する処理をつける
    int[] a = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    br.close();

    int[][] dp = new int[n + 1][n + 1];
    for (int[] sub : dp) {
      Arrays.fill(sub, -1);
    }
    int[] colMax = new int[n + 1];
    Arrays.fill(colMax, -1);

    int base = 0;
    int dpMax = 0;
    dp[Math.min(a[0], a[1])][Math.max(a[0], a[1])] = 0;
    colMax[a[0]] = 0;
    colMax[a[1]] = 0;

    ArrayList<Query> queryList = new ArrayList<>();

    for (int loop = 1; loop < n; loop++) {
      int start = (loop * 3) - 1;
      if (a[start] == a[start + 1] && a[start] == a[start + 2]) {
        base++;
        continue;
      }
      queryList.clear();
      //揃える場合の遷移
      for (int temp = 0; temp < 3; temp++) {
        int x = a[start + (temp % 3)];
        int y = a[start + ((temp + 1) % 3)];
        int z = a[start + ((temp + 2) % 3)];
        //追加される3枚にペアがある場合
        if (x == y) {
          for (int i = 1; i <= n; i++) {
            if (dp[Math.min(i, x)][Math.max(i, x)] >= 0) {
              queryList.add(new Query(Math.min(i, z), Math.max(i, z),
                  dp[Math.min(i, x)][Math.max(i, x)] + 1));
            }
          }
        } else {
          //xを採用
          if (dp[x][x] >= 0) {
            queryList.add(new Query(Math.min(y, z), Math.max(y, z), dp[x][x] + 1));
          }
        }
      }

      for (int temp = 0; temp < 3; temp++) {
        int x = a[start + (temp % 3)];
        int y = a[start + ((temp + 1) % 3)];
        //int z = a[start + ((temp + 2) % 3)];
        //揃えない場合
        //xのみ採用
        for (int i = 1; i <= n; i++) {
          if(colMax[i] >= 0){
            queryList.add(new Query(Math.min(i, x), Math.max(i, x), colMax[i]));
          }
        }
        //xyを採用
        queryList.add(new Query(Math.min(x,y), Math.max(x,y), dpMax));
      }

      for (Query q : queryList) {
        dpMax = Math.max(dpMax, q.value);
        colMax[q.a] = Math.max(colMax[q.a], q.value);
        colMax[q.b] = Math.max(colMax[q.b], q.value);
        dp[q.a][q.b] = Math.max(dp[q.a][q.b], q.value);
      }
    }
    System.out.println(Math.max(dp[a[a.length - 1]][a[a.length - 1]] + 1, dpMax) + base);
  }
}

class Query {

  int a, b, value;

  Query(int a, int b, int value) {
    this.a = a;
    this.b = b;
    this.value = value;
  }
}