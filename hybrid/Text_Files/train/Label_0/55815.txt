import java.util.Scanner;

//Alien Messages
public class Main{

	int w, h, C, si, sj, SD, ED;
	int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
	int[] D = {5, 10, 3, 9, 12, 6};
	int[][] p = {{0,2},{1,3},{0,1},{0,3},{2,3},{1,2}};
	int[][] nx = {{0, 5, 4},{3, 1, 4},{2, 0, 3},{2, 5, 1}};
	int[][] map;
	
	boolean check(int pi, int pj){
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)if(map[i][j]==0){
			int c = 0;
			for(int k=0;k<4;k++){
				int ni = i+d[k][0], nj = j+d[k][1];
				if(0<=ni&&ni<h&&0<=nj&&nj<w&&map[ni][nj]==0)c++;
			}
			if(i==pi&&j==pj)c++;
			if(i==si+d[ED][0]&&j==sj+d[ED][1])c++;
			if(c<2)return false;
		}
		return true;
	}
	
	boolean f(int i, int j, int c, int pd){
		if(!check(i, j))return false;
		if(si+d[ED][0]==i&&sj+d[ED][1]==j&&c<C)return false;
		for(int k=0;k<3;k++){
			map[i][j] = D[nx[pd][k]];
			boolean ok = true;
			int ND = -1;
			for(int x=0;x<2;x++){
				int dir = p[nx[pd][k]][x];
				int ni = i+d[dir][0], nj = j+d[dir][1];
				if(!(0<=ni&&ni<h&&0<=nj&&nj<w&&map[ni][nj]!=-1)){
					ok = false; break;
				}
				if(map[ni][nj]==0){
					ND = dir;
				}
				else {
					int r = (dir+2)%4;
					if(((map[ni][nj]>>r)&1)==0){
						ok = false;
					}
				}
			}
			if(!ok)continue;
			if(ND==-1){
				if(c==C)return true;
			}
			else if(f(i+d[ND][0], j+d[ND][1], c+1, ND))return true;
		}
		map[i][j] = 0;
		return false;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			w = sc.nextInt(); h = sc.nextInt();
			if((w|h)==0)break;
			C = 0;
			map = new int[h][w];
			for(int i=0;i<h;i++)for(int j=0;j<w;j++){
				map[i][j]=sc.nextInt()==0?0:-1;
				C+=map[i][j]==0?1:0;
			}
			boolean res = false, con = true;
			for(int i=0;i<h&&con;i++)for(int j=0;j<w&&con;j++)if(map[i][j]==0){
				con = false;
				for(int k=0;k<6;k++){
					boolean ok = true;
					for(int x=0;x<2;x++){
						int ni = i+d[p[k][x]][0], nj = j+d[p[k][x]][1];
						if(!(0<=ni&&ni<h&&0<=nj&&nj<w&&map[ni][nj]==0)){
							ok = false;
						}
					}
					if(!ok)continue;
					map[i][j] = D[k];
					si = i; sj = j; SD = p[k][0]; ED = p[k][1];
					if(f(i+d[p[k][0]][0], j+d[p[k][0]][1], 2, SD)){
						res = true; break;
					}
				}
			}
			System.out.println(res?"Yes":"No");
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}