import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

//Roads on Towns
public class Main{

	int NA, NB;
	double INF = 1L<<50, res = INF;

	final double EPS = 1e-10;

	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	double cross(double[] a, double[] b){
		return a[0]*b[1]-a[1]*b[0];
	}
	double norm(double[] a, double[] b){
		return Math.hypot(a[0]-b[0], a[1]-b[1]);
	}
	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0], a[1]-b[1]};
	}
	double area(double[] a, double[] b, double[] c){
		double res = cross(a, b)+cross(b, c)+cross(c, a);
		return Math.abs(res)/2;
	}
	double ex(double[] a, double[] b, double[] c){
		double[] s1 = sub(b, a), s2 = sub(c, a);
		return cross(s1, s2);
	}
	boolean crossing(double[] a, double[] b, double[] s, double[] t){
		if(Math.abs(cross(sub(b, a), sub(t, s)))<EPS){
			return Math.min(dist(a, b, s), Math.min(dist(a, b, t), Math.min(dist(s, t, a), dist(s, t, b))))<EPS;
		}
		if(ex(a, b, s)*ex(a, b, t)>0)return false;
		if(ex(b, a, s)*ex(b, a, t)>0)return false;
		if(ex(s, t, a)*ex(s, t, b)>0)return false;
		return ex(t, s, a)*ex(t, s, b)<EPS;
	}
	double dist(double[] a, double[] b, double[] p){
		if(dot(sub(b, a), sub(p, a))<EPS)return norm(a, p);
		if(dot(sub(a, b), sub(p, b))<EPS)return norm(b, p);
		return Math.abs(cross(sub(b, a), sub(p, a)))/norm(a, b);
	}

	double[][][] p;
	int[] ua, ub;
	int ka, kb;
	double[][] pd;
	
	double[] d;
	double dijkstraA(double D){
		if(res + EPS < D + pd[0][1])return INF;
		Arrays.fill(d, INF);
		d[0] = 0;
		PriorityQueue<Integer> q = new PriorityQueue<Integer>(NB, new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {
				return (int)Math.signum(d[o1]-d[o2]);
			}
		});
		q.add(0);
		while(!q.isEmpty()){
			int v = q.poll();
			if(v==1)return d[1];
			for(int i=1;i<NA;i++){
				double w = d[v] + pd[v][i];
				if(res+EPS < w+D)continue;
				boolean ok = true;
				for(int j=0;j+1<=kb&&ok;j++)if(crossing(p[1][ub[j]], p[1][ub[j+1]], p[0][v], p[0][i]))ok = false;
				if(ok && w < d[i]){
					d[i] = w; q.add(i);
				}
			}
		}
		return INF;
	}
	double dijkstraB(double D){
		if(res+EPS < D+pd[NA][NA+1])return INF;
		Arrays.fill(d, INF);
		d[0] = 0;
		PriorityQueue<Integer> q = new PriorityQueue<Integer>(NB, new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {
				return (int)Math.signum(d[o1]-d[o2]);
			}
		});
		q.add(0);
		while(!q.isEmpty()){
			int v = q.poll();
			if(v==1)return d[1];
			for(int i=1;i<NB;i++){
				double w = d[v] + pd[NA+v][NA+i];
				if(res+EPS < w+D)continue;
				boolean ok = true;
				for(int j=0;j+1<=ka&&ok;j++)if(crossing(p[0][ua[j]], p[0][ua[j+1]], p[1][v], p[1][i]))ok = false;
				if(ok && w < d[i]){
					d[i] = w; q.add(i);
				}
			}
		}
		return INF;
	}
	
	void fa(){
		for(int k=2;k<NA;k++){
			double d = pd[0][k] + pd[k][1];
			ka = 2;
			ua[1] = k; ua[2] = 1;
			res = Math.min(res, d+dijkstraB(d));
		}
	}
	void fb(){
		for(int k=2;k<NB;k++){
			double d = pd[NA][NA+k] + pd[NA+k][NA+1];
			kb = 2;
			ub[1] = k; ub[2] = 1;
			res = Math.min(res, d+dijkstraA(d));
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		NA = sc.nextInt(); NB = sc.nextInt();
		p = new double[2][][];
		p[0] = new double[NA][2]; p[1] = new double[NB][2];
		for(int i=0;i<NA;i++)for(int j=0;j<2;j++)p[0][i][j]=sc.nextDouble();
		for(int i=0;i<NB;i++)for(int j=0;j<2;j++)p[1][i][j]=sc.nextDouble();
		ua = new int[NA]; ub = new int[NB];
		d = new double[1000];
		pd = new double[NA+NB][NA+NB];
		for(int i=0;i<NA;i++){
			for(int j=i;j<NA;j++)pd[i][j] = pd[j][i] = norm(p[0][i], p[0][j]);
			for(int j=0;j<NB;j++)pd[i][NA+j] = pd[NA+j][i] = norm(p[0][i], p[1][j]);
		}
		for(int i=0;i<NB;i++){
			for(int j=i;j<NB;j++)pd[NA+i][NA+j] = pd[NA+j][NA+i] = norm(p[1][i], p[1][j]);
		}
		double d = pd[0][1];
		ua[1] = 1;
		ka = 1;
		res = Math.min(res, d+dijkstraB(d));
		d = pd[NA][NA+1];
		ub[1] = 1;
		kb = 1;
		res = Math.min(res, d+dijkstraA(d));
//		fa(); fb();
		if(res==INF)System.out.println(-1);
		else System.out.printf("%.10f\n", res);
	}

	public static void main(String[] args) {
		new Main().run();
	}
}