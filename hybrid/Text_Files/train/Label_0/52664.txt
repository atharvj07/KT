import java.awt.geom.*;
import java.util.*;


public class Main {
	
	double EPS = 1.0e-08;
	
	//0649 start
	//0710 sstop
	public class Point3D{
		double x,y,z;
		public Point3D(double x, double y, double z) {
			this.x = x;this.y = y;this.z = z;
		}
		
		private double dot(Point3D p){
			return this.x*p.x+this.y*p.y+this.z*p.z;
		}
		
		private double norm(){
			return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z);
		}
		//３次元ベクトルの角度
		private double angle(Point3D p2){
			double a = this.dot(p2);
			double b = this.norm();
			double c = p2.norm();
			return Math.acos(a/(b*c));
		}
	}
	Point3D [] mlist;
	double [] mrad;

	private void doit() {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			Point3D [] stars = new Point3D[n];
			for(int i = 0; i < n; i++){
				stars[i] = new Point3D(sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
			}
			int m = sc.nextInt();
			mlist = new Point3D[m];
			mrad = new double[m];
			for(int i = 0; i < m; i++){
				mlist[i] = new Point3D(sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
				mrad[i] = sc.nextDouble();
			}
			
			int ans = 0;
			for(int i = 0; i < n; i++){
				boolean isfind = false;
				isfind = findStar(stars[i]);
				if(isfind){
					ans++;
				}
			}
			System.out.println(ans);
		}
		
	}

	private boolean findStar(Point3D p) {
		int len = mlist.length;
		for(int i = 0; i < len; i++){
			double mRad = mrad[i];
			double nRad = p.angle(mlist[i]);
//			System.out.println("nrad = " + nRad);
//			System.out.println("mrad = " +mRad);
			if(mRad + EPS> nRad){
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}