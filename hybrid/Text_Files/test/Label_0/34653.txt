//Referred Dukkha's code 
 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;
 
public class ConvexHull {
 
	private static class Point{
		int x; int y;
		Point(int x, int y){
			this.x=x;
			this.y=y;
		}
	}
	private static long crossProduct(Point a, Point b, Point c) {
		return (long)(a.x-b.x)*(b.y-c.y) - (long)(b.x-c.x)*(a.y-b.y);
	}
 
	/*
	 * private static boolean isUpper(Point p, Point a, Point b ) {
	 * if(a==null||b==null||crossProduct(p,a,b)>0||a==b&&p.y>b.y){ return true; }
	 * return false; } private static boolean isLower(Point p, Point c, Point d) {
	 * 
	 * if(c==null||d==null||crossProduct(p,c,d)<0||c==d&&p.y<d.y) { return true; }
	 * return false; }
	 */
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	//	Scanner sc = new Scanner(System.in);
		int q = Integer.parseInt(br.readLine());
		TreeSet<Point> u = new TreeSet<>((p1,p2)->p1.x-p2.x);
		TreeSet<Point> l = new TreeSet<>((p1,p2)->p1.x-p2.x);
		while(q-- > 0){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			Point p = new Point(x,y);
			Point a = u.ceiling(p);
			Point b = u.floor(p);
			Point c = l.ceiling(p);
			Point d = l.floor(p);
			//checking if the point is outside the hull
			boolean upper = false;
			if(a==null||b==null||a==b&&p.y>b.y||crossProduct(p,b,a)>0)
				upper =true;
			boolean lower = false;
			if(c==null||d==null||c==d&&p.y<d.y||crossProduct(p,d,c)<0) 
				lower = true;
			if(t==2)
				System.out.println(upper||lower?"NO":"YES");
			//Updating the convex hull after every point if there is a need to change the hull 
			else {
				if(upper) {
					removeLeft(u, p,1);
					removeRight(u, p, 1);
					u.add(p);
				}
				if(lower) {
					removeLeft(l,p,-1);
					removeRight(l, p, -1);
					l.add(p);
				}
			}	
		}
	}
	private static void removeLeft(TreeSet<Point> u, Point p, int i) {
		Point low = u.floor(p);
 
		if(low==null) {
			return;
		}
		if(p.x==low.x) {
			u.remove(low);
			low = u.floor(p);
		}
		if(low==null) {
			return;
		}
		Point low1 = u.lower(low);
		while(low1!=null&&crossProduct(low,low1,p)*i<=0) {
			u.remove(low);
			low=low1;
			low1 = u.lower(low);
		}
	}
	private static void removeRight(TreeSet<Point> u, Point p, int i) {
 
		Point high = u.ceiling(p);
 
		if(high==null) {
			return;
		}
		if(p.x==high.x) {
			u.remove(high);
			high = u.ceiling(p);
		}
		if(high==null) {
			return;
		}
		Point high1 = u.higher(high);
		while(high1!=null&&crossProduct(high,high1,p)*i>=0) {
			u.remove(high);
			high =high1;
			high1=u.higher(high);
		}
	}
}