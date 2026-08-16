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

	int n, w;
	int[] a, b;

	void run(){
		n=sc.nextInt();
		w=sc.nextInt();
		a=new int[n];
		b=new int[n];
		for(int i=0; i<n; i++){
			a[i]=sc.nextInt();
		}
		for(int i=0; i<n; i++){
			b[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		// x累積和(mod 2)
		// x[i]=x[i-1] <=> S[i]=0
		// => -a[i]
		// x[i-w-1] = x[i+w] <=> S[i-w, i+w] = 0
		// => -b[i]

		// y[i] = x[i]+i mod 2
		// y[i] != y[i-1] => -a[i]
		// y[i-w-1] != y[i+w] => -b[i]

		int scoreSum=0, bestScore=-1;
		for(int i : a){
			scoreSum+=i;
		}
		for(int i : b){
			scoreSum+=i;
		}
		String ans=null;
		for(int sum=0; sum<2; sum++){
			V[] vs=new V[n+w*2+3];
			for(int i=0; i<vs.length; i++){
				vs[i]=new V();
			}
			V s=vs[n+w*2+1], t=vs[n+w*2+2];
			// [0, w]
			for(int i=0; i<=w; i++){
				if(i%2==0){
					s.add(vs[i], INF);
				}else{
					vs[i].add(t, INF);
				}
			}
			// [n+w, n+w*2]
			for(int i=n+w; i<=n+w*2; i++){
				if((i+sum)%2==0){
					s.add(vs[i], INF);
				}else{
					vs[i].add(t, INF);
				}
			}
			// [w+1, n+w]
			for(int i=w+1; i<=n+w; i++){
				int at=i-w-1;
				vs[i-w-1].add(vs[i+w], b[at]);
				vs[i+w].add(vs[i-w-1], b[at]);
				vs[i].add(vs[i-1], a[at]);
				vs[i-1].add(vs[i], a[at]);
			}
			int score=scoreSum-fordFulkerson(vs, s, t);
//			debug(score);
			if(score>bestScore){
				bestScore=score;
				for(V v : vs){
					v.used=false;
				}
				visit(s);
				StringBuilder sb=new StringBuilder();
				for(int i=w+1; i<=n+w; i++){
					if(vs[i-1].used^vs[i].used){
						sb.append(0);
					}else{
						sb.append(1);
					}
				}
				ans=sb.toString();
			}
		}
		println(ans);
	}

	void println(String s){
		System.out.println(s);
	}

	void visit(V v){
		v.used=true;
		for(E e : v.es){
			if(e.cap>0&&!e.to.used){
				visit(e.to);
			}
		}
	}

	int fordFulkerson(V[] vs, V s, V t){
		for(int flow=0;;){
			for(V v : vs)
				v.used=false;
			int f=dfs(s, t, INF);
			if(f==0)
				return flow;
			flow+=f;
		}
	}

	int dfs(V v, V t, int f){
		if(v==t)
			return f;
		v.used=true;
		for(E e : v.es){
			if(!e.to.used&&e.cap>0){
				int d=dfs(e.to, t, min(f, e.cap));
				if(d>0){
					e.cap-=d;
					e.rev.cap+=d;
					return d;
				}
			}
		}
		return 0;
	}

	class V{
		ArrayList<E> es=new ArrayList<E>();
		boolean used;

		void add(V to, int cap){
			E e=new E(to, cap), rev=new E(this, 0);
			e.rev=rev;
			rev.rev=e;
			es.add(e);
			to.es.add(rev);
		}
	}

	class E{
		V to;
		E rev;
		int cap;

		E(V to, int cap){
			this.to=to;
			this.cap=cap;
		}
	}

	void debug(Object... os){
		System.err.println(deepToString(os));
	}

	public static void main(String[] args){
		new Main().run();
	}

}