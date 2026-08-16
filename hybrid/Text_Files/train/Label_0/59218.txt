import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class D {
	
	static class Scanner{
		BufferedReader br=null;
		StringTokenizer tk=null;
		public Scanner(){
			br=new BufferedReader(new InputStreamReader(System.in));
		}
		public String next() throws IOException{
			while(tk==null || !tk.hasMoreTokens()) {
				String cad = br.readLine();
				if (cad == null)
					return null;
				tk=new StringTokenizer(cad);
			}
			return tk.nextToken();
		}
		public int nextInt() throws NumberFormatException, IOException{
			return Integer.valueOf(next());
		}
		public long nextLong() throws NumberFormatException, IOException{
			return Long.valueOf(next());
		}
		public double nextDouble() throws NumberFormatException, IOException{
			return Double.valueOf(next());
		}
	}
	
	static class Pair {
		double x, y;
		public Pair(double xx, double yy) {
			x = xx;
			y = yy;
		}
		double dot(Pair o){
			return x * o.x + y * o.y;
		}
		Pair sub(Pair o) {
			return new Pair(x - o.x, y - o.y);
		}
		Pair add(Pair o) {
			return new Pair(x + o.x, y + o.y);
		}
		Pair mult(double a){
			return new Pair(a * x,  a * y);
		}
		double norm() {
			return Math.sqrt(x * x + y * y);
		}
		double project(Pair ref) {
			double c =  this.dot(ref) / ref.norm();
			Pair n = ref.mult(1. / ref.norm());
			n = n.mult(c);
			return this.sub(n).norm();
		}
	}
	
	
	static double process(Pair a, Pair b, Pair c) {
		double ret = Math.min(a.sub(b).norm(), a.sub(c).norm());
		ret = Math.min(ret, b.sub(c).norm());
		ret /= 2;
		double ret2 = Double.MAX_VALUE;
		ret2 = Math.min(a.sub(b).project(c.sub(b)), b.sub(c).project(a.sub(c)));
		ret2 = Math.min(ret2, c.sub(a).project(b.sub(a)));
		ret2 /= 2;
		return Math.min(ret, ret2);
	}
	
	
	static Pair[] points;
	
	public static void main(String args[]) throws NumberFormatException, IOException {
		Scanner sc = new Scanner();
		int N = sc.nextInt();
		points = new Pair[N];
		for(int i = 0; i < N; i++)
			points[i] = new Pair(sc.nextInt(), sc.nextInt());
		double ans = Double.MAX_VALUE;
		for(int i = 0; i < N; i++)
			ans = Math.min(ans, process(points[i], points[(i + 1)%N], points[(i + 2)%N]));
		System.out.printf("%.15f\n", ans);
	}

}
