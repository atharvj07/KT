import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-9;

	int n;
	int[] b, x, y;
	int m;
	int[] s, g;
	HashMap<Integer, Integer> map;

	void run(){
		for(;;){
			n=sc.nextInt();
			if(n==0){
				break;
			}
			b=new int[n];
			x=new int[n];
			y=new int[n];
			for(int i=0; i<n; i++){
				b[i]=sc.nextInt();
				x[i]=sc.nextInt();
				y[i]=sc.nextInt();
			}
			m=sc.nextInt();
			s=new int[m];
			g=new int[m];
			for(int i=0; i<m; i++){
				s[i]=sc.nextInt();
				g[i]=sc.nextInt();
			}
			solve();
		}
	}

	void solve(){
		map=new HashMap<Integer, Integer>();
		for(int i=0; i<n; i++){
			map.put(b[i], i);
		}

		@SuppressWarnings("unchecked")
		LinkedList<E>[] es=new LinkedList[n];
		for(int j=0; j<n; j++){
			es[j]=new LinkedList<E>();
			for(int i=0; i<n; i++){
				if(i==j){
					continue;
				}
				double cost=Math.hypot(x[i]-x[j], y[i]-y[j]);
				if(cost<50+EPS){
					es[j].add(new E(i, cost));
				}
			}
		}
		for(int i=0; i<m; i++){
			LinkedList<Integer> path=dijkstra(es, map.get(s[i]), map.get(g[i]));
			if(path==null){
				println("NA");
			}else{
				for(int k=0; k<path.size(); k++){
					print(b[path.get(k)]+(k==path.size()-1?"\n":" "));
				}
			}
		}
	}

	LinkedList<Integer> dijkstra(LinkedList<E>[] es, int s, int g){
		int n=es.length;
		double[] d=new double[n];
		int[] pre=new int[n];
		PriorityQueue<P> que=new PriorityQueue<P>();

		Arrays.fill(d, INF);
		Arrays.fill(pre, -1);
		d[s]=0;
		pre[s]=s;
		que.offer(new P(s, 0));
		for(; !que.isEmpty();){
			P p=que.poll();
			if(d[p.v]<p.d)
				continue;
			for(E e : es[p.v]){
				if(d[e.to]>d[p.v]+e.cost){
					pre[e.to]=p.v;
					d[e.to]=d[p.v]+e.cost;
					que.offer(new P(e.to, d[e.to]));
				}
			}
		}
		LinkedList<Integer> path=new LinkedList<Integer>();
		for(int i=g;; i=pre[i]){
			path.addFirst(i);
			if(i==-1){
				return null;
			}
			if(i==s){
				return path;
			}
		}
	}

	class E{
		int to;
		double cost;

		E(int to, double cost){
			this.to=to;
			this.cost=cost;
		}
	}

	class P implements Comparable<P>{
		int v;
		double d;

		P(int v, double d){
			this.v=v;
			this.d=d;
		}

		@Override
		public int compareTo(P p){
			if(d+EPS<p.d){
				return -1;
			}else if(d>p.d+EPS){
				return 1;
			}else{
				return 0;
			}
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
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}