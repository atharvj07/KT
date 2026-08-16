import java.util.Arrays;
import java.util.Scanner;

//Kaeru Jump
public class Main{

	int h, w, n;
	char[][] m;
	int[][] d = {{-1,0},{0,1},{1,0},{0,-1}};
	char[] str = {'U','R','D','L'};
	char[] res;

	int[][] near(int i, int j){
		int[][] r = new int[4][2];
		for(int[]a:r)Arrays.fill(a, -1);
		for(int k=0;k<4;k++){
			int pi = i+d[k][0], pj = j+d[k][1];
			while(0<=pi&&pi<h&&0<=pj&&pj<w){
				if(m[pi][pj]=='o'){
					r[k][0] = pi; r[k][1] = pj; break;
				}
				pi += d[k][0]; pj += d[k][1];
			}
		}
		return r;
	}

	boolean dfs(int i, int j, int D, int c){
		if(c==n-1)return true;
		int[][] e = near(i, j);
		for(int k=0;k<4;k++){
			if(e[k][0]==-1||D==(k+2)%4)continue;
			res[c] = str[k];
			m[i][j] = '.';
//			boolean ok = true;
//			if(c<n-2){
//				for(int dir=0;dir<4;dir++){
//					if(e[dir][0]==-1)continue;
//					int[][] adj = near(e[dir][0], e[dir][1]);
//					boolean exist = false;
//					for(int x=0;x<4;x++)if(adj[x][0]!=-1)exist = true;
//					if(!exist)ok = false;
//				}
//			}
//			if(ok){
				if(dfs(e[k][0], e[k][1], k, c+1))return true;
//			}
			m[i][j] = 'o';
		}
		return false;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		h = sc.nextInt(); w = sc.nextInt();
		n = 0;
		m = new char[h][];
		int si = -1, sj = -1, sd = -1;
		for(int i=0;i<h;i++){
			m[i] = sc.next().toCharArray();
			for(int j=0;j<w;j++){
				if(m[i][j]=='.')continue;
				n++;
				if(m[i][j]=='o')continue;
				si = i; sj = j;
				sd = m[i][j]=='U'?0:m[i][j]=='R'?1:m[i][j]=='D'?2:3;
				m[i][j] = 'o';
			}
		}
		res = new char[n-1];
		dfs(si, sj, sd, 0);
		System.out.println(new String(res));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}