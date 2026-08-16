public class
Main
{
  public void
  run (
    final java.util.Scanner sc,
    final java.io.PrintStream out
    )
  {
    int[ ][ ] a;
    int N;
    int i, j, k, l;
    int res;

    N = sc.nextInt ( );
    a = new int[ N ][ N + 1 ];
    for ( i = 0; i < N; ++i )
    for ( j = 1; j <= N ; ++j )
      a[ i ][ j ] = sc.nextInt ( );

    for ( i = 0; i < N; ++i )
    for ( j = 1; j <= N; ++j )
      a[ i ][ j ] += a[ i ][ j - 1 ];

    res = a[ 0 ][ 1 ];
    for ( i = 0; i < N; ++i )
    for ( j = i + 1; j <= N; ++j )
    {
      for ( k = 0; k < N; ++k )
      {
        int t = 0;

        for ( l = k; l < N; ++l )
        {
          t += a[ l ][ j ] - a[ l ][ i ];
          res = Math.max ( res, t );
        }
      }
    }

    out.println ( res );
  }

  public static void
  main (
    String[ ] args
    )
  {
    ( new Main ( ) ).run ( new java.util.Scanner ( System.in ), System.out );
  }
}