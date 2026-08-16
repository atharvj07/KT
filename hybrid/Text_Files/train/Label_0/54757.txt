import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int n,m,s,g;
	static boolean[][][] visited;   //node,pref,v
	static double[][][] cost;       //node,pref,v
	static int[][] D,C;
	static int[] dspeed = {-1, 0, 1};
	static final int INF = (1 << 21);

	public static void main(String[] args) {
		while(read()) {
			solve();
		}
	}

	static boolean read() {
		n = sc.nextInt(); m = sc.nextInt();
		if(n == 0 && m == 0) return false;
		s = sc.nextInt(); g = sc.nextInt();
		D = new int[n+1][n+1]; C = new int[n+1][n+1];
		for(int v = 0; v < n+1; v++) {
			Arrays.fill(D[v], INF);
			Arrays.fill(C[v], INF);
		}
		for(int i = 0; i < m; i++) {
			int x = sc.nextInt(), y = sc.nextInt(), d = sc.nextInt(), c = sc.nextInt();
			D[y][x] = D[x][y] = d;
			C[y][x] = C[x][y] = c;
		}
		return true;
	}

	static void solve() {
		cost = new double[n+1][n+1][30+1];
		for(int i = 0; i < n+1; i++) for(int j = 0; j < n+1; j++) Arrays.fill(cost[i][j], INF);
		PriorityQueue<IState> que = new PriorityQueue<IState>();
		for(int v = 1; v <= n; v++) {
			if(D[s][v] == INF) continue;
			cost[v][s][1] = D[s][v] / 1.0;
			IState st = new Main().new IState(v,s,1, D[s][v] / 1.0);
			que.add(st);
		}
		while(!que.isEmpty()) {
			IState u = que.poll();
			if(u.node == g && u.speed == 1) {
				System.out.printf("%.5f\n", cost[u.node][u.pref][u.speed]);
				return;
			}
 			for(int v = 1; v <= n; v++) {
				if(D[u.node][v] == INF) continue;
				for(int k = 0; k < 3; k++) {
					int nspeed = u.speed + dspeed[k];
					if(nspeed > C[u.node][v] || v == u.pref) continue;
					double new_cost = cost[u.node][u.pref][u.speed] + D[u.node][v] / (double)nspeed;
					if(new_cost < cost[v][u.node][nspeed]) {
						cost[v][u.node][nspeed] = new_cost;
						IState st = new Main().new IState(v, u.node, nspeed, new_cost);
						que.add(st);
					}
				}
			}
		}
		System.out.println("unreachable");
	}

	public class IState implements Comparable<IState>{
		int node,pref,speed;
		double cost;
		IState(int node, int pref, int speed, double cost) {
			this.node = node; this.pref = pref; this.speed = speed; this.cost = cost;
		}
		public int compareTo(IState s) {
			if(this.cost < s.cost) {
				return -1;
			} else if(this.cost > s.cost) {
				return 1;
			} else {
				return 0;
			}
		}

		public String toString() {
			return "" + node + " " + pref + " " + speed + " " + cost;
		}
	}

}