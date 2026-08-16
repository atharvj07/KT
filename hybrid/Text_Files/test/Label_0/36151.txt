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
	double EPS=1e-6;

	int n;
	double r;
	P[] ps;

	void run(){
		for(;;){
			n=sc.nextInt();
			if(n==0){
				break;
			}
			r=sc.nextInt();
			ps=new P[n];
			for(int i=0; i<n; i++){
				ps[i]=new P(sc.nextInt(), sc.nextInt());
			}
			solve();
		}
	}

	void solve(){
		P[][] qs=new P[n][];
		for(int i=0; i<n; i++){
			qs[i]=new P[]{ps[i].add(new P(0, r)), ps[i].add(new P(r, 0)),
					ps[i].add(new P(0, -r)), ps[i].add(new P(-r, 0))};
		}

		ArrayList<Seg> list1=new ArrayList<Seg>();

		for(int i=0; i<n; i++){
			int j=(i+1)%n;
			for(int k=0; k<4; k++){
				list1.add(new Seg(qs[i][k], qs[i][(k+1)%4]));
				list1.add(new Seg(qs[i][k], qs[j][k]));
			}
		}

		ArrayList<P> clist=new ArrayList<P>();
		for(Seg segP : list1){
			P p1=segP.p1, p2=segP.p2;
			for(Seg segQ : list1){
				P q1=segQ.p1, q2=segQ.p2;
				if(crsSS(p1, p2, q1, q2)){
					P c=isLL(p1, p2, q1, q2);
					if(c!=null){
						clist.add(c);
					}
				}
			}
			clist.add(p1);
			clist.add(p2);
		}

		// arrangement
		ArrayList<Seg> list2=new ArrayList<Seg>();
		for(Seg segP : list1){
			P p1=segP.p1, p2=segP.p2;
			ArrayList<P> list=new ArrayList<P>();
			for(P q : clist){
				if(disSP(p1, p2, q)<EPS){
					list.add(q);
				}
			}
			P[] cs=list.toArray(new P[0]);
			int m=cs.length;
			for(int i=0; i<m; i++){
				for(int j=i+1; j<m; j++){
					double d1=cs[i].sub(p1).abs();
					double d2=cs[j].sub(p1).abs();
					if(d1>d2){
						P t=cs[i];
						cs[i]=cs[j];
						cs[j]=t;
					}
				}
			}
			// debug(p1, p2, cs);
			for(int i=0; i<m-1; i++){
				if(cs[i].sub(cs[i+1]).abs()>EPS){
					list2.add(new Seg(cs[i], cs[i+1]));
				}
			}
		}
		Seg[] segs=list2.toArray(new Seg[0]);
		for(Seg seg : segs){
			// debug("seg", seg.p1, seg.p2);
		}
		int m=segs.length;
		boolean[] use=new boolean[m];
		fill(use, true);
		double sum=0;
		for(int i=0; i<m; i++){
			if(!use[i]){
				continue;
			}
			P p1=segs[i].p1, p2=segs[i].p2;
			for(int j=i+1; j<m; j++){
				P q1=segs[j].p1, q2=segs[j].p2;
				if(p1.sub(q1).abs()<EPS&&p2.sub(q2).abs()<EPS
						||p1.sub(q2).abs()<EPS&&p2.sub(q1).abs()<EPS){
					use[j]=false;
				}
			}
			// debug("use", p1, p2);
			P mid=p1.add(p2).div(2);
			double d=Double.MAX_VALUE;
			P x1=new P(-1e6, mid.y), x2=new P(+1e6, mid.y);
			P y1=new P(mid.x, -1e6), y2=new P(mid.x, +1e6);
			for(int k=0; k<n; k++){
				P q1=ps[k], q2=ps[(k+1)%n];
				d=min(d, abs(q1.x-mid.x)+abs(q1.y-mid.y));
				if(crsSS(x1, x2, q1, q2)){
					P c=isLL(x1, x2, q1, q2);
					if(c!=null){
						d=min(d, c.sub(mid).abs());
					}
				}
				if(crsSS(y1, y2, q1, q2)){
					P c=isLL(y1, y2, q1, q2);
					if(c!=null){
						d=min(d, c.sub(mid).abs());
					}
				}
			}
			// debug(p1, p2, d);
			if(d+EPS>r){
				if(contains(ps, p1)==1){
					// debug(p1, p2, d);
					sum+=p1.sub(p2).abs();
				}
			}
		}
		// debug(sum);
		println(String.format("%.12f", sum));
	}

	double map(double x, double x1, double x2, double y1, double y2){
		return 0;
	}

	double disSP(P p1, P p2, P q){
		if(p2.sub(p1).dot(q.sub(p1))<EPS)
			return q.sub(p1).abs();
		if(p1.sub(p2).dot(q.sub(p2))<EPS)
			return q.sub(p2).abs();
		return disLP(p1, p2, q);
	}

	double disLP(P p1, P p2, P q){
		return abs(p2.sub(p1).det(q.sub(p1)))/p2.sub(p1).abs();
	}

	boolean crsSS(P p1, P p2, P q1, P q2){
		if(max(p1.x, p2.x)+EPS<min(q1.x, q2.x))
			return false;
		if(max(q1.x, q2.x)+EPS<min(p1.x, p2.x))
			return false;
		if(max(p1.y, p2.y)+EPS<min(q1.y, q2.y))
			return false;
		if(max(q1.y, q2.y)+EPS<min(p1.y, p2.y))
			return false;
		return signum(p2.sub(p1).det(q1.sub(p1)))
				*signum(p2.sub(p1).det(q2.sub(p1)))<EPS
				&&signum(q2.sub(q1).det(p1.sub(q1)))
						*signum(q2.sub(q1).det(p2.sub(q1)))<EPS;
	}

	P isLL(P p1, P p2, P q1, P q2){
		double d=q2.sub(q1).det(p2.sub(p1));
		if(abs(d)<EPS)
			return null;
		return p1.add(p2.sub(p1).mul(q2.sub(q1).det(q1.sub(p1))/d));
	}

	int contains(P[] ps, P q){
		int n=ps.length;
		int res=-1;
		for(int i=0; i<n; i++){
			P a=ps[i].sub(q), b=ps[(i+1)%n].sub(q);
			if(a.y>b.y){
				P t=a;
				a=b;
				b=t;
			}
			if(a.y<EPS&&b.y>EPS&&a.det(b)>EPS){
				res=-res;
			}
			if(abs(a.det(b))<EPS&&a.dot(b)<EPS)
				return 0;
		}
		return res;
	}

	class Seg{
		P p1, p2;

		Seg(P p1, P p2){
			this.p1=p1;
			this.p2=p2;
		}
	}

	class P implements Comparable<P>{
		double x, y;

		P(double x, double y){
			this.x=x;
			this.y=y;
		}

		P add(P p){
			return new P(x+p.x, y+p.y);
		}

		P sub(P p){
			return new P(x-p.x, y-p.y);
		}

		P mul(double m){
			return new P(x*m, y*m);
		}

		P div(double d){
			return new P(x/d, y/d);
		}

		double abs(){
			return sqrt(abs2());
		}

		double abs2(){
			return x*x+y*y;
		}

		double arg(){
			return atan2(y, x);
		}

		double dot(P p){
			return x*p.x+y*p.y;
		}

		double det(P p){
			return x*p.y-y*p.x;
		}

		double ang(P p){
			return atan2(det(p), dot(p));
		}

		P rot90(){
			return new P(y, -x);
		}

		P rot(double d){
			return new P(cos(d)*x-sin(d)*y, sin(d)*x+cos(d)*y);
		}

		public int compareTo(P p){
			return Double.compare(x, p.x)*2+Double.compare(y, p.y);
		}

		public String toString(){
			return String.format("(%.3f, %.3f)", x, y);
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