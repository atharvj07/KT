import java.util.Arrays;
import java.util.Scanner;

//A Long Ride on a Railway
public class Main{

	int n, m, max;
	int INF = 1<<27;
	int[][] d;
	boolean[] u;
	int[] ans, trace;
	
	void debug(Object...o){
		System.err.println(Arrays.deepToString(o));
	}
	
	long f(int[] a, int n){
		long x = 0;
		for(int i=0;i<n;i++)x = x*10+(a[i]-1);
		return x;
	}
	
	void dfs(int k, int v, int dist){
		if(max==dist){
			trace[k] = v;
			long a = f(trace, k+1);
			long b = f(ans, ans.length);
			if(a<b){
				ans = new int[k+1];
				for(int i=0;i<=k;i++)ans[i]=trace[i];
//				debug(max); debug(ans);
			}
		}
		else if(max<dist){
			trace[k] = v;
			max = dist;
			ans = new int[k+1];
			for(int i=0;i<=k;i++)ans[i]=trace[i];
//			debug(max); debug(ans);
		}
		for(int i=0;i<m;i++){
			if(u[i])continue;
			if(d[i][0]!=v&&d[i][1]!=v)continue;
			trace[k] = v;
			if(d[i][0]==v){
				int t = d[i][1];
				u[i] = true;
				dfs(k+1, t, dist+d[i][2]);
				u[i] = false;
			}
			else{
				int t = d[i][0];
				u[i] = true;
				dfs(k+1, t, dist+d[i][2]);
				u[i] = false;
			}
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			n = sc.nextInt();
			m = sc.nextInt();
			if((n|m)==0)break;
			d = new int[m][3];		
			for(int i=0;i<m;i++)for(int j=0;j<3;j++)d[i][j]=sc.nextInt();
			trace = new int[m];
			u = new boolean[m];
			max = 0;
			for(int i=0;i<m;i++){
				u[i] = true;
				trace[0] = d[i][0];
				dfs(1, d[i][1], d[i][2]);
				trace[0] = d[i][1];
				dfs(1, d[i][0], d[i][2]);
				u[i] = false;
			}
			System.out.println(max);
			for(int i=0;i<ans.length;i++)System.out.print(ans[i]+(i==ans.length-1?"\n":" "));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}