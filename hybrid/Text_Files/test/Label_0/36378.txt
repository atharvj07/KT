import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

//Time Trial
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
		int[][][] assign = new int[50][50][50];
		int[][] ref = new int[19600][3];
		int ID = 0;
		for(int i=0;i<50;i++)for(int j=i+1;j<50;j++)for(int k=j+1;k<50;k++){
			ref[ID][0] = i; ref[ID][1] = j; ref[ID][2] = k;
			assign[i][j][k]=ID++;
		}
		boolean[][] u = new boolean[19600][50];
		for(;;){
			int w = sc.nextInt(), h = sc.nextInt();
			if((w|h)==0)break;
			char[][] map = new char[h][];
			int[][] id = new int[h][w], rid = new int[50][2];
			int[] tile = new int[3], rock = new int[3];
			int kt = 0, kr = 0, start = 0, M = 0;
			for(int i=0;i<h;i++){
				map[i] = sc.next().toCharArray();
				for(int j=0;j<w;j++){
					if(map[i][j]=='@'){
						id[i][j] = M;
						rid[M][0] = i; rid[M][1] = j;
						start = M++;
					}
					else if(map[i][j]=='_'){
						id[i][j] = M;
						rid[M][0] = i; rid[M][1] = j;
						tile[kt++] = M++;
					}
					else if(map[i][j]=='*'){
						id[i][j] = M;
						rid[M][0] = i; rid[M][1] = j;
						rock[kr++] = M++;
					}
					else if(map[i][j]=='.'){
						rid[M][0] = i; rid[M][1] = j;
						id[i][j] = M++;
					}
					else id[i][j] = -1;
				}
			}
			int G = assign[tile[0]][tile[1]][tile[2]], S = assign[rock[0]][rock[1]][rock[2]];
			for(boolean[]a:u)Arrays.fill(a, false);
			u[S][start] = true;
			List<int[]> l = new ArrayList<int[]>();
			l.add(new int[]{S, start});
			int step = 0, res = -1;
			while(!l.isEmpty()){
				List<int[]> next = new ArrayList<int[]>();
				for(int[] a:l){
					if(G==a[0]){
						res = step; next.clear(); break;
					}
					int[] r = ref[a[0]], nr = new int[3];
					int pi = rid[a[1]][0], pj = rid[a[1]][1];
					for(int k=0;k<4;k++){
						int ni = pi+d[k][0], nj = pj+d[k][1], npos = id[ni][nj];
						if(npos==-1)continue;
						nr[0] = r[0]; nr[1] = r[1]; nr[2] = r[2];
						int mpos = id[ni+d[k][0]][nj+d[k][1]];
						if(r[0]==npos){
							if(mpos==-1||r[1]==mpos||r[2]==mpos)continue;
							nr[0] = mpos;
						}
						else if(r[1]==npos){
							if(mpos==-1||r[0]==mpos||r[2]==mpos)continue;
							nr[1] = mpos;
						}
						else if(r[2]==npos){
							if(mpos==-1||r[0]==mpos||r[1]==mpos)continue;
							nr[2] = mpos;
						}
						Arrays.sort(nr);
						int ns = assign[nr[0]][nr[1]][nr[2]];
						if(!u[ns][npos]){
							u[ns][npos] = true; next.add(new int[]{ns, npos});
						}
					}
				}
				step++;
				l = next;
			}
			System.out.println(res);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}