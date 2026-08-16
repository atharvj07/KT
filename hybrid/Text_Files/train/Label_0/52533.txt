import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.util.Arrays;
public class E {
	private static class Segment implements Comparable<Segment> {
		double s;
		double e;
		public Segment(double s, double e) {
			this.s = s;
			this.e = e;
		}
		public int compareTo(Segment a) {
			if(s<a.s) return -1;
			if(s==a.s) return 0;
			else return 1;
		}
	}
	public static void main(String args[]) {
		Kattio sc = new Kattio(System.in);
		long x0 = sc.getLong();
		long y0 = sc.getLong();
		long v = sc.getLong();
		long T = sc.getLong();
		long r0 = v*T;
		double r00 = (r0+0.0)*r0;
		double PI2 = 2*Math.PI;
		int n = sc.getInt();
		Segment[] set = new Segment[2*n];
		int w = 0;
		for(int i = 0; i<n; i++) {
			long x = sc.getLong() - x0;
			long y = sc.getLong() - y0;
			long r = sc.getLong();
			long dd = x*x + y*y;
			double d = Math.sqrt(dd);
			if(dd > (double)(r0+r)*(r0+r)) continue;
			if(r*r >= dd) {
				System.out.println(1.0);
				return;
			}
			double base = (Math.atan2(y,x) + PI2)%PI2;
			double alpha;
			if(Math.sqrt(dd - r*r) <= r0) {
				alpha = Math.asin(r/d);				
			} else {
				double calpha = (dd + r00 - r*(r+0.0))/(2*d*r0);
				if(calpha >= 1) calpha = 1;
				if(calpha <= -1) calpha = -1;
				alpha = Math.abs(Math.acos(calpha));
			}
			if(alpha == 0) continue;
			double s = base - alpha;
			double e = base + alpha;
			if(s<0) {
				s += PI2;
				set[w++] = new Segment(s,PI2);
				s = 0;
			}
			if(e>PI2) {
				e -= PI2;
				set[w++] = new Segment(0,e);
				e = PI2;
			}
			set[w++] = new Segment(s,e);
			
			
		}
		if(w == 0) {
			System.out.println(0);
			return;
		}
		double sum = 0;
		Arrays.sort(set,0,w);
		double start = set[0].s;
		double end = set[0].e;
		for(int a = 1; a<w; a++) {
			if(set[a].s>end) {
				sum += end - start;
				start = set[a].s;
				end = set[a].e;
			} else {
				end = Math.max(end,set[a].e);
			}
		}
		sum += end - start;
		System.out.println(sum/(2*Math.PI));
	}
	/*public static void update(TreeSet<Segment> set, double s, double e) {
		if(s == e) return;
		if(s>e) {
			update(set,0,e);
			update(set,s,Math.PI*2);
			return;
		}
		//System.out.println(s + " " + e);
		
		
		NavigableSet<Segment> sub = set.subSet(new Segment(s,s),true,new Segment(e,e),true);
		//System.out.println(sub.size());
		
		Segment ss = set.ceiling(new Segment(s,s));
		Segment ee = set.ceiling(new Segment(e,e));
		
		Iterator<Segment> itr = sub.iterator();
		while(itr.hasNext()) {
			itr.next();
			itr.remove();
		}
		boolean a = (ss != null && (ss.compareTo(new Segment(s,s)) == 0));
		boolean b = (ee != null && (ee.compareTo(new Segment(e,e)) == 0));
		//System.out.println(a + " " + b);
		if(!a && !b) {
			//System.out.println("false:false " + s + " " + e);
			
			set.add(new Segment(s,e));
			
		} else if(!a && b) {
			//System.out.println("false:true " + ee.s + " " + ee.e + " " + s + " " + e);
			ee.s = s;
			set.add(ee);
		} else if(a && !b){
			//System.out.println("true:false " + ss.s + " " + ss.e + " " + s + " " + e);
			ss.e = e;
			set.add(ss);
		} else if(ss != ee) {
			//System.out.println("true:true " + ss.s + " " + ss.e + " " + s + " " + e);
			ss.e = e;
			set.add(ss);
		} else {
			set.add(ss);
		}
		
		
	}*/
}
class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
	super(new BufferedOutputStream(System.out));
	r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
	super(new BufferedOutputStream(o));
	r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
	return peekToken() != null;
    }

    public int getInt() {
	return Integer.parseInt(nextToken());
    }

    public double getDouble() { 
	return Double.parseDouble(nextToken());
    }

    public long getLong() {
	return Long.parseLong(nextToken());
    }

    public String getWord() {
	return nextToken();
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
	if (token == null) 
	    try {
		while (st == null || !st.hasMoreTokens()) {
		    line = r.readLine();
		    if (line == null) return null;
		    st = new StringTokenizer(line);
		}
		token = st.nextToken();
	    } catch (IOException e) { }
	return token;
    }

    private String nextToken() {
	String ans = peekToken();
	token = null;
	return ans;
    }
}
