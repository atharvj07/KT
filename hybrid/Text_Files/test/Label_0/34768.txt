import java.util.*;
import java.io.*;
import static java.lang.Math.*;

class Main {

    public static void main( final String[] args ) {

	final Scanner stdin = new Scanner( System.in );

	while ( true ) {

	    final int n = stdin.nextInt();
	    if ( n == -1 ) {
		break;
	    }

	    double xn = n / 2.0;
	    while ( abs( xn * xn * xn - n ) >= n * 1.0e-5 ) {
		xn = xn - ( xn * xn * xn - n ) / ( 3 * xn * xn );
	    }
	    System.out.printf( "%.10f\n", xn );
	}	
    }    
}