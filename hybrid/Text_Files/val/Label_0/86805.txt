import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

//School Excursion
public class Main{

//	int[][] cap;
	Map<Integer, Integer>[] capmap;
	Map<Integer, Integer>[] costmap;
//	short[][] cost;
	int[] prev;
	int[] dist;
	
	int minimumCostFlow(int s, int t, int f){
		int flow = 0;
		int n = capmap.length;
//		int n = cap.length;
		while(f > 0){
			Arrays.fill(dist, Integer.MAX_VALUE);
			dist[s] = 0;
			boolean isUpdate = true;
			while(isUpdate){
				isUpdate = false;
				for(int v=0;v<n;v++){
					if(dist[v]==Integer.MAX_VALUE)continue;
					for(int j:capmap[v].keySet()){
						if(capmap[v].get(j)>0 && dist[v] + (costmap[v].get(j)==null?0:costmap[v].get(j)) < dist[j]){
							isUpdate = true;
							prev[j] = v;
							dist[j] = dist[v] + (costmap[v].get(j)==null?0:costmap[v].get(j));
						}
					}
				}
			}
			if(dist[t]==Integer.MAX_VALUE)return -1;
			int d = f;
			for(int v=t;v!=s;v=prev[v]){
				d = Math.min(d, capmap[prev[v]].get(v));
			}
			f -= d;
			flow += d*dist[t];
			for(int v=t;v!=s;v=prev[v]){
				capmap[prev[v]].put(v, capmap[prev[v]].get(v)-d);
//				cap[prev[v]][v] -= d;
				capmap[v].put(prev[v], capmap[v].get(prev[v])==null?0:capmap[v].get(prev[v])+d);
//				cap[v][prev[v]] += d;
			}
		}
		return flow;
	}
	
	int[] h;
	int minimumFlow(int s, int t, int f){
		int flow = 0;
		Arrays.fill(h, 0);
		while(f>0){
			PriorityQueue<int[]> q = new PriorityQueue<int[]>(255, new Comparator<int[]>() {
				public int compare(int[] o1, int[] o2) {
					return o1[0] - o2[0];
				}
			});
			Arrays.fill(dist, Integer.MAX_VALUE);
			dist[s] = 0;
			q.add(new int[]{0, s});
			while(!q.isEmpty()){
				int[] p = q.poll();
				int v = p[1];
				if(dist[v] < p[0])continue;
				for(int i:capmap[v].keySet()){
					if(capmap[v].get(i)>0 && dist[v] + (costmap[v].get(i)==null?0:costmap[v].get(i)) + h[v] - h[i] < dist[i]){
						dist[i] = dist[v] + (costmap[v].get(i)==null?0:costmap[v].get(i)) + h[v] - h[i];
						prev[i] = v;
						q.add(new int[]{dist[i], i});
					}
				}
			}
			if(dist[t]==Integer.MAX_VALUE){
				return -1;
			}
			for(int v=0;v<dist.length;v++){
				h[v] += dist[v];
			}
			int d = f;
			for(int v=t;v!=s;v=prev[v]){
				d = Math.min(d, capmap[prev[v]].get(v));
			}
			f -= d;
			flow += d*h[t];
			for(int v=t;v!=s;v=prev[v]){
				capmap[prev[v]].put(v, capmap[prev[v]].get(v)-d);
				capmap[v].put(prev[v], capmap[v].get(prev[v])==null?0:capmap[v].get(prev[v])+d);
//				cap[prev[v]][v] -= d;
//				cap[v][prev[v]] += d;
			}
		}
		return flow;
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		prev = new int[6000]; dist = new int[6000]; h = new int[6000];
		costmap = new Map[6000]; capmap = new Map[6000];
		for(int i=0;i<6000;i++){
			capmap[i]=new HashMap<Integer, Integer>();
			costmap[i] = new HashMap<Integer, Integer>();
		}
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			int N = 0;
			Set<Integer>[] set = new Set[n-1];
			int[][][] edge = new int[n-1][][];
			int[][] ids = new int[n-1][];
			Map<Integer, Integer>[] in = new Map[n-1], out = new Map[n-1];
			for(int i=0;i<n-1;i++){
				in[i] = new HashMap<Integer, Integer>();
				out[i] = new HashMap<Integer, Integer>();
				set[i] = new HashSet<Integer>();
				int m = sc.nextInt();
				ids[i] = new int[m];
				edge[i] = new int[m][3];
				for(int j=0;j<m;j++){
					int s = sc.nextInt(), t = sc.nextInt(), c = sc.nextInt();
					edge[i][j][0] = s; edge[i][j][1] = t; edge[i][j][2] = c;
					set[i].add(t);
				}
			}
			for(int i=0;i<n-1;i++){
				for(int j=0;j<edge[i].length;j++)ids[i][j] = N++;
				for(int x:set[i]){
					in[i].put(x, N++); out[i].put(x, N++);
				}
			}
			int S = N, PRE = N+1, T = N+2;
			N+=3;
			int G = sc.nextInt();
			for(int i=0;i<N;i++){
				capmap[i].clear();
				costmap[i].clear();
//				for(int j=0;j<N;j++)cost[i][j]=0;
			}
			for(int j=0;j<edge[0].length;j++){
				capmap[S].put(ids[0][j], 1);
				costmap[S].put(ids[0][j], 0);
//				cost[S][ids[0][j]] = 0;
			}
			capmap[PRE].put(T, G);
			costmap[PRE].put(T, 0);
//			cost[PRE][T] = 0;
			for(int x:set[n-2]){
				capmap[out[n-2].get(x)].put(PRE, 1);
				costmap[out[n-2].get(x)].put(PRE, 0);
//				cost[out[n-2].get(x)][PRE] = 0;
			}
			for(int i=0;i<n-1;i++){
				for(int j=0;j<edge[i].length;j++){
					int s = ids[i][j], t = in[i].get(edge[i][j][1]), c = edge[i][j][2];
					capmap[s].put(t, 1);
					costmap[s].put(t, c);
//					cost[s][t] = (short) c;
				}
				for(int x:set[i]){
					int s = in[i].get(x), t = out[i].get(x);
					capmap[s].put(t, 1);
					costmap[s].put(t, 0);
//					cost[s][t] = 0;
				}
				if(i+1<n-1){
					for(int x:set[i]){
						int s = out[i].get(x);
						for(int j=0;j<edge[i+1].length;j++){
							if(x<=edge[i+1][j][0]){
								capmap[s].put(ids[i+1][j], 1);
								costmap[s].put(ids[i+1][j], 0);
//								cost[s][ids[i+1][j]] = 0;
							}
						}
					}
				}
			}
			int max = 0, res = 0;
			for(int g=1;g<=G;g++){
				int r = minimumCostFlow(S, T, 1);
//				System.out.println("G:"+g+" R:"+r);
				if(r!=-1){
					max = g; res += r;
				}
			}
			System.out.println(max+" "+res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}