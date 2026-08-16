
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	int INF = 1 << 28;
	int p, q, r;
	final int DIV = 1000000;
	double s, t;
	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			p = sc.nextInt();
			q = sc.nextInt();
			r = sc.nextInt();
			if( (p|q|r) == 0 ) break;
			s = p - q;
			t = (double)( q-p ) / q; 
			if( r == 0 ) System.out.println((double)2 * ( p - q ) * PI );
			else {
				double sum = 0;
				int loop = q / lcm(q, p-q);
				double theta = 2 * PI * loop;
				
				for(int i=0;i<DIV;i++) {
					double t1 = theta / DIV * i;
					double t2 = theta / DIV * ( i + 1 );
					P p = hypotroid( (t1+t2) / 2 ) ;
					sum += sqrt(p.x * p.x + p.y * p.y) * (t2-t1);
				}
				System.out.println(sum);
			}
		}
	}
	
	int lcm( int a, int b ) {
		if( b == 0 ) return a;
		else return lcm(b, a%b);
	}
	
	P hypotroid( double theta ) {
		double x = - s * sin(theta) - (double) t * r * sin( theta * t );
		double y = s * cos(theta) + (double) t * r * cos( theta * t );
		return new P(x, y);
	}
	
	class P {
		double x, y;
		P(double x, double y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}
}