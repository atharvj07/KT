import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  Scanner sc;

  void run() {
    for ( ;; ) {
      int n = ni();
      int r = ni();

      if ( ( n | r ) == 0 )
        break;

      ArrayList<Integer> list = new ArrayList<Integer>();
      for ( int i = 0; i < n; ++i ) {
        list.add( n - i );
      }

      for ( int i = 0; i < r; ++i ) {
        int p = ni();
        int c = ni();

        List<Integer> subl = new ArrayList<Integer>( list.subList( p - 1, p + c
            - 1 ) );
        for ( int j = 0; j < c; ++j ) {
          list.remove( p - 1 );
        }
        list.addAll( 0, subl );

        // debug( list );
      }

      System.out.println( list.get( 0 ) );
    }
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