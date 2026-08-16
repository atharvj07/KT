import java.util.*;
import java.awt.geom.*;
import java.awt.geom.Point2D.Double;

import static java.lang.Math.*;
public class Main {
	final Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		new Q2007I();
	}
	
	Point2D intersectionPoint(Line2D l1,Line2D l2){
		return intersectionPoint(l1.getP1(), l1.getP2(), l2.getP1(), l2.getP2());
	}
	Point2D intersectionPoint(Point2D a1,Point2D a2,Point2D b1,Point2D b2){
		Point2D a=diff(a2,a1),
				b=diff(b2,b1);
		return sum(a1, mul(cross(b, diff(b1,a1))/cross(b,a), a));
	}
	Point2D diff(Point2D p1,Point2D p2){
		return new Point2D.Double(p1.getX()-p2.getX(), p1.getY()-p2.getY());
	}
	double cross(Point2D p1,Point2D p2){
		return p1.getX()*p2.getY() - p2.getX()*p1.getY();
	}
	Point2D mul(double n,Point2D p1){
		return new Point2D.Double(p1.getX()*n, p1.getY()*n);
	}
	Point2D sum(Point2D p1,Point2D p2){
		return new Point2D.Double(p1.getX()+p2.getX(), p1.getY()+p2.getY());
	}
	private ArrayList<Point2D> polygonCut(ArrayList<Point2D> plist, Line2D cut) {
		int n = plist.size();
		ArrayList<Point2D> ans = new ArrayList<Point2D>();
		for(int i =0; i<n; i++){
			Point2D from = plist.get(i), to = plist.get((i+1)%n);
			if(cut.relativeCCW(from) <= 0){
				ans.add(from);
			}
			int temp1 = cut.relativeCCW(from);
			int temp2 = cut.relativeCCW(to);
			if(temp1 * temp2 < 0){
				Point2D IntersectP = intersectionPoint(cut, new Line2D.Double(from,to));
				ans.add(IntersectP);
			}
		}
		return ans;
	}
	
	class Q2007I{
		int N;
		Q2007I(){
			while(true){
				N=sc.nextInt();
				if(N==0)	break;
				solve();
			}
		}
		void solve(){
			int[] x=new int[N],
					y=new int[N];
			for(int i=0; i<N; ++i){
				x[i]=sc.nextInt();
				y[i]=sc.nextInt();
			}
			
			double ret = f1(x,y);
			System.out.printf("%.7f\n" ,ret);
			
		}
		final double EPS = 1.0e-7;
		double f1(int[] x,int[] y){
			double l=0, r=30000;
			while(abs(r-l) > EPS){
				double mid = (l+r)/2;
				ArrayList<Point2D> tmp = new ArrayList<Point2D>(N);
				for(int i=0; i<N; ++i){
					tmp.add(new Point2D.Double(x[i], y[i]));
				}
				boolean flg = f2(tmp, mid);	// true = 沈む false = 残る
				if(flg)	r=mid;
				else	l=mid;
			}
			return r;
		}
		
		boolean f2(ArrayList<Point2D> ps, double d){
			
			Line2D.Double[] cuts = new Line2D.Double[ps.size()];
			for(int i=0; i<ps.size(); ++i){
				Point2D p1 = ps.get(i),
						p2 = ps.get((i+1)%ps.size());
				double x = -(p2.getY()-p1.getY()),
						y = (p2.getX()-p1.getX());
				double d2 = p1.distance(p2);
				x = x*d/d2;	y=y*d/d2;
				Point2D v1 = new Point2D.Double(x,y);
				cuts[i] = new Line2D.Double(sum(p1, v1), sum(p2, v1));
			}
			
			for(Line2D.Double cut: cuts){
				ps = polygonCut(ps, cut);
			}
			
//			System.out.println("D:"+d+" ps:"+ps.size());
			
			return ps.isEmpty();
			
		}
	}
}