import java.util.*;
import static java.lang.Math.*;

public class Main {

	class Point{
		double x, y;
		Point(double _x, double _y){ this.x = _x; this.y = _y; }
		Point(){ new Point(0,0); }
		double abs(){ return hypot(this.x,this.y); }
		Point rot(double th){ 
			return new Point(x*cos(th)-y*sin(th),x*sin(th) + y*cos(th));
		}
		Point rotAt(Point a, double th){
			Point t = this.sub(a);
			t = t.rot(th);
			return t.add(a);
		}
		Point sub(Point a){
			return new Point(this.x-a.x, this.y-a.y);
		}
		Point add(Point a){
			return new Point(this.x+a.x, this.y+a.y);
		}
		Point multi(double a){
			return new Point(a*this.x, a*this.y);
		}
		Point div(double a){
			return new Point(this.x/a, this.y/a);
		}
	}
	
	Point left, right;

	void run(){
		Scanner in = new Scanner(System.in);
		for(;;){
			int N = in.nextInt();
			double D = in.nextDouble();
			if(N==0 && D==0) return;
			left = new Point(-D,0);
			right = new Point(D,0);
			for(int i=0; i<N; i++){
				double  lv= in.nextDouble(),
						rv = in.nextDouble(),
						time = in.nextDouble();
				proc(lv*PI/180*time,rv*PI/180*time);
			}
			Point center = right.add(left).div(2.0);
			System.out.printf("%.7f\n%.7f\n",center.x+1e-9, center.y+1e-9);
		}
	}
	
	void proc(double lv, double rv){
		if(lv == rv){
			Point v = right.sub(left).rot(PI/2.0);
			v = v.multi(lv/v.abs());
			left = left.add(v);
			right = right.add(v);
			return ;
		}
		Point center = left.multi(-rv).add(right.multi(lv)).div(lv-rv);
		boolean leftIsNear = left.sub(center).abs() < right.sub(center).abs();
		if(lv!=0)left = left.rotAt(center, (lv*rv<0?-1:leftIsNear?1:-1)*lv/center.sub(left).abs());
		if(rv!=0)right = right.rotAt(center, (lv*rv<0?1:leftIsNear?1:-1)*rv/center.sub(right).abs());
		return;
	}

	public static void main(String args[]){
		new Main().run();
	}
}