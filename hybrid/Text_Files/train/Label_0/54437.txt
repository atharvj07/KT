import java.util.*;
import java.awt.geom.*;

import static java.lang.Math.*;
public class Main {
	final Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	Main(){
		new AOJ1213();
//		System.out.println(Line2D.relativeCCW(0, 0, 0, 2, -1, 0));
	}
	
	class AOJ1213{
		Point2D[] p;
		int cnt=0;
		AOJ1213(){
			p = new Point2D[3];
			while(true){
				for(int i=0; i<3; ++i){
					p[i]=new Point2D.Double(sc.nextInt(), sc.nextInt());
				}
				if(p[0].equals(p[1]))	break;
				++cnt;
				solve();
			}
		}
		void solve(){
			ArrayList<Point2D> a = new ArrayList<Point2D>(4);
			a.add(new Point2D.Double(0,0));
			a.add(new Point2D.Double(0, 10000));
			a.add(new Point2D.Double(10000, 10000));
			a.add(new Point2D.Double(10000, 0));
			
			for(int i=1; i<=2; ++i){
				Line2D l1 = new Line2D.Double(p[0], p[i]),
						l2 = perpendicularBisector(l1);

				if( Line2D.relativeCCW(l2.getX1(), l2.getY1(), l2.getX2(), l2.getY2(), p[0].getX(), p[0].getY()) > 0){
					l2.setLine(l2.getP2(), l2.getP1());
				}

				a = polygonCut(a, l2);
			}
			
			double d=0.0;
			for(int i=0; i<a.size(); ++i){
				d += cross(a.get(i), a.get((i+1)%a.size())) / 2;
			}
			
			System.out.print(cnt+" ");
			System.out.printf("%.5f\n", abs(d) / 100000000);
		}
		final double EPS=1.0e-8;
		double cross(Point2D p1,Point2D p2){
			return p1.getX()*p2.getY() - p2.getX()*p1.getY();
		}
		double dot(Point2D p1,Point2D p2){
			return p1.getX()*p2.getX() + p1.getY()*p2.getY();
		}
		Point2D sum(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()+p2.getX(), p1.getY()+p2.getY());
		}
		Point2D add(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()+p2.getX(), p1.getY()+p2.getY());
		}
		Point2D diff(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()-p2.getX(), p1.getY()-p2.getY());
		}
		Point2D sub(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()-p2.getX(), p1.getY()-p2.getY());
		}
		Point2D mid(Line2D l1){
			return mid(l1.getP1(),l1.getP2());
		}
		Point2D mid(Point2D p1,Point2D p2){
			return new Point2D.Double((p1.getX()+p2.getX())/2, (p1.getY()+p2.getY())/2);
		}
		Point2D mul(double n,Point2D p1){
			return new Point2D.Double(p1.getX()*n, p1.getY()*n);
		}
		Line2D perpendicularBisector(Line2D l1){
			return perpendicularBisector(l1.getP1(), l1.getP2());
		}
		Line2D perpendicularBisector(Point2D p1,Point2D p2){
			Point2D mid=mid(p1,p2),
					diff=diff(p1,p2);
			return new Line2D.Double(mid, sum(mid, new Point2D.Double(diff.getY(), -diff.getX())));
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
		Point2D intersectionPoint(Line2D l1,Line2D l2){
			return intersectionPoint(l1.getP1(), l1.getP2(), l2.getP1(), l2.getP2());
		}
		Point2D intersectionPoint(Point2D a1,Point2D a2,Point2D b1,Point2D b2){
			Point2D a=diff(a2,a1),
					b=diff(b2,b1);
			return sum(a1, mul(cross(b, diff(b1,a1))/cross(b,a), a));
		}
	}
}