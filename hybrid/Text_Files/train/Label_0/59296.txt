import java.util.*;
import java.io.*;
import static java.lang.Math.*;

class Main {

    public static void main( final String[] args ) {

	final Scanner stdin = new Scanner( System.in );

	while ( stdin.hasNextInt() ) {
	    final int c1 = stdin.nextInt();
	    final int c2 = stdin.nextInt();
	    final int c3 = stdin.nextInt();

	    boolean[] selected = new boolean[11];
	    selected[c1] = true;
	    selected[c2] = true;
	    selected[c3] = true;

	    int count = 0;
	    for ( int i = 1; i <= 10; i++ ) {
		if ( !selected[i] && i <= 20 - c1 - c2 ) {
		    count++;
		}
	    }
	    if ( count >= 4 ) {
		System.out.println( "YES" );
	    } else {
		System.out.println( "NO" );
	    }
	}	
    }    
}