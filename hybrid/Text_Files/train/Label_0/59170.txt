import	java.util.Scanner;

/**
 * @author fayiz
 * @data 2019/8/28 13:59
 **/
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int s = sc.nextInt();
    int e = sc.nextInt();

    int maxPoss = s / e;

    int a[] = new int[n];
    for(int i = 0; i < n; ++i)
      a[i] = sc.nextInt();
    //记录每个b[i] 出现的次数
    int cnt[] = new int[100001];
    //b[i]数组
    int b[] = new int[m];
    for(int i = 0; i < m; ++i) {
      b[i] = sc.nextInt();
      cnt[b[i]]++;
    }
    //一个二位矩阵记录的是
    int ind[][] = new int[100001][];
    for(int i = 0; i <= 100000; ++i) {
      ind[i] = new int[cnt[i]];
    }

    int ptr[] = new int[100001];
    for(int i = 0; i < m; ++i)
      ind[b[i]][ptr[b[i]]++] = i;

    int dp[][] = new int[n + 1][maxPoss + 1];
    for(int i = 0; i <= n; ++i) {
      for(int j = 0; j <= maxPoss; ++j)
        dp[i][j] = Integer.MAX_VALUE;
    }
    dp[0][0] = -1;

    int ans = 0;
    for(int i = 1; i <= n; ++i) {
      for(int j = 0; j < maxPoss; ++j) {
        if(dp[i - 1][j] == Integer.MAX_VALUE)
          break;

        int cval = a[i - 1];
        int start = 0, end = ind[cval].length - 1, cind = -1;
        int lim = dp[i - 1][j];
        while(start <= end) {
          int mid = (start + end) >> 1;
          if(ind[cval][mid] > lim) {
            cind = mid;
            end = mid - 1;
          }
          else
            start = mid + 1;
        }
        if(cind != -1)
          dp[i][j + 1] = ind[cval][cind];
      }
      for(int j = 0; j <= maxPoss; ++j) {
        if(dp[i - 1][j] == Integer.MAX_VALUE)
          break;
        dp[i][j] = Math.min(dp[i][j], dp[i - 1][j]);
      }

      for(int j = 0; j <= maxPoss; ++j) {
        if(dp[i][j] == Integer.MAX_VALUE)
          break;
        int curCost = e * j + dp[i][j] + 1 + i;
        if(curCost <= s) {
          ans = Math.max(ans, j);
        }
      }
    }
    System.out.println(ans);
  }
}

	  		    	    				  	 	 		 			