import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//How I Mathematician Wonder What You Are!
public class Main{

	final double EPS = 1.0e-8;
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
	double area(Point[] p) {
		double s = 0;
		for(int i=0; i<p.length; i++) {
			int j = (i+1)%p.length;
			s += extp(p[i], p[j]);
		}
		return Math.abs(s);
	}
	Point[] convexCut(Point[] p, Line l) {
		List<Point> q = new ArrayList<Point>();
		for (int i = 0; i < p.length; ++i) {
			Point a= p[i], b = p[(i+1)%p.length];
			if (ccw(l.s, l.t, a) != -1) q.add(a);
		    if (ccw(l.s, l.t, a)*ccw(l.s, l.t, b) < 0)
		      q.add(crosspoint(new Line(a, b), l));
		}
		return q.toArray(new Point[q.size()]);
	}

	class Point {
		double x;
		double y;
		public Point(double x_, double y_) {
			x = x_; y=y_;
		}
	}
	class Line {
		Point s,t;
		Line(Point s_, Point t_) {
			s = s_; t = t_;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			Point[] p = new Point[n];
			for(int i=0;i<n;i++)p[i]=new Point(sc.nextDouble(), sc.nextDouble());
			Point[] c = new Point[4];
			c[0] = new Point(0, 0);
			c[1] = new Point(10000, 0);
			c[2] = new Point(10000, 10000);
			c[3] = new Point(0, 10000);
			for(int i=0;i<n;i++){
				Line l = new Line(p[i], p[(i+1)%n]);
				c = convexCut(c, l);
				if(area(c)<EPS)break;
			}
			System.out.println(area(c)<EPS?0:1);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}