import java.util.Scanner;

//Fishnet
public class Main{

	double EPS = 1.0e-8;
	double norm(Point p) {
		return Math.hypot(p.x, p.y);
	}
	double inp(Point p1, Point p2) {
		return p1.x*p2.x + p1.y*p2.y;
	}
	double extp(Point p1, Point p2) {
		return p1.x*p2.y - p2.x*p1.y;
	}
	Point sub(Point p1, Point p2) {
		return new Point(p1.x-p2.x, p1.y-p2.y);
	}
	int ccw(Point a, Point b, Point c) {
		Point p = sub(b, a);
		Point q = sub(c, a);
		if(extp(p, q) > EPS) return 1;		// counter clockwise
		if(extp(p, q) < -EPS)return -1;		// clockwise
		if(inp(p, q) < -EPS) return 2;		// c--a--b on line
		if(Math.abs(norm(p) - norm(q)) < EPS) return -2;	// a--b--c on line
		return 0;				// a--c--b(or a--c=b) on line 
	}
	Point crosspoint(Line l, Line m) {
		if(isParallel(l, m)){
			throw new IllegalArgumentException("parallel");
		}
		  double A = extp(sub(l.t, l.s), sub(m.t, m.s));
		  double B = extp(sub(l.t, l.s), sub(l.t, m.s));
		  if (Math.abs(A) < EPS && Math.abs(B) < EPS) return m.s; // same line
		  if (Math.abs(A) < EPS) assert(false); // !!!PRECONDITION NOT SATISFIED!!!
		  Point tp = sub(m.t, m.s);
		  return new Point(m.s.x + B/A*tp.x, m.s.y + B/A*tp.y);
	}
	boolean isParallel(Line l, Line m){
		Point a = new Point(l.t.x - l.s.x, l.t.y - l.s.y);
		Point b = new Point(m.t.x - m.s.x, m.t.y - m.s.y);
		if(Math.abs(Math.abs((a.x*b.x + a.y*b.y)/(Math.hypot(a.x, a.y)*Math.hypot(b.x, b.y)) - 1)) < EPS){
			return true;
		}
		return false;
	}
	class Point {
		public double x;
		public double y;
		public Point(double x_, double y_) {
			x = x_; y=y_;
		}
	}
	class Line {
		public Point s,t;
		public Line(Point s_, Point t_) {
			s = s_; t = t_;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			Point[][] p = new Point[4][n];
			for(int i=0;i<n;i++)p[0][i] = new Point(sc.nextDouble(), 0);
			for(int i=0;i<n;i++)p[1][i] = new Point(sc.nextDouble(), 1);
			for(int i=0;i<n;i++)p[2][i] = new Point(0, sc.nextDouble());
			for(int i=0;i<n;i++)p[3][i] = new Point(1, sc.nextDouble());
			Line[] v = new Line[n+2];
			Line[] h = new Line[n+2];
			v[0] = new Line(new Point(0, 0), new Point(0, 1));
			for(int i=1;i<=n;i++)v[i] = new Line(p[0][i-1], p[1][i-1]);
			v[n+1] = new Line(new Point(1,0), new Point(1,1));
			h[0] = new Line(new Point(0, 0), new Point(1,0));
			for(int i=1;i<=n;i++)h[i] = new Line(p[2][i-1], p[3][i-1]);
			h[n+1] = new Line(new Point(0,1), new Point(1,1));
			double max = 0;
			for(int i=0;i<=n;i++)for(int j=0;j<=n;j++){
				Point p1 = crosspoint(h[i], v[j]);
				Point p2 = crosspoint(h[i+1], v[j]);
				Point p3 = crosspoint(h[i+1], v[j+1]);
				Point p4 = crosspoint(h[i], v[j+1]);
				max = Math.max(max, Math.abs(extp(p1, p2)+extp(p2, p3)+extp(p3, p4)+extp(p4, p1)));
			}
			System.out.printf("%.7f\n", max/2);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}