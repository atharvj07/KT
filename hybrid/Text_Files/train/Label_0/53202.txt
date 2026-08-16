import java.util.*;
import java.io.*;

class Main {

    static long backToOne ( int a, int m ) {
	int no = 1;
	boolean[] visited = new boolean[m];

	long count = 0;
	while ( true ) {
	    visited[no] = true;
	    no = (no * a) % m;
	    count++;
	    if ( visited[no] ) {
		if( no == 1 ) {
		    return count;
		} else {
		    return -1L;
		}
	    }
	}
    }

    static long gcd( long a, long b ) {
	if ( a < b ) {
	    return gcd ( b, a );
	}
	while ( b != 0 ) {
	    final long tmp = a;
	    a = b;
	    b = tmp % a;	    
	}
	return a;
    }

    static long lcm( long a, long b ) {
	return a * b / gcd( a, b );
    }
    
    public static void main(String[] args) {

	final Scanner stdin = new Scanner(System.in);

	while ( true ) {
	    final int a1 = stdin.nextInt();
	    final int m1 = stdin.nextInt();
	    final int a2 = stdin.nextInt();
	    final int m2 = stdin.nextInt();
	    final int a3 = stdin.nextInt();
	    final int m3 = stdin.nextInt();
	    if ( a1 == 0 && a2 == 0 && a3 == 0 && m1 == 0 && m2 == 0 && m3 == 0) {
		break;
	    }
	    long a = backToOne( a1, m1 );
	    long b = backToOne( a2, m2 );
	    long c = backToOne( a3, m3 );
	    System.out.println( lcm( lcm( a, b ), c ) );
	}
	
    }
    
}