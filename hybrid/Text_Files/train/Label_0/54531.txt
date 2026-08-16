import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

//Sort the Panels
public class Main{

	int[][] dist;
	int n, M = 20, INF = 1<<29, S, G;
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			n = sc.nextInt();
			if(n==0)break;
			char[] t1 = sc.next().toCharArray(), t2 = sc.next().toCharArray();
			S = 0; G = 0;
			for(int i=0;i<n;i++){
				S+=t1[i]=='W'?1<<i:0; G+=t2[i]=='W'?1<<i:0;
			}
			dist = new int[1<<n][n];
			for(int[]a:dist)Arrays.fill(a, INF);
			PriorityQueue<Integer> q = new PriorityQueue<Integer>(n, new Comparator<Integer>() {
				public int compare(Integer o1, Integer o2) {
					return dist[o1/M][o1%M]-dist[o2/M][o2%M];
				}
			});
			for(int i=0;i<n;i++){
				dist[S][i] = 0; q.add(S*M+i);
			}
			while(!q.isEmpty()){
				int V = q.poll();
				int s = V/M, p = V%M;
				if(s==G){
					System.out.println(dist[s][p]); break;
				}
				for(int a=0;a<n;a++){
					int pa = s&(1<<a);
					if(pa==(G&(1<<a)))continue;
					for(int b=0;b<n;b++){
						if(a==b||(s&(1<<b))==(G&(1<<b)))continue;
						int w = dist[s][p]+Math.abs(p-a)+Math.abs(a-b);
						int pb = s&(1<<b), ns = s;
						if(pa>0)ns|=1<<b;
						else ns&=~(1<<b);
						if(pb>0)ns|=1<<a;
						else ns&=~(1<<a);
						if(w<dist[ns][b]){
							dist[ns][b] = w; q.add(ns*M+b);
						}
					}
				}
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}