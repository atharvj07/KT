import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int n, m;
	HashMap<String, Integer> map;
	String[] dic;

	void run(){
		m=sc.nextInt();
		n=sc.nextInt();
		sc.nextLine();
		map=new HashMap<String, Integer>();
		for(int i=0; i<m; i++){
			for(String s : sc.nextLine().split(" ")){
				if(!map.containsKey(s)){
					map.put(s, 0);
				}
				map.put(s, map.get(s)+1);
			}
		}
		m=map.size();
		dic=new String[n];
		for(int i=0; i<n; i++){
			dic[i]=sc.next();
		}
		solve();
	}

	void solve(){
//		debug("map", map);
//		debug("dic", dic);
		V s=new V(), t=new V();
		V[] us=new V[m], vs=new V[n];
		for(int i=0; i<m; i++){
			us[i]=new V();
			s.add(us[i], 1, 0);
		}
		for(int i=0; i<n; i++){
			vs[i]=new V();
			vs[i].add(t, 1, 0);
		}
		String[] text=map.keySet().toArray(new String[0]);
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				int d=levenshteinDistance(text[i], dic[j]);
				// debug(text[i], dic[j], d,map.get(text[i]));
				us[i].add(vs[j], 1, d*map.get(text[i]));
			}
		}
		ArrayList<V> list=new ArrayList<V>(asList(s, t));
		list.addAll(asList(vs));
		list.addAll(asList(us));
		println(primalDual(list.toArray(new V[0]), s, t, m)+"");
	}

	int[][] d=new int[1001][1001];

	int levenshteinDistance(String s, String t){
		int m=s.length(), n=t.length();
		for(int j=1; j<=n; j++)
			d[j][0]=j;
		for(int i=1; i<=m; i++)
			d[0][i]=i;
		for(int j=1; j<=n; j++){
			for(int i=1; i<=m; i++){
				int cost=s.charAt(i-1)==t.charAt(j-1)?0:1;
				d[j][i]=min(d[j][i-1]+1, min(d[j-1][i]+1, d[j-1][i-1]+cost));
			}
		}
		return d[n][m];
	}

	int primalDual(V[] vs, V s, V t, int f){
		int cost=0;
		for(; f>0;){
			dijkstra(vs, s);
			if(t.d==INF)
				return -1;
			for(V v : vs)
				v.h+=v.d;
			int d=f;
			for(E e=t.pre; e!=null; e=e.rev.to.pre)
				d=min(d, e.cap);
			for(E e=t.pre; e!=null; e=e.rev.to.pre){
				e.cap-=d;
				e.rev.cap+=d;
			}
			f-=d;
			cost+=d*t.h;
		}
		return cost;
	}

	void dijkstra(V[] vs, V s){
		PriorityQueue<E> que=new PriorityQueue<E>();
		for(V v : vs)
			v.d=INF;
		s.d=0;
		que.offer(new E(s, 0, s.d));
		for(; !que.isEmpty();){
			E p=que.poll();
			if(p.cost>p.to.d)
				continue;
			for(E e : p.to.es){
				int d=p.cost+e.cost+p.to.h-e.to.h;
				if(e.cap>0&&d<e.to.d){
					e.to.d=d;
					e.to.pre=e;
					que.offer(new E(e.to, 0, e.to.d));
				}
			}
		}
	}

	class V{
		ArrayList<E> es=new ArrayList<E>();
		E pre;
		int h, d;

		void add(V to, int cap, int cost){
			E e=new E(to, cap, cost), rev=new E(this, 0, -cost);
			e.rev=rev;
			rev.rev=e;
			es.add(e);
			to.es.add(rev);
		}
	}

	class E implements Comparable<E>{
		V to;
		E rev;
		int cap, cost;

		E(V to, int cap, int cost){
			this.to=to;
			this.cap=cap;
			this.cost=cost;
		}

		@Override
		public int compareTo(E e){
			return cost-e.cost;
		}
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}