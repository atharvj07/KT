import java.awt.geom.Point2D;
import java.util.*;

public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}

	public Main() {
		new AOJ0090().doIt();
	}

	class AOJ0090{
		void doIt(){
			final double EPS=1.0e-8;
			while(true){
				int n = in.nextInt();
				if(n==0)break;
				ArrayList<Point2D> p = new ArrayList<Point2D>();
				ArrayList<Point2D> list = new ArrayList<Point2D>();
				for(int i=0;i<n;i++){
					String res[] = in.next().split(",");
					p.add(new Point2D.Double(Double.parseDouble(res[0]),Double.parseDouble(res[1])));
				}
				for(int i=0;i<n;i++)for(int s=i+1;s<n;s++){
					Point2D[] a = intersectPtCC(new Circle(p.get(i),1),new Circle(p.get(s),1));
					if(a==null)continue;
					list.add(a[0]);list.add(a[1]);
				}
				int result = 1;
				for(int i=0;i<list.size();i++){
					int cnt = 0;
					for(int s=0;s<n;s++){
						if(list.get(i).distanceSq(p.get(s))<=(1+EPS)*(1+EPS))cnt++;
					}
					result = Math.max(result, cnt);
				}
				System.out.println(result);
			}
		}

		class Circle{
			Point2D p;
			double r;
			Circle(Point2D p,double r){ 
				this.p=p;
				this.r=r;
			}
			Circle(double x,double y,double r){  
				this.p=new Point2D.Double(x,y); 
				this.r=r;
			}
		}
		 //円と円の交点
		Point2D [] intersectPtCC(Circle a,Circle b){
		double dis = a.p.distance(b.p);
		if(dis > a.r + b.r)return null;
		Point2D v = sub(b.p, a.p);
		double rc=(dis*dis+a.r*a.r- b.r*b.r)/(2*dis);
		double rate = rc / dis;
		v = mul(rate, v);
		Point2D c = add(v, a.p);
		double disC2c = c.distance(b.p);
		double disqc = Math.sqrt(b.r * b.r - disC2c * disC2c);
		Point2D v2 = sub(b.p, c);
		v2 = mul(disqc / disC2c, v2);
		Point2D [] res = new Point2D[2];
		res[0] = add(normalVector1(v2), c);
		res[1] = add(normalVector2(v2), c);
		return res;
		}

		Point2D normalVector1(Point2D p){
			return new Point2D.Double(-p.getY(), p.getX());
		}
		Point2D normalVector2(Point2D p){
			return new Point2D.Double(p.getY(), -p.getX());
		}
		Point2D mul(double n,Point2D p1){
			return new Point2D.Double(p1.getX()*n,p1.getY()*n);
		}
		Point2D sub(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()-p2.getX(),p1.getY()-p2.getY());
		}
		Point2D add(Point2D p1,Point2D p2){
			return new Point2D.Double(p1.getX()+p2.getX(), p1.getY()+p2.getY());
		}
	}
}