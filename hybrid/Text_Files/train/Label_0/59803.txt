import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Deven-Eleven
public class Main{

	static int[][] move = {{0,-1},{1,-1},{-1,0},{1,0},{0,1},{1,1}};
	static int[][] move2 = {{-1,-1},{0,-1},{-1,0},{1,0},{-1,1},{0,1}};
	static int m, n, s;
	
	static int[][] bfs(int x, int y){
		int[][] r = new int[m+1][n+1];
		boolean[][] v = new boolean[m+1][n+1];
		int step = 1;
		List<int[]> l = new ArrayList<int[]>();
		v[x][y] = true;
		l.add(new int[]{x, y});
		while(!l.isEmpty()){
			List<int[]> next = new ArrayList<int[]>();
			for(int[]a:l){
				for(int k=0;k<6;k++){
					int nx = a[0]+(a[1]%2==0?move[k][0]:move2[k][0]);
					int ny = a[1]+(a[1]%2==0?move[k][1]:move2[k][1]);
					if(1<=nx&&nx<=m&&1<=ny&&ny<=n&&!v[nx][ny]){
						v[nx][ny] = true;
						r[nx][ny] = step;
						next.add(new int[]{nx, ny});
					}
				}
			}
			step++;
			l = next;
		}
		return r;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			m = sc.nextInt();
			if(m==0)break;
			n = sc.nextInt();
			s = sc.nextInt();
			int[][][] a = new int[s][m+1][n+1];
			for(int i=0;i<s;i++)a[i]=bfs(sc.nextInt(), sc.nextInt());
			int max = 0;
			int t = sc.nextInt();
			while(t--!=0){
				int[][] r = bfs(sc.nextInt(), sc.nextInt());
				int c = 0;
				for(int x=1;x<=m;x++){
					for(int y=1;y<=n;y++){
						boolean f = true;
						for(int k=0;k<s;k++){
							if(r[x][y]>=a[k][x][y])f=false;
						}
						if(f)c++;
					}
				}
				max = Math.max(max, c);
			}
			System.out.println(max);
		}
	}
}