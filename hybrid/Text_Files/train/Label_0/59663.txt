import java.io.*;
import java.util.*;

class Main {

    void solve(){

	Scanner sc = new Scanner( System.in );
	int w = sc.nextInt();

	StringBuilder res = new StringBuilder();

	while ( w > 0 ) {
	    
	    switch ( w%3 ) {
	    case 0:
		res.insert(0, '0');
		w /= 3;
		break;
	    case 1:
		res.insert(0, '+');
		w /= 3;
		break;
	    case 2:
		res.insert(0, '-');
		w = w/3 + 1;
		break;
	    }
	}
	
	System.out.println( res.toString() );
    }

    public static void main( String[] a ) { new Main().solve(); }
}

