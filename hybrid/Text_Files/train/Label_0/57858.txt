
import java.util.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	int INF = 1 << 28;
	final int N = 10000001;
	boolean prime[];
	LinkedList<Integer> maxp;
	int[] p4;
	
	void run() {
		Scanner sc = new Scanner(System.in);
		prime = new boolean[N];
		maxp = new LinkedList<Integer>();
		prime();
		for(;;) {
			int val = sc.nextInt();
			if(val == 0) break;
			int l = 0; int r = p4.length-1;
			while(l<=r) {
				int c = (l + r) / 2;
				if( p4[c] < val ) l = c+1;
				else if(p4[c] > val) r = c-1;
				else {
					l = c;
					break;
				}
			}
//			debug(p4);
			if(l>p4.length-1)System.out.println(p4[r]);
			else if(r<0) System.out.println(p4[l]);
			else System.out.println(min(p4[l],p4[r]));
		}
		
	}
	
	void prime() {
		prime[0] = prime[1] = true;
		for(int i=2;i<N;i++) if(!prime[i]){
			if(i-8>=0 && (!prime[i-8] && !prime[i-6] && !prime[i-2])) {
				maxp.add(i);
//				debug(i);
			}
			for(int j=i*2;j<N;j+=i) prime[j] = true;
		}
		p4 = new int[maxp.size()];
		int size = maxp.size();
		for(int i=0;i<size;i++) p4[i] = maxp.removeFirst();
		
	}

	public static void main(String[] args) {
		new Main().run();
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}
}