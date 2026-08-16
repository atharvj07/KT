
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	int INF = 1 << 28;
	boolean val[];
	String eq;
	int p;
	int MAX = 11;

	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			eq = sc.next();
			if( eq.equals("#") )break;
			val = new boolean[MAX];
			boolean yn = true;
			for(int i=0;i<(1<<MAX);i++) {
				p = 0;
				for(int j=0;j<MAX;j++) val[j] = ((i>>j)&1) == 1;
				if( !equation() ) {
					yn = false;
					break;
				}
			}
			System.out.println( (yn? "YES": "NO") );
			
		}
	}
	
	boolean equation() {
		boolean l = formula();
		p++;
		boolean r = formula();
		debug(l, r);
		return !(l^r);
	}
	
	boolean formula() {
		switch (eq.charAt(p)) {
		case 'T': p++; return true;
		case 'F': p++; return false;
		case '(':
			p++;
			boolean l = formula();
			int tmp = p++;
			if( eq.charAt(p) == '>' ) { p++; tmp++;}
			boolean r = formula();
			p++;
			if( eq.charAt(tmp) == '*' ) return mlt(l, r);
			else if( eq.charAt(tmp) == '+' ) return add(l, r);
			else return inc(l, r);
		case '-': p++; return inv(formula());
		default : p++; return val(eq.charAt(p-1));
		}
	}
	
	boolean val(char x) {
		debug(x);
		return val[x-'a'];
	}
	
	boolean inv(boolean x) {
		return !x;
	}
	
	boolean add(boolean x, boolean y) {
		return x|y;
	}
	
	boolean mlt(boolean x, boolean y) {
		return x&y;
	}
	
	boolean inc(boolean x, boolean y) {
		return inv( mlt( x, inv(y) ) );
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... os) {
		//System.err.println(Arrays.deepToString(os));
	}
}