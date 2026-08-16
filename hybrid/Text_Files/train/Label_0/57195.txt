import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws Exception {
		try(Scanner sc = new Scanner(System.in)) {
			int V = sc.nextInt(); // 頂点数
			int E = sc.nextInt(); // 辺数
			int INF = Integer.MAX_VALUE;

			int[][] dis = new int[V][V];
			for(int i=0; i<V; i++) {
				for(int j=0; j<V; j++) {
					if(i == j) dis[i][j] = 0;
					else dis[i][j] = INF;
				}
			}
			for(int i=0; i<E; i++) {
				int s = sc.nextInt();
				int t = sc.nextInt();
				int d = sc.nextInt();
				dis[s][t] = d;
			}
			boolean negative = false;
			for(int k=0; k<V; k++) {
				for(int i=0; i<V; i++) {
					for(int j=0; j<V; j++) {
						if(dis[i][k] < INF && dis[k][j] < INF) {
							dis[i][j] = Math.min(dis[i][j], dis[i][k]+dis[k][j]);
						}
					}
					if(dis[i][i] < 0)	negative = true;
				}
			}
			
			if(negative) {
				System.out.println("NEGATIVE CYCLE");
				return;
			}
			for(int i=0; i<V; i++) {
				for(int j=0; j<V-1; j++) {
					System.out.print((dis[i][j]>=INF? "INF":dis[i][j]) + " ");
				}
				System.out.println(dis[i][V-1]>=INF? "INF":dis[i][V-1]);
			}
			
		}
	}

}





