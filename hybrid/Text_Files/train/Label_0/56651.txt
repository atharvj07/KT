import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;
public class Main {
	public static final int[] vx = {1,0,-1,0};
	public static final int[] vy = {0,-1,0,1};
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int w = sc.nextInt();
		int h = sc.nextInt();
		char[][] s = new char[w][h];
		for (int y=0;y<h;y++) {
			String line = sc.next();
			for (int x=0;x<w;x++) {
				s[x][y] = line.charAt(x);
			}
		}
		int n = sc.nextInt();
		Pos2d[] open = new Pos2d[n];
		for(int i=0;i<n;i++) {
			open[i] = new Pos2d(sc.nextInt(),sc.nextInt());
		}

		int ans = -1;
		boolean[][] reach = new boolean[w][h];//壁にめり込むところまでtrue
		reach[0][0] = true;
		if (s[0][0]=='t') {
			ans = 0;
		}
		Queue<Pos2d> q = new ArrayDeque<Pos2d>();
		q.offer(new Pos2d(0,0));
		for(int time=0;time<=n;time++) {
			if (time!=0) {
				s[open[time-1].x][open[time-1].y] = '.';
				if (reach[open[time-1].x][open[time-1].y]) {
					q.offer(open[time-1]);
				}else{
					continue;
				}
			}
			while(!q.isEmpty()) {
				Pos2d p = q.poll();
				for(int i=0;i<4;i++) {
					int nx = p.x + vx[i];
					int ny = p.y + vy[i];
					if (nx>= 0 && nx<w && ny>=0 && ny<h) {
						if (!reach[nx][ny]) {
							reach[nx][ny] = true;
							if (s[nx][ny]=='t') {
								ans = time;
							}else if (s[nx][ny]!='#') {
								q.offer(new Pos2d(nx,ny));
							}
						}
					}
				}
			}
			if (ans!=-1) {
				break;
			}
		}
		System.out.println(ans);
		sc.close();
	}
}
class Pos2d {
	public int x;
	public int y;
	public Pos2d(int x,int y) {
		this.x = x;
		this.y = y;
	}
}