import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

//Bicycle Diet
public class Main{

	class E{
		int s, t, c;
		public E(int s, int t, int c) {
			this.s = s;
			this.t = t;
			this.c = c;
		}
	}
	
	int m, n, k, d;
	
	int get(String s){
		if(s.charAt(0)=='H')return n+m;
		if(s.charAt(0)=='D')return n+m+1;
		int x = Integer.parseInt(s.substring(1))-1;
		return s.charAt(0)=='C'?x:x+m;
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			m = sc.nextInt();
			n = sc.nextInt();
			k = sc.nextInt();
			d = sc.nextInt();
			if((m|n|k|d)==0)break;
			int[] cake = new int[m];
			for(int i=0;i<m;i++)cake[i]=sc.nextInt();
			int N = m+n+2;
			List<E> l[] = new ArrayList[N];
			for(int i=0;i<N;i++)l[i]=new ArrayList<E>();
			while(d--!=0){
				int s = get(sc.next());
				int t = get(sc.next());
				int cost = sc.nextInt()*k;
				l[s].add(new E(s,t,cost));
				l[t].add(new E(t,s,cost));
			}
			int[][] dist = new int[N][1<<m];
			for(int[]a:dist)Arrays.fill(a, 1<<28);
			boolean[][] u = new boolean[N][1<<m];
			dist[n+m][0] = 0;
			u[n+m][0] = true;
			boolean update = true;
			while(update){
				update = false;
				boolean[][] next = new boolean[N][1<<m];
				for(int i=0;i<N;i++){
					for(int j=0;j<1<<m;j++){
						if(!u[i][j])continue;
						for(E e:l[i]){
							if(m<=e.t){
								int v = dist[i][j]+e.c;
								if(v<dist[e.t][j]){
									dist[e.t][j] = v;
									update = true;
									next[e.t][j] = true;
								}
							}
							else {
								if((j&(1<<e.t))>0)continue;
								int v = dist[i][j]+e.c-cake[e.t];
								if(v<dist[e.t][j+(1<<e.t)]){
									dist[e.t][j+(1<<e.t)] = v;
									update = true;
									next[e.t][j+(1<<e.t)] = true;
								}
							}
						}
					}
				}
				u = next;
			}
			int min = 1<<28;
			for(int j=0;j<1<<m;j++)min = Math.min(min, dist[n+m+1][j]);
			System.out.println(min);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}