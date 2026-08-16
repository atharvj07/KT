import java.util.*;


public class Main{
	public static void main( String args[] ) {

		int counter  = 0;
		int n;
		int h;
		int w;
		
		
		Scanner scan = new Scanner( System.in );
		n = scan.nextInt();
		h = scan.nextInt();
		w = scan.nextInt();
		
		counter = 0;
		
		int temp1,temp2;
		
		if( h > w ) {
			temp1 = h;
			temp2 = w;
		}
		else {
		
			temp1 = w;
			temp2 = h;
 		}
		
		counter = ( n - temp1 + 1 ) * ( n - temp2 + 1 );
		
		
		
		System.out.println( counter );
		
		scan.close();
		
	}
}