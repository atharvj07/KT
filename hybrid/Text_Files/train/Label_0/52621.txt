import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Square Carpets
public class Main{

	int w, h, res, L;
	int[][] a, t;
	boolean[][][] ok;
	Map<Integer, Integer> ref;

	void copy(int[][] a, int[][] b){
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)b[i][j]=a[i][j];
	}

	int get(int[][] t){
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)sb.append(t[i][j]);
		return sb.toString().hashCode();
	}

	void dfs(int i, int j, int step){
		if(res<=step)return;
		if(i==h){
			res = step; return;
		}
		if(a[i][j]==0){
			if(j==w-1)dfs(i+1, 0, step);
			else dfs(i, j+1, step);
		}
		if(t[i][j]==1){
			if(j==w-1)dfs(i+1, 0, step);
			else dfs(i, j+1, step);	
		}
		int[][] p = new int[h][w];
		copy(t, p);
		for(int len=L;len>0;len--){
			if(!ok[i][j][len])continue;
			for(int y=i;y<i+len;y++)for(int x=j;x<j+len;x++)t[y][x] = 1;
			int hash = get(t);
			if(ref.containsKey(hash)&&ref.get(hash)<=step){
				copy(p, t); return;
			}
			ref.put(hash, step);
			if(j==w-1)dfs(i+1, 0, step+1);
			else dfs(i, j+1, step+1);
			copy(p, t);
			break;
		}
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			w = sc.nextInt(); h = sc.nextInt();
			if((w|h)==0)break;
			L = Math.min(h, w);
			a = new int[h][w];
			ok = new boolean[h][w][L+1];
			for(int i=0;i<h;i++)for(int j=0;j<w;j++)a[i][j]=sc.nextInt();
			for(int d=1;d<=L;d++)for(int i=0;i+d<=h;i++)for(int j=0;j+d<=w;j++){
				boolean f = true;
				for(int y=i;y<i+d;y++)for(int x=j;x<j+d;x++)if(a[y][x]==0)f = false;
				if(f)ok[i][j][d] = true;
			}
			res = w*h;
			ref = new HashMap<Integer, Integer>();
			t = new int[h][w];
			dfs(0, 0, 0);
			System.out.println(res);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}