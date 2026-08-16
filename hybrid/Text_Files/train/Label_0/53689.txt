
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int[] a = new int[100000];
	int N, S, W, Q;
	int g, ans, p, prev, v, z, i;
	Scanner sc = new Scanner(System.in);
	void prime() {
		for(long i= 100000000;;i--) {
			boolean flg = false;
			for(long j=2;j*j< i;j++) if(i%j==0) { flg = true; break; }
			if(!flg) {
				debug(i); break;
			}
		}
	}
	void run() {
		for(;;) {
			N = sc.nextInt(); S = sc.nextInt(); W = sc.nextInt(); Q = sc.nextInt();
			if((N|S|Q|W) == 0) break;
			fill(a, 0);
			g = S;
		    for(i=0; i<N; i++) {
		        a[i] = (g/7) % 10;
		        if( g%2 == 0 ) { g = (g/2); }
		        else           { g = (g/2) ^ W; }
		    }
		    
		    if(Q == 2 || Q == 5) {
		    	ans = 0;
		    	z = 0;
		    	for(i=0;i<N;i++) {
		    		if(a[i] == 0) z++;
		    		if(a[i]%Q == 0) ans += i-z+1;
		    	}
		    	System.out.println(ans);
		    	continue;
		    }
		    p = 1; prev = 0; ans = 0;
		    HashMap<Integer, Integer> cnt = new HashMap<Integer, Integer>();
		    cnt.put(0, 1);
		    for(i=0;i<N;i++) {
		    	v = (prev + p * a[N - i-1])%Q;
		    	prev = v;
		    	if(cnt.containsKey(v)) {
		    		if(a[N - i-1] != 0) ans += cnt.get(v);
		    		cnt.put(v, cnt.get(v)+1);
		    	}
		    	else cnt.put(v, 1);
		    	
		    	p = (p*10)%Q;
		    }
		    
		    System.out.println(ans);
		}
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}