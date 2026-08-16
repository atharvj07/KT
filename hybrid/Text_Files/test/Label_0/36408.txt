import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	static int[][] map = new int[21][21];
	static double[] d = new double[21];
	static int n;
	static HashSet<Integer> hash = new HashSet<Integer>();
	public static void main(String[] args) {
		solve();
	}

	private static void solve() {
		Scanner sc = new Scanner(System.in);
		PrintWriter pr = new PrintWriter(System.out);
		while(true){
			n = sc.nextInt();
			for(int s=0;s<21;s++){
				for(int t=0;t<21;t++){
					map[s][t] = Integer.MAX_VALUE;
				}
			}
			int hx = sc.nextInt();
			int hy = sc.nextInt();
			int dx = sc.nextInt();
			int dy = sc.nextInt();
			if(n==0&&hx==0&&hy==0&&dx==0&&dy==0){
				break;
			}
			int[] x = new int[n];
			int[] y = new int[n];
			for(int k=0;k<n;k++){
				x[k] = sc.nextInt();
				y[k] = sc.nextInt();
			}
			for(int k=0;k<n;k++){
				map[0][k+1] = (hx-x[k])*(hx-x[k])+(hy-y[k])*(hy-y[k]);
			}
			for(int s=0;s<n;s++){
				for(int t=0;t<n;t++){
					map[s+1][t+1] = (x[s]-x[t])*(x[s]-x[t])+(y[s]-y[t])*(y[s]-y[t]);
				}
			}
			d[0] = Integer.MAX_VALUE;
			for(int k=1;k<n+1;k++){
				d[k] = Math.sqrt((dx-x[k-1])*(dx-x[k-1])+(dy-y[k-1])*(dy-y[k-1]));
			}
			if(dfs(0,0)<Integer.MAX_VALUE){
				pr.println("YES");
			}else{
				pr.println("NO");
			}

		}
		pr.flush();
		sc.close();
	}

	private static double dfs(double i,int node) {
		if(i>=d[node]) return Integer.MAX_VALUE;
		if(hash.size()==n) return i;
		for(int k=1;k<n+1;k++){
			if(map[node][k]<Integer.MAX_VALUE&&hash.contains(k)!=true){
				hash.add(k);
				if (i + Math.sqrt(map[node][k]) >= d[k]) {
					hash.remove(k);
					return Integer.MAX_VALUE;
				}
				hash.remove(k);
			}
		}
		for(int k=1;k<n+1;k++){
			if(map[node][k]<Integer.MAX_VALUE&&hash.contains(k)!=true){
				hash.add(k);
				if(dfs(i+Math.sqrt(map[node][k]),k)<Integer.MAX_VALUE){
					hash.remove(k);
					return i;
				}
				hash.remove(k);
			}
		}
		return Integer.MAX_VALUE;
	}
}