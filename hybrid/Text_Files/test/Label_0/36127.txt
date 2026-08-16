import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Black Force
public class Main{

	int h, w, c, val;
	int[][] a, d = {{-1,0},{0,1},{1,0},{0,-1}};
	boolean res, valid;
	boolean[][] v, b;

	void f(int L){
		v = new boolean[h][w];
		for(int i=1;i<h-1;i++)for(int j=1;j<w-1;j++){
			if(!v[i][j]&&a[i][j]<L){
				valid = true;
				val = 0;
				dfs(i, j, L);
				if(valid&&c<=val){
					res = true; return;
				}
			}
		}
	}

	void dfs(int i, int j, int L){
		if(v[i][j]||L<=a[i][j])return;
		v[i][j] = true;
		val += L-a[i][j];
		if(b[i][j]||i==0||i==h-1||j==0||j==w-1)valid = false;
		for(int k=0;k<4;k++){
			int ni = i+d[k][0], nj = j+d[k][1];
			if(0<=ni&&ni<h&&0<=nj&&nj<w)dfs(ni, nj, L);
		}
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			h = sc.nextInt(); w = sc.nextInt(); c = sc.nextInt();
			int r = sc.nextInt();
			if((h|w|c|r)==0)break;
			a = new int[h][w];
			Set<Integer> set = new HashSet<Integer>();
			for(int i=0;i<h;i++)for(int j=0;j<w;j++){
				int x = sc.nextInt();
				a[i][j] = x;
				set.add(x);
			}
			b = new boolean[h][w];
			while(r--!=0){
				b[sc.nextInt()-1][sc.nextInt()-1] = true;
			}
			res = false;
			for(int x:set){
				if(res)break;
				f(x);
			}
			for(int i=0;i<h;i++)for(int j=0;j<w;j++){
				if(res)break;
				if(b[i][j])continue;
				a[i][j]++;
				f(a[i][j]);
				a[i][j]--;
			}
			System.out.println(res?"Yes":"No");
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}