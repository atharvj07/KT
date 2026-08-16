import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

//Reverse Roads
public class Main{

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
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] e = new int[m][2];
		cap = new int[n][n];
		for(int i=0;i<m;i++){
			int from = sc.nextInt()-1;
			int to = sc.nextInt()-1;
			e[i][0] = from;
			e[i][1] = to;
			cap[from][to] = 1;
			cap[to][from] = 1;
		}
		int s = sc.nextInt()-1;
		int t = sc.nextInt()-1;
		System.out.println(maxFlow(s, t));
		int r = 0;
		List<Integer> l = new ArrayList<Integer>();
		for(int i=0;i<m;i++){
			if(cap[e[i][1]][e[i][0]]==0){
				r++;
				l.add(i+1);
			}
		}
		System.out.println(r);
		for(int i:l)System.out.println(i);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}