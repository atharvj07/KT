import java.awt.geom.*;
import java.util.*;
public class Main {
	
	//外積
	private double cross(Point2D p1, Point2D p2) {
		double res = p1.getX() * p2.getY() - p1.getY() * p2.getX();
		return res;
	}
	
	private double area(ArrayList<Point2D> polygon) {
		double res = 0.0;
		int n = polygon.size();
		for(int i = 0; i < n; i++){
			Point2D from = polygon.get(i), to = polygon.get((i+1) % n);
			res += cross(from, to);
		}
		return Math.abs(res) / 2.0;
	}

	private void doit() {
		Scanner sc = new Scanner(System.in);
		int count = 0;
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			ArrayList<Point2D> polygon = new ArrayList<Point2D>();
			for(int i = 0; i < n; i++){
				double x = sc.nextDouble();
				double y = sc.nextDouble();
				polygon.add(new Point2D.Double(x, y));
			}
			System.out.printf("%d %.1f\n",++count, area(polygon));
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}