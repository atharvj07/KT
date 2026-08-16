//Referred Dukkha's Code
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class CoveredPoints {
	static class Segment{
		int x1, y1, x2, y2;
		Segment(int x1, int y1, int x2, int y2){
			this.x1=x1;
			this.y1=y1;
			this.x2=x2;
			this.y2=y2;
		}
	}
	static long crossProduct(long x1, long y1, long x2, long y2)
	{
	 return x1*y2-x2*y1; 
	}
	
	static class Point{
		int x1, y1, z;
		Point(int x1, int y1, int z){
			this.x1=x1;
			this.y1=y1;
			this.z=z;
		}
	}
	static boolean check(long a, long b) {
		if(b<0) {
			a=-a;
			b=-b;
		}
		return a>=0 && a<=b;
	}
	static int xi, yi;
	static boolean checkIntersection(int px, int py, int qx, int qy, int rx, int ry, int sx, int sy) {
		long rs = crossProduct(rx, ry, sx, sy);
		long pqs = crossProduct(qx-px, qy-py, sx, sy);
		long pqr = crossProduct(qx-px, qy-py,rx,ry);
		//intersection condition
		if(rs==0||!check(pqs,rs)||!check(pqr,rs))
			return false;
		long z = GCD(pqs,rs);
		long a =pqs/z;
		long b =rs/z;
		if(rx%b!=0||ry%b!=0) {
			return false;
		}
		xi=(int)(px+rx/b*a);
		yi=(int)(py+ry/b*a);
		//System.out.println(xi+" "+yi);
		return true;
	}
    static boolean areIntersecting(Segment p, Segment q) {
    	int px = p.x1;
    	int py = p.y1;
    	int qx = q.x1;
    	int qy = q.y1;
    	int rx = p.x2-p.x1;
    	int ry = p.y2-p.y1;
    	int sx = q.x2-q.x1;
    	int sy = q.y2-q.y1;
		return checkIntersection(px,py,qx,qy,rx,ry,sx,sy);
	}
	
	
	static long GCD(long a , long b) {
		return b==0?a:GCD(b,a%b);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Segment[] segments = new Segment[n]; 
		for(int i=0;i<n;i++) {
			Segment s = new Segment(sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextInt());
			segments[i]=s;
		}
		/*
		 * for(int i=0;i<n;i++) { System.out.println(segments[i].x1+" "+
		 * segments[i].y1+" "+segments[i].x2+" "+segments[i].y2); }
		 */
		long count=0;
		for(int i=0;i<n;i++) {
			Segment s = segments[i];
			count +=GCD(Math.abs(s.x2-s.x1), Math.abs(s.y2-s.y1))+1;
		}
		//System.out.println(count);
		ArrayList<Point> ipoints = new ArrayList<Point>();
		for(int i=0; i<n;i++) {
			Segment p = segments[i];
			for(int j=i+1;j<n;j++) {
				Segment q = segments[j];
				if(areIntersecting(p,q)) {
					ipoints.add(new Point(xi,yi,i));
					ipoints.add(new Point(xi,yi,j));
				}
			}
		}
		
		
		Collections.sort( ipoints, new Comparator<Point>() {
		       public int compare(Point x1, Point x2) {
		         int result = Long.compare(x1.x1, x2.x1);
		         if ( result == 0 ) {
		             result = Long.compare(x1.y1, x2.y1);
		           } 
		         if(result == 0) {
		        	 result = Long.compare(x1.z, x2.z);
		         }
		         return result;
		      }
		    });
		
		int l = ipoints.size();
		//System.out.println(l);
		Point[] pp = ipoints.toArray(new Point[l]);
		
		// System.out.println("");
		  for(int i=0;i<l;i++) {
	  //  System.out.println(pp[i].x1+" "+pp[i].y1+" "+pp[i].z);
		  }
		 
		for(int i=0,j; i<l; i=j) {
			int x1 =pp[i].x1;
			int y1 =pp[i].y1;
			j=i;
			while(j<l&&pp[j].x1==x1&&pp[j].y1==y1) 
				j++;
			int temp=0;
			for(int h=i;h<j;h++) {
				if(h==i||pp[h].z !=pp[h-1].z) {
					temp++;
				}
			}
			count-=temp-1;
			
		}
		System.out.println(count);
	}
}