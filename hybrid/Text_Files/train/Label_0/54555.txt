import java.awt.geom.*;
import java.io.*;
import java.util.*;
//reference rankalee's code
public class Main {
	double EPS = 1.0e-08;
	
	class P{
		double [] p;
		public P(double[] p) {
			this.p = new double[3];
			for(int i =0; i < 3; i++){
				this.p[i] = p[i];
			}
			this.p = p;
		}
	}
	
	class Line{
		P p1, p2;

		public Line(P p1, P p2) {
			this.p1 = p1;
			this.p2 = p2;
		}
		
	}
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0)break;
			double [] input = new double[3];
			for(int i = 0; i < 3; i++) input[i] = sc.nextInt();
			P last = new P(new double[3]);
			P dir = new P(input);
			P [] data = new P[n];
			double [] rlist = new double[n];
			for(int i = 0; i < n; i++){
				double [] temp = new double[3];
				temp[0] = sc.nextInt();
				temp[1] = sc.nextInt();
				temp[2] = sc.nextInt();
				data[i] = new P(temp);
				rlist[i] = sc.nextInt();
			}
			while(true){
				double mn = 1 << 24;
				int mni = -1;
				Line l = new Line(last, dir);
				double ldis = distance(last, dir);
				for(int i = 0; i < n; i++){
					double disL = distanceLP(l, data[i]);
					if(disL >= rlist[i]) continue;
					
					P linep = projection(l , data[i]);
					double temp = distance(last, linep) + distance(linep, dir) ;
					if(ldis + EPS > temp ||  distance(last, linep) > distance(linep, dir)){
						if(disL >= rlist[i]) continue;
						double nowdis = distance(last, linep) - Math.sqrt(rlist[i] * rlist[i] - disL * disL);
						
						if(nowdis < EPS) continue;
						
						//System.out.println(nowdis / ldis);
						if(mn > nowdis / ldis){
							mn = nowdis / ldis;
							mni = i;
						}
					}
					//System.out.println("line = "+ i + " "+ Arrays.toString(linep.p));
					
					
				}
				//System.out.println("cand = " + mni + " mindis " + mn);
				if(mni == -1){
					break;
				}
				P nextdist = add(last, mul(mn, sub(dir, last)));
				Line midLine = new Line(data[mni], nextdist);
				P nextterm = reflection(midLine, last);
				last = new P(nextdist.p.clone());
				dir = new P(nextterm.p.clone());
			}
			System.out.printf("%.4f %.4f %.4f\n",last.p[0],last.p[1],last.p[2] );
		}
	}

	private P reflection(Line l, P p) {
		return add(p, mul(2.0, sub(projection(l,p) , p)));
	}

	private double distance(P p1, P p2) {
		double res = 0;
		for(int i = 0; i < 3; i++){
			res += (p1.p[i] - p2.p[i]) * (p1.p[i] - p2.p[i]);
		}
		return Math.sqrt(res);
	}

	private double distanceLP(Line l, P p) {
		return abs(sub(p, projection(l,p)));
	}

	private double abs(P p) {
		return Math.sqrt(norm(p));
	}

	private double norm(P p) {
		return dot(p,p);
	}

	private double dot(P p1, P p2) {
		double res = 0.0;
		for(int i = 0; i < 3; i++){
			res += p1.p[i] * p2.p[i];
		}
		return res;
	}

	private P sub(P p1, P p2) {
		double [] res = new double[3];
		for(int i = 0; i < 3; i++){
			res[i] = p1.p[i] - p2.p[i];
		}
		return new P(res);
	}

	private P projection(Line l, P p) {
		double t = dot(sub(p, l.p1), sub(l.p1, l.p2)) / norm(sub(l.p1, l.p2));
		return add(l.p1, mul(t, (sub(l.p1, l.p2))));
	}

	private P add(P p1, P p2) {
		double [] res = new double[3];
		for(int i = 0; i < 3; i++){
			res[i] = p1.p[i] + p2.p[i];
		}
		return new P(res);
	}

	private P mul(double t, P p) {
		double [] res = new double[3];
		for(int i = 0; i < 3; i++){
			res[i] = p.p[i] * t;
		}
		return new P(res);
	}

	public static void main(String [] args){
		new Main().doit();
	}
}