import java.util.Arrays;
import java.util.Scanner;

public class Main {
  Scanner sc;

  int n, m;
  int MAX = 1000;
  int ofs = MAX / 2;
  int[][] dp, cave, pr;
  int LIM = 1000000;

  int[] tx = new int[] { 1, 0, -1, 0 };
  int[] ty = new int[] { 0, -1, 0, 1 };

  void run() {
    while (true) {
      m = ni();
      n = ni();
      if ( n == 0 && m == 0 )
        break;

      dp = new int[MAX + 1][MAX + 1];
      pr = new int[MAX + 1][MAX + 1];
      cave = new int[MAX + 1][MAX + 1];
      int x = 0;
      int y = 0;
      int stx = ofs;
      int sty = ofs;
      int num = 1;
      cave[ ofs ][ ofs ] = 1;
      num++;
      int t = 0;
      while (num <= m) {
        int an = t / 2 + 1;
        for ( int i = 1; i <= an; i++ ) {
          int tmpx = x + tx[ t % 4 ] * i + ofs;
          int tmpy = y + ty[ t % 4 ] * i + ofs;
          cave[ tmpy ][ tmpx ] = num;
          if ( num == n ) {
            stx = tmpx;
            sty = tmpy;
          }

          if ( isPrime( num ) ) {
            pr[ tmpy ][ tmpx ]++;
            // cave[ tmpy ][ tmpx ] *= -1;
          }
          num++;
          if ( num > m ) {
            break;
          }
        }
        x += tx[ t % 4 ] * an;
        y += ty[ t % 4 ] * an;
        t++;
      }

      // for ( int i = 0; i < cave.length; ++i ) {
      // for ( int j = 0; j < cave[ 0 ].length; ++j ) {
      // if ( j > 0 ) {
      // System.out.print( " " );
      // }
      // System.out.print( String.format( "%4d", cave[ i ][ j ] ) );
      // }
      // System.out.println();
      // }
      int maxc = 0;
      int maxn = 0;
      dp[ sty ][ stx ] = pr[ sty ][ stx ];
      for ( int i = sty; i < MAX; i++ ) {
        int d = i - sty;
        int start = stx - d;
        start = start < 0 ? 0 : start;

        int end = stx + d;
        end = ( end >= ( MAX + 1 ) ) ? MAX : end;

        for ( int j = start; j <= end; j++ ) {

          // int dp1 = 0;
          // if(j >= 1)dp1 = dp[i-1][j-1];
          // int dp2 = dp[i-1][j];
          // int dp3 = 0;
          // if(j <MAX)dp3 = dp[i-1][j+1];
          // dp[i][j] += Math.max( Math.max(dp1, dp2), dp3 );

          for ( int l = -1; l <= 1; ++l ) {
            if ( j + l < 0 )
              continue;
            if ( j + l > MAX )
              continue;
            dp[ i + 1 ][ j + l ] = Math.max( dp[ i + 1 ][ j + l ], dp[ i ][ j ]
                + pr[ i + 1 ][ j + l ] );
            if ( maxc < dp[ i ][ j ] ) {
              maxc = dp[ i ][ j ];
              maxn = cave[ i ][ j ];
            } else if ( maxc == dp[ i ][ j ] ) {
              if ( maxn < cave[ i ][ j ] && pr[ i ][ j ] == 1 ) {
                maxn = cave[ i ][ j ];
              }
            }
          }
        }
      }
      System.out.printf( "%d %d\n", maxc, maxn );
    }

  }

  boolean isPrime(int n) {
    if ( n == 2 )
      return true;
    if ( n % 2 == 0 )
      return false;
    for ( int i = 3; i * i <= n; i += 2 ) {
      if ( n % i == 0 )
        return false;
    }
    return true;
  }

  Main() {
    sc = new Scanner( System.in );
  }

  int ni() {
    return sc.nextInt();
  }

  public static void main(String[] args) {
    new Main().run();
  }

  void debug(Object... os) {
    System.err.println( Arrays.deepToString( os ) );
  }

}