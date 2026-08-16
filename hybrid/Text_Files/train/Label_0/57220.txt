import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {
	
	void run() {
		Scanner sc = new Scanner(System.in);
		
		int INF = 1<<29;
		
		for(;;) {
			int n = sc.nextInt(), m = sc.nextInt(), c = sc.nextInt();
			if((n|m|c) == 0) break;
			
			Es[] G = new Es[n];
			for(int i=0;i<n;i++) G[i] = new Es();
			for(int i=0;i<m;i++) {
				int f = sc.nextInt()-1, t = sc.nextInt()-1, cost = sc.nextInt();
				G[f].add(new E(f, t, cost));
			}
			
			PriorityQueue<S> que = new PriorityQueue<S>();
			int[][] d = new int[n][n+1];
			for(int[] a: d) fill(a, INF);
			que.add(new S(0, 0, 0)); d[0][0] = 0;
			
			for(;!que.isEmpty();) {
				S cur = que.remove();
//				debug(cur.p, cur.e, cur.c);
				if(d[cur.p][cur.e] != cur.c) continue;
				if(cur.p == n-1 && cur.c < c) {
					System.out.println(cur.e);
					break;
				}
				
				for(E next: G[cur.p]) {
					if(d[next.t][cur.e] > cur.c + next.c) {
						d[next.t][cur.e] = cur.c + next.c;
						que.add(new S(next.t, cur.e, cur.c+next.c));
					}
					if(d[next.t][cur.e+1] > cur.c) {
						d[next.t][cur.e+1] = cur.c;
						que.add(new S(next.t, cur.e+1, cur.c));
					}
				}
			}
		}
	}
	
	class S implements Comparable<S>{
		int p, e, c;
		S(int p, int e, int c) {
			this.p = p;
			this.e = e;
			this.c = c;
		}

		public int compareTo(S o) {
			// TODO Auto-generated method stub
			if(e != o.e) return e - o.e;
			return c-o.c;
			
		}
	}
	
	class Es extends ArrayList<E> {}
	
	class E {
		int f, t, c;
		E(int f, int t, int c) {
			this.f = f;
			this.t = t;
			this.c = c;
		}
	}
	
	void debug(Object...os) {
		System.err.println(deepToString(os));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}