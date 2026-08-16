import java.util.Scanner;

//On or Off
public class Main{

	int h, w, M, INF = 1<<29;
	int[][] cost, on, off, nh, nw, v, dp;
	char[][] map;
	int[][] move = {{-1,0},{0,1},{1,0},{0,-1}};
	boolean[][] u;
	
	boolean dfs(int i, int j, int ti, int tj){
		if(i==ti&&j==tj)return true;
		u[i][j] = true;
		for(int k=0;k<4;k++){
			int ni = i+move[k][0], nj = j+move[k][1];
			if(0<=ni&&ni<h&&0<=nj&&nj<w&&!u[ni][nj]&&map[ni][nj]=='.'){
				if(dfs(ni, nj, ti, tj)){
					nh[i][j] = ni; nw[i][j] = nj; return true;
				}
			}
		}
		nh[i][j] = nw[i][j] = -1;
		return false;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		h = sc.nextInt(); w = sc.nextInt(); M = sc.nextInt();
		cost = new int[h][w];
		on = new int[h][w]; off = new int[h][w];
		nh = new int[h][w]; nw = new int[h][w];
		map = new char[h][w];
		for(int i=0;i<h;i++)map[i]=sc.next().toCharArray();
		v = new int[h][w];
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)v[i][j] = -1;
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)cost[i][j]=sc.nextInt();
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)on[i][j]=sc.nextInt();
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)off[i][j]=sc.nextInt();
		int t = 0, pi = sc.nextInt(), pj = sc.nextInt();
		dp = new int[h][w];
		v[pi][pj] = 0;
		dp[pi][pj] = on[pi][pj];
		while(--M!=0){
			int ti = sc.nextInt(), tj = sc.nextInt();
			u = new boolean[h][w];
			dfs(pi, pj, ti, tj);
			for(;;){
				int ni = nh[pi][pj], nj = nw[pi][pj];
				t++;
				if(v[ni][nj]==-1)dp[ni][nj] = on[ni][nj];
				else{
					dp[ni][nj] = Math.min(dp[ni][nj]+off[ni][nj]+on[ni][nj], dp[ni][nj]+(t-v[ni][nj])*cost[ni][nj]);
				}
				v[ni][nj] = t;
				pi = ni; pj = nj;
				if(pi==ti&&pj==tj)break;
			}
		}
		int res = 0;
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)if(v[i][j]!=-1)res+=dp[i][j]+off[i][j];
		System.out.println(res);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}