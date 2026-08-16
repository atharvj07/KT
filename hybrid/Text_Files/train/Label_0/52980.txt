import java.util.*;
import java.io.*;
import static java.lang.Math.*;

class Main {

    public static void main( final String[] args ) {

	final Scanner stdin = new Scanner( System.in );

	while ( stdin.hasNextInt() ) {

	    final int n = stdin.nextInt();
	    int[] array = new int[ n ];
	    for ( int i = 0; i < n; i++ ){
		array[ i ] = stdin.nextInt();
	    }
	    Arrays.sort( array );
	    int sum = 0;
	    int cum = 0;
	    for ( int i = 0; i < n; i++ ) {
		cum += array[ i ];
		sum += cum;
	    }
	    System.out.println( sum );
	}	
    }    
}