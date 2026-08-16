import java.awt.geom.*;
import java.util.*;
public class Main{
	double EPS = 1.0e-08;
	int INF = 1 << 24;
	//1240 start
	//1333 cording end
	//2325 restart
	//0007 sample match
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			Circle [] clist = new Circle[n];
			for(int i = 0; i < n; i++){
				Point2D p = new Point2D.Double(sc.nextInt(), sc.nextInt());
				clist[i] = new Circle(p, sc.nextInt());
			}
			
			ArrayList<Point2D> cand = new ArrayList<Point2D>();
			cand.add(clist[0].p);
			for(int i = 0; i < n-1; i++){
				Point2D [] res = intersectPtCC(clist[i], clist[i+1]);
				cand.add(res[0]);
				cand.add(res[1]);
			}
			cand.add(clist[n-1].p);
			
			int len = cand.size();
			double [][] dp = new double[len][len];
			for(int i = 0 ; i < len; i++){
				Arrays.fill(dp[i], INF);
				dp[i][i] = 0.0;
			}
			for(int i = 0; i < len; i++){
				for(int j = i + 1; j < len; j++){
					boolean isOK = true;
					Line2D m = new Line2D.Double(cand.get(i), cand.get(j));
					for(int k = j - 2; k > i; k -= 2){
						Line2D l;
						if(k % 2 == 0){
							l = new Line2D.Double(cand.get(k-1), cand.get(k));
						}
						else{
							l = new Line2D.Double(cand.get(k), cand.get(k + 1));
						}
						if(! m.intersectsLine(l)){
							isOK = false;
							break;
						}
					}
					if(isOK){
						dp[i][j] = cand.get(i).distance(cand.get(j));
						dp[j][i] = cand.get(i).distance(cand.get(j));
					}
				}
			}
			
			for(int j = 0; j < len; j++){
				for(int i = 0; i < len; i++){
					for(int k = 0; k < len; k++){
						dp[i][k] = Math.min(dp[i][k], dp[i][j] + dp[j][k]);
					}
				}
			}
			System.out.printf("%.6f\n",dp[0][len-1]);
		}
	}
	
	public class Circle{
		Point2D p;
		double r;
		public Circle(Point2D p, double r) {
			this.p = p; this.r = r;
		}
	}
	
	//円と円の交点
	Point2D [] intersectPtCC(Circle a,Circle b) {
		double dis = a.p.distance(b.p);
		Point2D v = sub(b.p, a.p);
		double rc = (dis * dis + a.r * a.r - b.r * b.r) / (2 * dis);
		double rate = rc / dis;
		v = mul(v, rate);
		Point2D c = add(v, a.p);
		double disC2c = c.distance(b.p);
		double disqc = Math.sqrt(b.r * b.r - disC2c * disC2c);
		Point2D v2 = sub(b.p, c);
		v2 = mul(v2, disqc / disC2c);
		Point2D [] res = new Point2D[2];
		res[0] = add(normalV1(v2), c);
		res[1] = add(normalV2(v2), c);
		return res;
	}
	
	private Point2D normalV1(Point2D p) {
		return new Point2D.Double(-p.getY(), p.getX());
	}
	
	private Point2D normalV2(Point2D p) {
		return new Point2D.Double(p.getY(), -p.getX());
	}

	private Point2D add(Point2D p1, Point2D p2) {
		double x = p1.getX() + p2.getX();
		double y = p1.getY() + p2.getY();
		return new Point2D.Double(x,y);
	}

	private Point2D mul(Point2D v, double rate) {
		return new Point2D.Double(v.getX() * rate, v.getY() * rate);
	}

	private Point2D sub(Point2D p1, Point2D p2) {
		double x = p1.getX() - p2.getX();
		double y = p1.getY() - p2.getY();
		return new Point2D.Double(x,y);
	}
	
	public static void main(String [] args){
		new Main().doit();
	}
}