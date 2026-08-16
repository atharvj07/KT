import java.util.Arrays;
import java.util.Scanner;

//Flame of Nucleus
public class Main{

	int INF = 1<<29;
	int[][] cap;
	boolean[] used;
	
	int augumentPath(int v, int t, int f){
		if(v==t)return f;
		used[v] = true;
		for(int i=0;i<cap[v].length;i++){
			if(cap[v][i]>0 && !used[i]){
				int d = augumentPath(i, t, Math.min(f, cap[v][i]));
				if(d>0){
					cap[v][i] -= d;
					cap[i][v] += d;
					return d;
				}
			}
		}
		return 0;
	}

	int maxFlow(int s, int t){
		int flow = 0;
		int n = cap.length;
		used = new boolean[n];
		while(true){
			Arrays.fill(used, false);
			int f = augumentPath(s, t, Integer.MAX_VALUE);
			if(f==0)return flow;
			flow += f;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int n = sc.nextInt(), m = sc.nextInt(), L = sc.nextInt();
			int[][] wf = new int[n+1][n+1];
			for(int[]a:wf)Arrays.fill(a, INF);
			for(int i=1;i<=n;i++)wf[i][i]=0;
			while(m--!=0){
				int s = sc.nextInt(), t = sc.nextInt(), c = sc.nextInt();
				wf[s][t]=wf[t][s]=c;
			}
			for(int k=1;k<=n;k++)for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)wf[i][j]=Math.min(wf[i][j], wf[i][k]+wf[k][j]);
			int[] p = new int[n+1], k = new int[n+1];
			for(int i=1;i<=n;i++)p[i]=sc.nextInt();
			for(int i=1;i<=n;i++)k[i]=sc.nextInt();
			cap = new int[n*2+2][n*2+2];
			for(int i=1;i<=n;i++)cap[0][i]=p[i];
			for(int i=1;i<=n;i++)cap[n+i][2*n+1]=k[i];
			for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)if(wf[i][j]<L)cap[i][n+j]=p[i];
			System.out.println(maxFlow(0, 2*n+1));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}