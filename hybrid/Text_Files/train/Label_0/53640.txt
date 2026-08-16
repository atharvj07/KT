
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int n, w, cnt;
	int[] cnts;
	
	void run() {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt(); w = sc.nextInt();
		cnts = new int[2*n+10];
		cnt = 0;
		
		for(int i=1;i<=w;i++) {
			update(i, 1);
		}
		System.out.print(cnt + (n==w? "\n":" "));
		for(int i=1;i<n-w+1;i++) {
//			debug(i, cnts);
			update(i, -1);
			update(i+w, 1);
			System.out.print(cnt + (i==n-w? "\n": " "));
		}
	}
	
	void update(int x, int c) {
		cnts[1] += c==1? 2: -2;
		if(x!=1) cnts[x] += c==1? 2: -2;
		if( ( cnts[x] == 2 || cnts[x] == 3 ) && c == 1 ) cnt++;
		if( ( cnts[x] == 1 || cnts[x] == 0 ) && c == -1 ) cnt--;
		for(long j=2;j*j<=x;j++) if(x%j==0) {
			cnts[(int)j] += c;
			if( cnts[(int)j] == 2 && c == 1 ) cnt++;
			if( cnts[(int)j] == 1 && c == -1 ) cnt--;
			if( j != x/j ){
				cnts[(int)(x/j)] += c;
				if( cnts[(int)(x/j)] == 2 && c == 1 ) cnt++;
				if( cnts[(int)(x/j)] == 1 && c == -1 ) cnt--;
			}
		}
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}