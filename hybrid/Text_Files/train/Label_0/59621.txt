import java.util.*;
import java.awt.geom.*;
public class Main {
	double EPS = 1.0e-08;
	
	private void doit() {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int M = sc.nextInt()-1;
			int L = sc.nextInt()-1;
			if(n == 0 && M == -1 && L == -1) break;
			Point2D [][] point = new Point2D.Double[n][5];
			Line2D [][] line = new Line2D.Double[n][5];
			//input
			for(int i=0; i < n; i++){
				double x = sc.nextDouble();
				double y = sc.nextDouble();
				double a = sc.nextDouble();
				double r = sc.nextDouble();
				//each point
				for(int j=0; j < 5; j++){
					double rad = Math.toRadians(-a + (double)j * 72);
					double endx = x + r * Math.sin(rad);
					double endy = y + r * Math.cos(rad);
					point[i][j] = new Point2D.Double(endx, endy);
				}
				//each line
				for(int j=0; j < 5; j++){
					line[i][j] = new Line2D.Double(point[i][j] , point[i][(j+2)%5]);
				}
			}
			double [][] pass = new double[n][n];
			//calc
			for(int i=0; i < n; i++){
				pass[i][i] = 0.0;
				for(int j=i+1; j< n; j++){
					double ans = 1 << 24;
					for(int k = 0; k < 5; k++){
						for(int l = 0; l < 5; l++){
							Line2D nowi = line[i][k];
							Line2D nowj = line[j][l];
							if(nowi.intersectsLine(nowj)){
								ans = 0.0;
								continue;
							}
							double res = getDis1(nowi,nowj);
							ans = Math.min(ans, res);
						}
					}
					pass[i][j] = ans; pass[j][i] = ans;
				}
			}//end i
			
			
			for(int j=0; j < n; j++){
				for(int i = 0;i < n; i++){
					for(int k = 0; k < n; k++){
						pass[i][k] = Math.min(pass[i][k], pass[i][j] + pass[j][k]);
					}
				}
			}
			System.out.printf("%1.16f\n",pass[M][L]);
		}
	}

	private double getDis1(Line2D a, Line2D b) {
		Point2D a1 = a.getP1();
		Point2D a2 = a.getP2();
		Point2D b1 = b.getP1();
		Point2D b2 = b.getP2();
		double res = getD(a1,a2,b1);
		res = Math.min(res, getD(a1,a2,b2));
		res = Math.min(res, getD(b1,b2,a1));
		res = Math.min(res, getD(b1,b2,a2));
		return res;
	}

	private double getD(Point2D a, Point2D b, Point2D c) {
		Point2D ba = getV(b,a);
		Point2D ca = getV(c,a);
		Point2D ab = getV(a,b);
		Point2D cb = getV(c,b);
		double result;
		if(getDot(ba,ca) < EPS){
			result = a.distance(c);
		}
		else if(getDot(ab,cb) < EPS){
			result = c.distance(b);
		}
		else{
			result = Math.abs(getCross(ba,ca)) / b.distance(a);
		}
		return result;
	}

	private double getCross(Point2D a, Point2D b) {
		return (a.getX() * b.getY() - a.getY() * b.getX());
	}

	private double getDot(Point2D a, Point2D b) {
		return (a.getX() * b.getX() + a.getY() * b.getY());
	}

	private Point2D getV(Point2D a, Point2D b) {
		Point2D res = new Point2D.Double(a.getX() - b.getX(), a.getY() - b.getY());
		return res;
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}