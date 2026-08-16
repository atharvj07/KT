import java.util.*;
import java.awt.geom.*;
import java.awt.geom.Line2D.Double;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int n = sc.nextInt();
			if(n==0) break;
			
			double sx = sc.nextDouble();
			double sy = sc.nextDouble();
			double ex = sc.nextDouble();
			double ey = sc.nextDouble();
			
			Line2D.Double se = new Line2D.Double(sx,sy,ex,ey);
			Line2D.Double[] q = new Line2D.Double[4];
			Point2D.Double[] p = new Point2D.Double[4];
			double ans = Integer.MAX_VALUE;
			boolean flag = false;
			for(int i=0;i<n;i++){
				double minx = sc.nextDouble();
				double miny = sc.nextDouble();
				double maxx = sc.nextDouble();
				double maxy = sc.nextDouble();
				double h = sc.nextDouble();
				if(flag==false){
					p[0] = new Point2D.Double(minx,miny);
					p[1] = new Point2D.Double(maxx,miny);
					p[2] = new Point2D.Double(maxx,maxy);
					p[3] = new Point2D.Double(minx,maxy);
					q[0] = new Line2D.Double(p[0],p[1]);
					q[1] = new Line2D.Double(p[1],p[2]);
					q[2] = new Line2D.Double(p[2],p[3]);
					q[3] = new Line2D.Double(p[3],p[0]);
					
					if(minx<=sx && sx<=maxx && miny<=sy && sy<=maxy && minx<=ex && ex<=maxx && miny<=ey && ey<=maxy) flag = true;
					double min = Integer.MAX_VALUE;
					for(int j=0;j<4;j++){
						if(se.intersectsLine(q[j])==true) flag = true;
						min = Math.min(min, se.ptSegDist(p[j]));
						min = Math.min(min, q[j].ptSegDist(sx,sy));
						min = Math.min(min, q[j].ptSegDist(ex,ey));
					}
					if(h>min) ans = Math.min(ans, min);
					else ans = Math.min(ans, (min*min+h*h)/(2*h));
				}
			}
			
			if(flag==true) System.out.println(0);
			else System.out.println(ans);
		}	
	}	
}