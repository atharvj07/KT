import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import static java.lang.Math.sin;
import static java.lang.Math.cos;
import static java.lang.Math.toRadians;

public class Main {

  private static StringBuilder buf = new StringBuilder();

  public static void main(String[] args) throws IOException {
    
    try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

      int n = Integer.parseInt( br.readLine() );
      Point2D p1 = new Point2D(0,0);
      Point2D p2 = new Point2D(100, 0);

      calcKochCurve(n, p1, p2);
      System.out.print(buf);
      
    }
  }

  private static void calcKochCurve(int d, Point2D p1, Point2D p2) {
    double rad = toRadians(60);

    buf.append(p1);
    kochCurve( d, p1, p2, rad );
    buf.append(p2);
  } 

  private static void kochCurve(int d, Point2D p1, Point2D p2, double rad) {
    if( d != 0) {
      Point2D s = new Point2D();
      Point2D t = new Point2D();

      s.x = (2*p1.x + p2.x) / 3;
      s.y = (2*p1.y + p2.y) / 3;
      t.x = (p1.x + 2*p2.x) / 3;
      t.y = (p1.y + 2*p2.y) / 3;

      Point2D u = new Point2D();

      u.x = (t.x - s.x)*cos(rad) - (t.y - s.y)*sin(rad) + s.x;
      u.y = (t.x - s.x)*sin(rad) + (t.y - s.y)*cos(rad) + s.y;

      kochCurve(d-1, p1, s, rad);
      buf.append(s);
      kochCurve(d-1, s, u, rad);
      buf.append(u);
      kochCurve(d-1, u, t, rad);
      buf.append(t);
      kochCurve(d-1, t, p2, rad);
    }
  }
}

class Point2D {
  double x;
  double y;

  public Point2D() { }
  public Point2D(double x,double y) {
    this.x = x;
    this.y = y;
  }

  @Override
  public String toString() {
    return String.format("%.8f %.8f\n", x, y);
  }
  public double distance(Point2D p) {
    return Math.sqrt(Math.pow((p.x - this.x),2) + Math.pow((p.y - this.y), 2));
  }
}
