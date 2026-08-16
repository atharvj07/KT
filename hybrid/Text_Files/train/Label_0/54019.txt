import java.util.*;
import java.lang.*;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long X = sc.nextLong();
		long[] five = new long[1001];
		long A = 0;
		for( int i=1; i<=1000; i++ ){
			A++;
			five[i] = A*A*A*A*A;
		}
		loop:for( int i=0; i<=1000; i++ ){
			for( int k=0; k<=1000; k++ ){
				if( five[i]-five[k]==X ){
					System.out.println(i+" "+k);
					break loop;
				}
				if( five[i]+five[k]==X ){
					System.out.println(i+" "+(-k));
					break loop;
				}			
			}
		}
	}
}