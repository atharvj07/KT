import java.util.Scanner;

//Malfatti Circles
public class Main{

	final double EPS = 1e-9, EPS2 = 1e-6;
	
	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	double cross(double[] a, double[] b){
		return a[0]*b[1]-a[1]*b[0];
	}
	double norm(double[] a){
		return Math.hypot(a[0], a[1]);
	}
	double norm(double[] a, double[] b){
		return Math.hypot(a[0]-b[0], a[1]-b[1]);
	}
	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0], a[1]-b[1]};
	}
	double[] mid(double[] a, double[] b){
		return new double[]{(a[0]+b[0])/2, (a[1]+b[1])/2};
	}
	double area(double[] a, double[] b, double[] c){
		double res = cross(a, b)+cross(b, c)+cross(c, a);
		return Math.abs(res)/2;
	}
	double ex(double[] a, double[] b, double[] c){
		double[] s1 = sub(b, a), s2 = sub(c, a);
		return cross(s1, s2);
	}
	double angleTan(double[] a, double[] b){
		return Math.atan2(cross(a, b), dot(a, b));
	}
	double angleCos(double[] a, double[] b){
		double na = norm(a), nb = norm(b);
		return Math.acos(dot(a, b)/na/nb);
	}
	boolean crossing(double[] a, double[] b, double[] s, double[] t){
		//A-B, S-Tが共に平行の場合、2線分間の距離が0か否かで交差を判定する
		if(Math.abs(cross(sub(b, a), sub(t, s)))<EPS){
			return Math.min(dist(a, b, s), Math.min(dist(a, b, t), Math.min(dist(s, t, a), dist(s, t, b))))<EPS;
		}
		if(ex(a, b, s)*ex(a, b, t)>0)return false;
		if(ex(b, a, s)*ex(b, a, t)>0)return false;
		if(ex(s, t, a)*ex(s, t, b)>0)return false;
		return ex(t, s, a)*ex(t, s, b)<EPS;
		//ここでex(,,)*ex(,,)<EPSとすると、(0,0)(1,0)-(2,0)(3.0)のような一直線に並んでいて交差していないものもtrueとなってしまう
		//→平行な場合は先頭のif文内で処理するようになった
	}
	//Segment a-b Point p
	double dist(double[] a, double[] b, double[] p){
		if(dot(sub(b, a), sub(p, a))<EPS)return norm(a, p);
		if(dot(sub(a, b), sub(p, b))<EPS)return norm(b, p);
		return Math.abs(cross(sub(b, a), sub(p, a)))/norm(a, b);
	}
	//Segment a-b Segment s-t
	double dist(double[] a, double[] b, double[] s, double[] t){
		if(crossing(a, b, s, t))return 0;
		return Math.min(dist(a, b, s), Math.min(dist(a, b, t), Math.min(dist(s, t, a), dist(s, t, b))));
	}
	//Line a-b Point p
	double distLP(double[] a, double[] b, double[] p){
		return Math.abs(cross(sub(b, a), sub(p, a)))/norm(a, b);
	}
	//TODO verify
	double[] cp(double[] a, double[] b, double[] s, double[] t){
		double ds = distLP(a, b, s), dt = distLP(a, b, t);
		double k = ds/(ds+dt);
		double[] d = sub(t, s);
		return new double[]{s[0]+k*d[0], s[1]+k*d[1]};
	}
	//TODO verify
	double thita(double[] a, double[] b){
		return Math.atan2(cross(a, b), dot(a, b));
	}
	//TODO verify
	double[][] circleCrossPoint(double x1, double y1, double r1, double x2, double y2, double r2){
		double x = x2-x1, y = y2-y1;
		double S = x*x+y*y;
		double A = (S+r1*r1-r2*r2)/2;
		double[][] res = new double[2][2];
		res[0][0] = (A*x+y*Math.sqrt(S*r1*r1-A*A))/S; res[0][1] = (A*y-x*Math.sqrt(S*r1*r1-A*A))/S;
		res[1][0] = (A*x-y*Math.sqrt(S*r1*r1-A*A))/S; res[1][1] = (A*y+x*Math.sqrt(S*r1*r1-A*A))/S;
		return res;
	}
	
	double[][] p, d, q;
	double[] thita, CP, len, r;
	
	int check(double t){
		q[0][0] = p[0][0]+t*d[0][0];
		q[0][1] = p[0][1]+t*d[0][1];
		r[0] = dist(p[0], p[1], q[0]);
		double R2 = dist(p[1], p[2], q[0]);
		if(R2+EPS < r[0])return 1;
//		System.out.println("r[0]: "+r[0]+" R2:"+R2);
		search(1); search(2);
//		System.out.println("Q1 "+q[1][0]+","+q[1][1]+" R:"+r[1]);
//		System.out.println("Q2 "+q[2][0]+","+q[2][1]+" R:"+r[2]);
//		System.out.println("NORM : " + norm(q[1], q[2]));
		if(Math.abs(r[1]+r[2]-norm(q[1], q[2]))<EPS2)return 0;
		return r[1]+r[2] < norm(q[1], q[2])?1:-1;
	}
	
	void search(int k){
		double L = 0, R = len[k];
		for(int LOOP=0;LOOP<80&&R-L>EPS;LOOP++){
			double m = (L+R)/2;
			int c = checkSub(m, k);
//			System.out.println("Search C:"+c+" K:"+k+" L:"+L+" R:"+R);
			if(c==0){
//				System.out.println("C==0**************************************************************");
				break;
			}
			if(c<0)L = m;
			else R = m;
		}
	}
	
	int checkSub(double t, int k){
		q[k][0] = p[k][0]+t*d[k][0];
		q[k][1] = p[k][1]+t*d[k][1];
//		System.out.println("Q0: "+q[0][0]+","+q[0][1]);
//		System.out.println("Q K:"+k+" "+q[k][0]+","+q[k][1]);
		r[k] = dist(p[k], p[(k+1)%3], q[k]);
		if(t < EPS)return -1;
		if(Math.abs(t-len[k])<EPS)return 1;
		double RK = dist(p[(k+1)%3], p[(k+2)%3], q[k]);
		if(RK+EPS < r[k])return 1;
//		System.out.println("T:"+t+" K:"+k+" R[k]:"+r[k]);
//		System.out.println("r[0]+r[k]: "+(r[0]+r[k]));
//		System.out.println("NORM:"+norm(q[0], q[k]));
		if(Math.abs(r[0]+r[k]-norm(q[0], q[k]))<EPS)return 0;
		return r[0]+r[k] < norm(q[0], q[k])?-1:1;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int X1 = sc.nextInt(), Y1 = sc.nextInt(), X2 = sc.nextInt(), Y2 = sc.nextInt(), X3 = sc.nextInt(), Y3 = sc.nextInt();
			if((X1|Y1|X2|Y2|X3|Y3)==0)break;
			p = new double[][]{{X1, Y1},{X2, Y2}, {X3, Y3}};
			thita = new double[3];
			d = new double[3][2];
			for(int i=0;i<3;i++){
				double[] subs = sub(p[(i+1)%3], p[i]), subt = sub(p[(i+2)%3], p[i]);
				double thita = angleTan(subs, subt)/2;
//				System.out.println(thita*180/Math.PI);
				d[i][0] = Math.cos(thita)*subs[0]-Math.sin(thita)*subs[1];
				d[i][1] = Math.sin(thita)*subs[0]+Math.cos(thita)*subs[1];
				double D = norm(d[i]);
				d[i][0]/=D; d[i][1]/=D;
//				System.out.println("D:"+d[i][0]+","+d[i][1]);
			}
			double[] A = p[0], B = {p[0][0]+10000*d[0][0], p[0][1]+10000*d[0][1]}, C = p[1], D = {p[1][0]+10000*d[1][0], p[1][1]+10000*d[1][1]};
			CP = cp(A, B, C, D);
			len = new double[3];
			for(int i=0;i<3;i++)len[i] = norm(p[i], CP);
//			System.out.println("CrossPoint: "+CP[0]+","+CP[1]);
//			System.out.println(len[0]+","+len[1]+","+len[2]);
			q = new double[3][2];
			r = new double[3];
			double L = 0, R = len[0];
			for(;;){
				double m = (L+R)/2;
				int c = check(m);
//				System.out.println("M:"+m);
//				System.out.println("RES C:"+c+" Q[0] "+q[0][0]+","+q[0][1]+" R:"+r[0]);
				if(c==0)break;
				if(c<0)L = m;
				else R = m;
			}
			System.out.printf("%.6f %.6f %.6f\n", r[0], r[1], r[2]);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}