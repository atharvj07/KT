import java.awt.geom.Point2D;
import java.util.*;

import static java.lang.Math.*;
public class Main {
	final Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		new AOJ2207();
	}
	class AOJ2207{
		int N;
		final int INF=1<<29;
		AOJ2207(){
			while(sc.hasNext()){
				N=sc.nextInt();
				if(N==0)	break;
				solve();
			}
		}
		void solve(){
			ArrayList<Edge> es=new ArrayList<Edge>();
			HashMap<String,Integer> map=new HashMap<String,Integer>();
			int kind=0;
			for(int i=0; i<N; ++i){
				sc.nextInt();
				String as=sc.next();
				int a=-1;
				if(map.containsKey(as))	a=map.get(as);
				else{
					a=kind;
					map.put(as, kind);
					++kind;
				}
				sc.next();
				int c=Integer.parseInt(sc.next().substring(3));
				String bs=sc.next();
				int b=-1;
				if(map.containsKey(bs))	b=map.get(bs);
				else{
					b=kind;
					map.put(bs, kind);
					++kind;
				}
				es.add(new Edge(a,b,c));
				es.add(new Edge(b,a,-c));
			}
//			System.out.println(es);

			bellmanFord bf=new bellmanFord(map.size(), es);
			for(int i=0; i<map.size(); ++i)if(bf.shortestPath(i)==null){
				System.out.println("No");
				return;
			}
			System.out.println("Yes");
		}
		class bellmanFord{
			final int INF=1<<29;
			int V,E;
			ArrayList<Edge> es;
			int[] d;
			bellmanFord(int V,ArrayList<Edge> es){
				this.V=V; this.es=es; this.E=es.size();
			}
			// startから到達可能な負の閉路があればnull．それ以外はstartからの最短経路．
			int[] shortestPath(int start){
				d=new int[V];
				for(int i=0; i<V; ++i)	d[i]=INF;
				d[start]=0;
				for(int i=1; i<=V; ++i){
					boolean update=false;
					for(Edge e:es){
						if(d[e.from]<INF && d[e.to]>d[e.from]+e.cost){
							d[e.to]=d[e.from]+e.cost;
							update=true;
							if(i==V)	return null;
						}
					}
					if(!update)	break;
				}
				return d;
			}
		}
		class Edge implements Comparable<Edge>{
			int from,to,cost;
			Edge(int from,int to,int cost){
				this.from=from;	this.to=to;	this.cost=cost;
			}
			@Override public int compareTo(Edge e){
				return this.cost-e.cost;
			}
			@Override public String toString(){
				return from+"->"+to+":"+cost;
			}
		}
	}
}