import java.util.Arrays;
import java.util.Random;

//The Closest Circle
public class Main{

	class Scanner {
		int nextInt() {
			try {
				int c = System.in.read();
				while (c != '-' && (c < '0' || '9' < c))
					c = System.in.read();
				if (c == '-') return -nextInt();
				int res = 0;
				do {
					res *= 10;
					res += c - '0';
					c = System.in.read();
				} while ('0' <= c && c <= '9');
				return res;
			} catch (Exception e) {
				return -1;
			}
		}
		double nextDouble() {
			return Double.parseDouble(next());
		}
		String next() {
			try {
				StringBuilder res = new StringBuilder("");
				int c = System.in.read();
				while (Character.isWhitespace(c))
					c = System.in.read();
				do {
					res.append((char) c);
				} while (!Character.isWhitespace(c = System.in.read()));
				return res.toString();
			} catch (Exception e) {
				return null;
			}
		}
	}
	
	class R implements Comparable<R>{
		double x, y, r;
		public R(double x, double y, double r) {
			this.x = x;
			this.y = y;
			this.r = r;
		}
		public int compareTo(R o) {
			if(Math.abs(x-o.x)<EPS)return (int)Math.signum(y-o.y);
			return (int)Math.signum(x-o.x);
		}
	}
	
	double EPS = 1e-8;
	
	void run(){
		Scanner sc = new Scanner();
		Random rand = new Random(System.currentTimeMillis());
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			int rot = rand.nextInt(44)+1;
			double sin = Math.sin(rot*Math.PI/180), cos = Math.cos(rot*Math.PI/180);
			R[] rs = new R[n];
			for(int i=0;i<n;i++){
				double r = sc.nextDouble(), x = sc.nextDouble(), y = sc.nextDouble();
				rs[i] = new R(cos*x-sin*y, sin*x+cos*y, r);
			}
			Arrays.sort(rs);
			double res = 1L<<60;
			for(int i=0;i<n;i++){
				int t = Math.min(n, i+50);
				for(int j=i+1;j<t;j++){
					res = Math.min(res, Math.sqrt((rs[i].x-rs[j].x)*(rs[i].x-rs[j].x) + (rs[i].y-rs[j].y)*(rs[i].y-rs[j].y))-rs[i].r-rs[j].r);
				}
			}
			System.out.printf("%.9f\n", res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}