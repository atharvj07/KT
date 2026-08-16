import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Zyflair Griffane
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		PandaScanner in = new PandaScanner(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		D solver = new D();
		solver.solve(1, in, out);
		out.close();
	}
}

class D {
    public void solve(int testNumber, PandaScanner in, PrintWriter out) {
        int tt = in.nextInt();
        while (tt --> 0) {
            Vector2D a = new Vector2D(in.nextInt(), in.nextInt());
            Vector2D b = new Vector2D(in.nextInt(), in.nextInt());
            Vector2D c = new Vector2D(in.nextInt(), in.nextInt());

            Vector2D[] quad = make(a, b, c);
            if (quad != null) {
                out.println("YES");
                out.println(quad[0].x + " " + quad[0].y + " " + quad[1].x + " " + quad[1].y + " " + quad[2].x + " " + quad[2].y + " " + quad[3].x + " " + quad[3].y);
                continue;
            }
            quad = make(b, a, c);
            if (quad != null) {
                out.println("YES");
                out.println(quad[0].x + " " + quad[0].y + " " + quad[1].x + " " + quad[1].y + " " + quad[2].x + " " + quad[2].y + " " + quad[3].x + " " + quad[3].y);
                continue;
            }
            quad = make(c, b, a);
            if (quad != null) {
                out.println("YES");
                out.println(quad[0].x + " " + quad[0].y + " " + quad[1].x + " " + quad[1].y + " " + quad[2].x + " " + quad[2].y + " " + quad[3].x + " " + quad[3].y);
                continue;
            }
            out.println("NO");
            out.println();
        }
    }
    public Vector2D[] make(Vector2D m, Vector2D a, Vector2D b) {
        Vector2D c = m.scale(2).sub(a);
        Circle cir = Circle.constructCircle(b, m, c);
        if (cir == null) return null;
        Vector2D A = cir.center;
        Vector2D B = A.add(m.sub(A).scale(2));
        Vector2D C = B.add(a.sub(B).scale(2));
        Vector2D D = A.add(b.sub(A).scale(2));
        Vector2D[] quad = new Vector2D[] { A, B, C, D };
        if (Util.convex(quad)) {
            return quad;
        }
        return null;
    }
}

class PandaScanner {
    public BufferedReader br;
    public StringTokenizer st;
    public InputStream in;

    public PandaScanner(InputStream in) {
        br = new BufferedReader(new InputStreamReader(this.in = in));
    }

    public String nextLine() {
        try {
            return br.readLine();
        }
        catch (Exception e) {
            return null;
        }
    }

    public String next() {
        if (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(nextLine().trim());
            return next();
        }
        return st.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
}

class Vector2D {
    public static final double EPS = 1e-9;

    public final double x;
    public final double y;

    public Vector2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Vector2D add(Vector2D o) {
        return new Vector2D(x + o.x, y + o.y);
    }

    public double cross(Vector2D o) {
        return x * o.y - y * o.x;
    }

    public double dist(Vector2D o) {
        return sub(o).mag();
    }

    public double mag() {
        return Math.sqrt(x * x + y * y);
    }

    public Vector2D normalize() {
        double m = mag();
        if (m == 0) {
            return new Vector2D(0, 0);
        }
        return new Vector2D(x / m, y / m);
    }

    public boolean parallel(Vector2D o) {
        return Math.abs(cross(o)) <= EPS;
    }

    public Vector2D perp() {
        return new Vector2D(-y, x);
    }

    public Vector2D scale(double s) {
        return new Vector2D(x * s, y * s);
    }

    public Vector2D sub(Vector2D o) {
        return new Vector2D(x - o.x, y - o.y);
    }

    public String toString() {
        return "(" + x +", " + y + ")";
    }
}

class Circle {

    public double radius;
    public Vector2D center;

    public Circle(Vector2D center, double radius) {
        this.center = center;
        this.radius = radius;
    }

    public static Circle constructCircle(Vector2D a, Vector2D b, Vector2D c) {
        if ((a.x == b.x && a.y == b.y) || (a.x == c.x && a.y == c.y) || (b.x == c.x && b.y == c.y)) {
            return null;
        }
        Seg AB = new Seg(a, b);
        Seg AC = new Seg(a, c);
        Vector2D mAB = AB.midpoint();
        Vector2D mAC = AC.midpoint();
        Line pbAB = new Line(mAB, mAB.add(AB.dir.perp()));
        Line pbAC = new Line(mAC, mAC.add(AC.dir.perp()));
        Vector2D center = pbAB.intersection(pbAC);
        if (center == null) {
            return null;
        }
        return new Circle(center, center.dist(a));
    }
}

class Util {

    public static final double EPS = 1e-9;

    public static boolean convex(Vector2D[] p)
    {
        int n = p.length;
        if(n <= 2) return false;

        double sign = p[1].sub(p[0]).cross(p[2].sub(p[0]));
        if(Math.abs(sign) < EPS) return false;

        if(sign > EPS) sign = 1;
        else sign = -1;
        for(int i = 1; i < n; i++)
        {
            double cur = p[(i + 1) % n].sub(p[i]).cross(p[(i + 2) % n].sub(p[i]));
            if(cur * sign < EPS) return false;
        }
        return true;
    }
}

class Seg {

    Vector2D origin;
    Vector2D dir;
    double length;

    public Seg(Vector2D v1, Vector2D v2) {
        origin = v1;
        dir = v2.sub(v1);
        length = dir.mag();
        dir = dir.normalize();
    }

    public Vector2D midpoint() {
        return origin.add(dir.scale(length / 2.0));
    }
}

class Line {

    Vector2D origin;
    Vector2D dir;

    public Line(Vector2D v1, Vector2D v2) {
        origin = v1;
        dir = v2.sub(v1);
        dir = dir.normalize();
    }

    public Vector2D intersection(Line o) {
        if (dir.parallel(o.dir)) {
            return null;
        }
        double c = dir.cross(o.dir);
        Vector2D d = o.origin.sub(origin);
        double t = d.cross(o.dir) / c;
        double u = d.cross(dir) / c;
        return origin.add(dir.scale(t));
    }
}

