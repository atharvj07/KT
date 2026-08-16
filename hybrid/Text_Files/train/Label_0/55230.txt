import java.util.Scanner;

//Left Hand Rule
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int INF = 1<<29;
		int[][] d = {{0,1},{1,0},{0,-1},{-1,0}};
		for(;;){
			int w = sc.nextInt(), h = sc.nextInt(), n = sc.nextInt();
			if((w|h|n)==0)break;
			boolean[][][] wall = new boolean[w][h][4];
			for(int x=0;x<w;x++)wall[x][0][2] = wall[x][h-1][0] = true;
			for(int y=0;y<h;y++)wall[0][y][3] = wall[w-1][y][1] = true;
			while(n--!=0){
				int x1 = sc.nextInt(), y1 = sc.nextInt(), x2 = sc.nextInt(), y2 = sc.nextInt();
				if(x1==x2){
					for(int y=Math.min(y1, y2);y<Math.max(y1, y2);y++)wall[x1][y][3] = wall[x1-1][y][1] = true;
				}
				else{
					for(int x=Math.min(x1, x2);x<Math.max(x1, x2);x++)wall[x][y1][2] = wall[x][y1-1][0] = true;
				}
			}
			boolean[][][] u = new boolean[w][h][4];
			int px = 0, py = 0, pk = 0, step = 1, res = INF;
			int x1 = sc.nextInt(), y1 = sc.nextInt(), x2 = sc.nextInt(), y2 = sc.nextInt(), gx = sc.nextInt(), gy = sc.nextInt();
			if(x2<x1||(x1==x2&&y2<y1)){
				int tx = x1, ty = y1;
				x1 = x2; y1 = y2; x2 = tx; y2 = ty;
			}
			if(x1==x2){
				if(x1==0){
					wall[x1][y1][3] = false;
					u[x1][y1][1] = true;
					px = x1; py = y1; pk = 1;
				}
				else{
					wall[x1-1][y1][1] = false;
					u[x1-1][y1][3] = true;
					px = x1-1; py = y1; pk = 3;
				}
			}
			else{
				if(y1==0){
					wall[x1][y1][2] = false;
					u[x1][y1][0] = true;
					px = x1; py = y1; pk = 0;
				}
				else{
					wall[x1][y1-1][0] = false;
					u[x1][y1-1][2] = true;
					px = x1; py = y1-1; pk = 2;
				}
			}
			for(boolean f=true;f;step++){
				if(px==gx&&py==gy){
					res = step; break;
				}
				for(int k=3;k<7;k++){
					int nk = (pk+k)%4;
					if(!wall[px][py][nk]){
						px+=d[nk][0]; py+=d[nk][1]; pk=nk;
						if(0<=px&&px<w&&0<=py&&py<h&&!u[px][py][pk]){
							u[px][py][pk] = true;
						}
						else{
							f = false; break;
						}
						break;
					}
				}
			}
			System.out.println(res==INF?"Impossible":res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}