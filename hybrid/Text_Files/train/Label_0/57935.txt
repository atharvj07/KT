import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Crop Circle
public class Main{

	final double EPS = 1e-8;
	final double[] BASE = {1, 0};
	
	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	double cross(double[] a, double[] b){
		return a[0]*b[1]-a[1]*b[0];
	}
	double norm(double[] a){
		return Math.sqrt(a[0]*a[0]+a[1]*a[1]);
	}
	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0], a[1]-b[1]};
	}
	void swap(double[] a, double[] b){
		double t = a[0];
		a[0] = b[0]; b[0] = t;
		t = a[1];
		a[1] = b[1]; b[1] = t;
	}
	double angleTan(double[] a, double[] b){
		return Math.atan2(cross(a, b), dot(a, b));
	}
	
	int checkCircleOverlap(double x1, double y1, double r1, double x2, double y2, double r2){
		double d2 = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
		if((r1+r2)*(r1+r2) < d2)return -1;
		double d = Math.sqrt(d2);
		if(d+r1<r2+EPS)return -2;
		if(r2 < r1 && d+r2 < r1+EPS)return 0;
		if(Math.abs(d-r1-r2)<EPS)return 1;
		return 2;
	}
	
	double[][] circleCrossPoint(double x1, double y1, double r1, double x2, double y2, double r2){
		double vx = x2-x1, vy = y2-y1, D = Math.sqrt(vx*vx+vy*vy);
		vx/=D; vy/=D;
		vx*=r1; vy*=r1;
		double thita = Math.acos((r1*r1+D*D-r2*r2)/(2*r1*D));
		double px = Math.cos(thita)*vx-Math.sin(thita)*vy, py = Math.sin(thita)*vx+Math.cos(thita)*vy;
		double px2 = Math.cos(-thita)*vx-Math.sin(-thita)*vy, py2 = Math.sin(-thita)*vx+Math.cos(-thita)*vy;
		double[][] res = new double[2][2];
		res[0][0] = x1+px; res[0][1] = y1+py;
		res[1][0] = x1+px2; res[1][1] = y1+py2;
		if(ccw(new double[]{x1, y1}, new double[]{x2, y2}, res[0])==1)swap(res[0], res[1]);
		return res;
	}
	
	int ccw(double[] a, double[] b, double[] c){
		b = sub(b, a); c = sub(c, a);
		if(cross(b, c) > 0)return 1;
		if(cross(b, c) < 0)return -1;
		if(dot(b, c) < 0)return +2;
		if(norm(b) < norm(c))return -2;
		return 0;
	}
	
	class CircumferenceRange{
		List<double[]> ranges;
		public CircumferenceRange() {
			ranges = new ArrayList<double[]>();
			ranges.add(new double[]{0, 2*Math.PI});
		}
		private double trans(double thita){
			return thita<0?2*Math.PI+thita:thita;
		}
		void sub(double from, double to){
			double f = trans(from), t = trans(to);
			if(t < f){
				subOffer(0, t);
				subOffer(f, 2*Math.PI);
			}
			else subOffer(f, t);
		}
		private void subOffer(double from, double to){
			for(int i=0;i<ranges.size();i++){
				double[] d = ranges.get(i);
				if(to < d[0] || d[1] < from)continue;
				if(from < d[0]+EPS && d[1] < to+EPS){
					ranges.remove(i--);
				}
				else if(d[0] < from && to < d[1]){
					ranges.remove(i);
					ranges.add(i, new double[]{to, d[1]});
					ranges.add(i++, new double[]{d[0], from});
				}
				else if(to < d[1]){
					ranges.remove(i);
					ranges.add(i, new double[]{to, d[1]});
				}
				else {
					ranges.remove(i);
					ranges.add(i, new double[]{d[0], from});
				}
			}
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			double[] x = new double[n], y = new double[n], r = new double[n];
			CircumferenceRange[] cr = new CircumferenceRange[n];
			for(int i=0;i<n;i++){
				x[i] = sc.nextDouble(); y[i] = sc.nextDouble(); r[i] = sc.nextDouble();
				cr[i] = new CircumferenceRange();
			}
			for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){
				int c = checkCircleOverlap(x[i], y[i], r[i], x[j], y[j], r[j]);
				if(c==0){
					cr[j].ranges.clear();
				}
				if(c!=2)continue;
				double[][] cp = circleCrossPoint(x[i], y[i], r[i], x[j], y[j], r[j]);
				cr[i].sub(angleTan(BASE, sub(cp[0], new double[]{x[i], y[i]})), angleTan(BASE, sub(cp[1], new double[]{x[i], y[i]})));
			}
			double res = 0;
			for(int i=0;i<n;i++)for(double[]d:cr[i].ranges)res+=r[i]*(d[1]-d[0]);
			System.out.printf("%.9f\n", res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}