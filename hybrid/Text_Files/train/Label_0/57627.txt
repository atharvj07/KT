import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

//Grid
public class Main{

	int r, c, si, sj, ti, tj;
	int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
	int[][] dist, mem;
	int MOD = 100000007, INF = 1<<28;
	
	int get(int i, int j){
		if(mem[i][j]!=-1)return mem[i][j];
		int res = 0;
		for(int k=0;k<4;k++){
			int ni = (i+d[k][0]+r)%r, nj = (j+d[k][1]+c)%c;
			if(dist[ni][nj] < dist[i][j])res+=get(ni, nj);
		}
		return mem[i][j] = res%MOD;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		r = sc.nextInt(); c = sc.nextInt(); si = sc.nextInt(); sj = sc.nextInt(); ti = sc.nextInt(); tj = sc.nextInt();
		dist = new int[r][c];
		for(int[]a:dist)Arrays.fill(a, INF);
		Queue<int[]> q = new LinkedList<int[]>();
		dist[si][sj] = 0;
		q.add(new int[]{si, sj});
		while(!q.isEmpty()){
			int[] V = q.poll();
			for(int k=0;k<4;k++){
				int ni = (V[0]+d[k][0]+r)%r, nj = (V[1]+d[k][1]+c)%c;
				if(dist[ni][nj]==INF){
					dist[ni][nj] = dist[V[0]][V[1]]+1;
					q.add(new int[]{ni, nj});
				}
			}
		}
		mem = new int[r][c];
		for(int[]a:mem)Arrays.fill(a, -1);
		mem[si][sj] = 1;
		System.out.println(get(ti, tj));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}