import java.util.*;
import java.awt.geom.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(true){
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			if(x1==0 && y1==0) break;
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			int x3 = sc.nextInt();
			int y3 = sc.nextInt();
			int x4 = sc.nextInt();
			int y4 = sc.nextInt();
			double maxx = Math.max(Math.max(x1,x2), x3);
			double maxy = Math.max(Math.max(y1,y2), y3);
			double minx = Math.min(Math.min(x1,x2), x3);
			double miny = Math.min(Math.min(y1,y2), y3);			
			Point2D.Double p1 = new Point2D.Double(x1,y1);
			Point2D.Double p2 = new Point2D.Double(x2,y2);
			Point2D.Double p3 = new Point2D.Double(x3,y3);
			Point2D.Double p4 = new Point2D.Double(x4,y4);
			Line2D.Double a = new Line2D.Double(p2,p3);
			Line2D.Double b = new Line2D.Double(p3,p1);
			Line2D.Double c = new Line2D.Double(p1,p2);
			double r = sc.nextDouble();

			if(p4.distance(p1)<=r && p4.distance(p2)<=r && p4.distance(p3)<=r){
				System.out.println("b");
			}else if(a.ptSegDist(p4)>=r && b.ptSegDist(p4)>=r && c.ptSegDist(p4)>=r){
				Line2D.Double da = new Line2D.Double(p1,p4);
				Line2D.Double db = new Line2D.Double(p2,p4);
				Line2D.Double dc = new Line2D.Double(p3,p4);
				if(minx<x4 && x4<maxx && miny<y4 && y4<maxy && a.intersectsLine(da)==false
						&& b.intersectsLine(db)==false && c.intersectsLine(dc)==false){
					System.out.println("a");
				}else{
					if(a.ptSegDist(p4)==r || b.ptSegDist(p4)==r || c.ptSegDist(p4)==r){
						System.out.println("c");
					}else{
						System.out.println("d");
					}
				}
			}else{
				System.out.println("c");
			}
		}
	}
}