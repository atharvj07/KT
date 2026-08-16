
import java.util.*;

class Main {
	Scanner sc = new Scanner(System.in);

	public void run() {
		while(sc.hasNext()){
			P p1=new P(sc.nextDouble(),sc.nextDouble());
			P p2=new P(sc.nextDouble(),sc.nextDouble());
			P p3=new P(sc.nextDouble(),sc.nextDouble());
			P px=new P(sc.nextDouble(),sc.nextDouble());
			
			if(P.ccw(p1,p2,px)*P.ccw(p2,p3,px)>=0
			&&P.ccw(p2,p3,px)*P.ccw(p3,p1,px)>=0	
			&&P.ccw(p3,p1,px)*P.ccw(p1,p2,px)>=0
				){
				ln("YES");
			}else{
				ln("NO");
			}
		}
	}
	public static String join(double[] array, String separator) {
		StringBuilder str = new StringBuilder(array[0] + "");
		for (int i = 1; i < array.length; i++) {
			str.append(separator).append(array[i] + "");
		}
		return str.toString();
	}

	
	
	public static void main(String[] args) {
		new Main().run();
	}

	public static void pr(Object o) {
		System.out.print(o);
	}

	public static void ln(Object o) {
		System.out.println(o);
	}

	public static void ln() {
		System.out.println();
	}
}


class P{
	double x;
	double y;
	P(double _x,double _y){
		x=_x;
		y=_y;
	}
	
	public static double dot(P a,P b){
			return a.x*b.x+a.y*b.y;
	}
	public static  double cross(P a,P b){
		return a.x*b.y-a.y*b.x;
	}
	public P a(P a){
		return new P(x+a.x,y+a.y);
	}
	public P s(P a){
		return new P(x-a.x,y-a.y);
	}
	
	public double norm(){
		return Math.sqrt(x*x+y*y);
	}
	
	public static int ccw(P a,P b,P c){
		if(P.cross(b.s(a),c.s(a))>Double.MIN_NORMAL){
			return 1;
		}
		if(P.cross(b.s(a),c.s(a))<-Double.MIN_NORMAL){
			return -1;
		}
		if(P.dot(b,c)<-Double.MIN_NORMAL)return 2;
		if(b.norm()<c.norm()-Double.MIN_NORMAL)return -2;
		return 0;
	}
}