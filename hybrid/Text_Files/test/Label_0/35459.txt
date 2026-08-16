import java.util.Scanner;


public class Main {

	
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int x1 = sc.nextInt();
			final int y1 = sc.nextInt();
			final int x2 = sc.nextInt();
			final int y2 = sc.nextInt();
			
			if(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0){
				break;
			}
			
			Point2D[][] lines = new Point2D[3][2];
			
			lines[0][0] = new Point2D(x1, y1);
			lines[0][1] = new Point2D(x2, y2);
			lines[1][0] = new Point2D(sc.nextInt(), sc.nextInt());
			lines[1][1] = new Point2D(sc.nextInt(), sc.nextInt());
			lines[2][0] = new Point2D(sc.nextInt(), sc.nextInt());
			lines[2][1] = new Point2D(sc.nextInt(), sc.nextInt());
			
			Point2D[] crosses = new Point2D[3];
			boolean not_found = false;
			for(int i = 0; i < 3; i++){
				if(Point2D.intersect_s(lines[i][0], lines[i][1], lines[i + 1 >= 3 ? 0 : (i + 1)][0], lines[i + 1 >= 3 ? 0 : (i + 1)][1])){
					crosses[i] = Point2D.interpoint_s(lines[i][0], lines[i][1], lines[i + 1 >= 3 ? 0 : (i + 1)][0], lines[i + 1 >= 3 ? 0 : (i + 1)][1]);
				}else{
					crosses[i] = null;
					not_found = true;
				}
				//System.out.println(crosses[i]);
			}
			
			if(not_found){
				System.out.println("kyo");
				continue;
			}
			
			boolean same = false;
			for(int i = 0; i < 3; i++){
				if(crosses[i].equals(crosses[i + 1 >= 3 ? 0 : (i + 1)])){
					same = true;
					break;
				}
			}
			
			if(same){
				System.out.println("kyo");
				continue;
			}
			
			double S = Point2D.area(crosses[0], crosses[1], crosses[2]);
			//System.out.println(S);
			if(S >= 1900000){
				System.out.println("dai-kichi");
			}else if(S >= 1000000){
				System.out.println("chu-kichi");
			}else if(S >= 100000){
				System.out.println("kichi");
			}else if(Double.isNaN(S)){
				System.out.println("kyo");
			}else{
				System.out.println("syo-kichi");
			}
			
			//なぜかテストケース通らない
		}
		
	}
}

class Point2D {
	public double x;
	public double y;

	public static final double EPS = 1e-9;

	public Point2D(double x, double y) {
		this.x = x;
		this.y = y;
	}

	public Point2D(Point2D point) {
		this.x = point.x;
		this.y = point.y;
	}

	public String toString() {
		return x + "," + y;
	}

	@Override
	public boolean equals(Object o) {
		if (o instanceof Point2D) {
			Point2D another = (Point2D) o;
			if (this.x - EPS < another.x && this.x + EPS > another.x
					&& this.y - EPS < another.y && this.y + EPS > another.y) {
				return true;
			}
			
			return false;

			// return this.x == another.x && this.y == another.y;
		}
		return false;
	}

	public Point2D add(double x, double y) {
		return new Point2D(this.x + x, this.y + y);
	}

	public Point2D sub(double x, double y) {
		return add(-x, -y);
	}

	public Point2D add(Point2D another) {
		return add(another.x, another.y);
	}

	public Point2D sub(Point2D another) {
		return sub(another.x, another.y);
	}

	public Point2D mul(double d) {
		return new Point2D(this.x * d, this.y * d);
	}

	public Point2D div(double d) {
		return new Point2D(this.x / d, this.y / d);
	}

	public double dot(double x, double y) {
		return this.x * x + this.y * y;
	}

	public double dot(Point2D another) {
		return dot(another.x, another.y);
	}

	public double cross(double x, double y) {
		return this.x * y - this.y * x;
	}

	public double cross(Point2D another) {
		return cross(another.x, another.y);
	}

	public double dist(double x, double y) {
		return Math.sqrt((this.x - x) * (this.x - x) + (this.y - y)
				* (this.y - y));
	}

	public double dist(Point2D another) {
		return dist(another.x, another.y);
	}

	public double dist_o() {
		return dist(0, 0);
	}

	public Point2D unit() {
		return div(dist_o());
	}

	public boolean pol(Point2D start, Point2D end) {
		return end.sub(start).cross(this.sub(start)) < EPS;
	}

	public boolean pos(Point2D start, Point2D end) {
		return (start.dist(this) + this.dist(end) < start.dist(end) + EPS);
	}

	public double pld(Point2D start, Point2D end) {
		return Math.abs((end.sub(start).cross(this.sub(start)))
				/ end.sub(start).dist_o());
	}

	public double psd(Point2D start, Point2D end) {
		if (end.sub(start).dot(this.sub(start)) < EPS) {
			return this.dist(start);
		} else if (start.sub(end).dot(this.sub(end)) < EPS) {
			return this.dist(end);
		} else {
			return end.sub(start).cross(this.sub(start)) / end.dist(start);
		}
	}

	public static boolean intersect_s(Point2D a1, Point2D a2, Point2D b1,
			Point2D b2) {
		return (a2.sub(a1).cross(b1.sub(a1)) * a2.sub(a1).cross(b2.sub(a1)) < EPS)
				&& (b2.sub(b1).cross(a1.sub(b1)) * b2.sub(b1).cross(a2.sub(b1)) < EPS);
	}

	public static boolean insersect_l(Point2D a1, Point2D a2, Point2D b1,
			Point2D b2) {
		return a1.sub(a2).cross(b1.sub(b2)) < EPS;
	}

	public static Point2D interpoint_s(Point2D a1, Point2D a2, Point2D b1,
			Point2D b2) {
		Point2D b = b2.sub(b1);
		double d1 = Math.abs(b.cross(a1.sub(b1)));
		double d2 = Math.abs(b.cross(a2.sub(b1)));
		double t = d1 / (d1 + d2);
		Point2D a = a2.sub(a1), v = a.mul(t);
		return a1.add(v);
	}

	public static Point2D interpoint_l(Point2D a1, Point2D a2, Point2D b1,
			Point2D b2) {
		Point2D a = a2.sub(a1);
		Point2D b = b2.sub(b1);
		double t = b.cross(b1.sub(a1)) / b.cross(a);
		Point2D v = a.mul(t);
		return a1.add(v);
	}

	public static Point2D[] cross_ss(Point2D p1, double r1, Point2D p2,
			double r2) {
		double dis = p1.dist(p2);

		if (r1 + EPS > r2 && r1 - EPS < r2 && dis < EPS) {
			return new Point2D[0]; // same
		}

		if (dis - EPS < r1 + r2 && dis + EPS > r1 + r2) {
			Point2D tmp = p2.sub(p1);
			tmp = tmp.mul(r1 / tmp.dist_o());
			Point2D ret[] = new Point2D[1];
			ret[0] = p1.add(tmp);
			return ret;
		} else if (dis + EPS > r1 + r2) {
			return new Point2D[0]; // out
		}

		double dis_m = Math.abs(r1 - r2);

		if (dis_m + EPS > dis && dis_m - EPS < dis) {
			Point2D tmp = null;
			if (r1 > r2) {
				tmp = p2.sub(p1);
			} else {
				tmp = p1.sub(p2);
			}

			double min = Math.min(r1, r2);

			tmp = tmp.mul((min + tmp.dist_o()) / tmp.dist_o());

			Point2D ret[] = new Point2D[1];
			ret[0] = p1.add(tmp);
			return ret;
		} else if (dis_m + EPS > dis) {
			return new Point2D[0]; // inner
		} else {
			Point2D ret[] = new Point2D[2];

			double theta = Math.acos((dis * dis + r1 * r1 - r2 * r2)
					/ (2 * dis * r1));
			double a = Math.atan2(p2.y - p1.y, p2.x - p1.x);

			ret[0] = new Point2D(r1 * Math.cos(a + theta) + p1.x, r1
					* Math.sin(a + theta) + p1.y);
			ret[1] = new Point2D(r1 * Math.cos(a - theta) + p1.x, r1
					* Math.sin(a - theta) + p1.y);
			return ret;
		}
	}

	public void interpoint_lc(Point2D start, Point2D end, Point2D c, double r,
			Point2D ans[]) {
		if (c.pld(start, end) > r + EPS)
			return;
		Point2D v = end.sub(start).unit();
		double delta = v.dot(start.sub(c)) * v.dot(start.sub(c))
				- start.dist(c) * start.dist(c) + r * r;
		double t = -v.dot(start.sub(c));
		double s = Math.sqrt(delta);
		ans[0] = start.add(v.mul(t + s));
		ans[1] = start.add(v.mul(t + s));
	}

	public Point2D normal_vector(Point2D p, Point2D a, Point2D b) {
		Point2D v = b.sub(a).unit();
		v = v.cross(p.sub(a)) > 0 ? new Point2D(v.y, (-1) * v.x) : new Point2D(
				(-1) * v.y, v.x);
		return v.mul(p.pld(a, b));
	}

	public static double area(Point2D a, Point2D b, Point2D c) {
		return Math.abs((c.sub(a).cross(b.sub(a))) * 0.5);
	}

}