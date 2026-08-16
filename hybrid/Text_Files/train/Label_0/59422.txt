import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) {
		IO io = new IO();
		while(true) {
			int n = io.nextInt();
			int m = io.nextInt();
			int r = io.nextInt();
			if (n == 0) {
				break;
			}
			Vector3.Long[] sx = new Vector3.Long[n];
			long[] sr = new long[n];
			for(int i=0;i<n;i++) {
				sx[i] = new Vector3.Long(io.nextLong(), io.nextLong(), io.nextLong());
				sr[i] = io.nextLong();
			}
			Vector3.Long[] tx = new Vector3.Long[m];
			long[] tb = new long[m];
			for(int i=0;i<m;i++) {
				tx[i] = new Vector3.Long(io.nextLong(), io.nextLong(), io.nextLong());
				tb[i] = io.nextLong();
			}
			Vector3.Long ex = new Vector3.Long(io.nextLong(), io.nextLong(), io.nextLong());
			double[] ti = new double[m];
			for(int i=0;i<m;i++) {
				ti[i] = (double) tb[i] / tx[i].subtract(ex).normSq();
			}
			boolean[][] block = new boolean[m][n];
			for(int i=0;i<n;i++) {
				Vector3.Long oa = ex.subtract(sx[i]);
				for(int j=0;j<m;j++) {
					block[j][i] = Vector3.Long.sphericalShellAndSegmentIntersects(oa, tx[j].subtract(sx[i]), sr[i]);
				}
			}
			double max = 0;
			LOOP: for(int i=1;i<(1<<m);i++) {
				double sum = 0;
				for(int j=0;j<m;j++) {
					if ((i&(1<<j)) > 0) {
						sum += ti[j];
					}
				}
				if (sum <= max) {
					continue;
				}
				int count = 0;
				boolean[] b = new boolean[n];
				for(int j=0;j<m;j++) {
					if ((i&(1<<j)) > 0) {
						for(int k=0;k<n;k++) {
							if (!b[k] && block[j][k]) {
								count++;
								b[k] = true;
								if (count > r) {
									continue LOOP;
								}
							}
						}
					}
				}
				max = sum;
			}
			io.println(max);
		}
		io.flush();
	}

}
abstract class Vector3 {
	public static class Long extends Vector3 {
		public static final Vector3.Long ZERO = new Vector3.Long(0, 0, 0);
		public long x;
		public long y;
		public long z;
		public Long() {
		}
		public Long(long x,long y,long z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
		public long dot(Long v) {
			return x * v.x + y * v.y + z * v.z;
		}
		public Long cross(Long v) {
			return new Long(y * v.z - z * v.y, z * v.x - x * v.z, x * v.y - y * v.x); 
		}
		public Long add(Long v) {
			return new Long(x + v.x, y + v.y, z + v.z);
		}
		public Long subtract(Long v) {
			return new Long(x - v.x, y - v.y, z - v.z);
		}
		public Long multiply(long k) {
			return new Long(k * x, k * y, k * z);
		}
		public long normSq() {
			return x * x + y * y + z * z;
		}
		public double norm() {
			return Math.sqrt(normSq());
		}
		public boolean isZero() {
			return x == 0 && y == 0 && z == 0;
		}
		public boolean equals(Object o) {
			if (o instanceof Vector3.Long) {
				Vector3.Long v = (Vector3.Long) o;
				return x == v.x && y == v.y && z == v.z;
			}
			return super.equals(o);
		}
		public String toString() {
			return "[" + this.x + "," + this.y + "]";
		}
		
		public static boolean sphericalShellAndSegmentIntersects(Long oa,Long ob,long r) {
			long aNormSq = oa.normSq();
			long bNormSq = ob.normSq();
			long rSq = r * r;
			if (aNormSq < rSq && bNormSq < rSq) {
				return false;
			}else if (aNormSq <= rSq || bNormSq <= rSq) {
				return true;
			}
			Long ab = ob.subtract(oa);
			if (ab.dot(oa) * ab.dot(ob) >= 0) {
				return false;
			}
			return (ab.cross(oa).normSq() <= r * r * ab.normSq());
		}
	}
}
class IO {
	BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
	StringBuilder out = new StringBuilder();
	int index = 0;
	String bfl = null;
	String[] bf = new String[0];
	private boolean read() {
		try {
			bfl = bi.readLine();
			if (bfl == null) {
				return false;
			}
			bf = bfl.split("\\s");
			index = 0;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return true;
	}
	public boolean hasNext() { return index < bf.length ? true : read(); }
	public boolean hasNextLine() { return read(); }
	public String next() { return hasNext() ? bf[index++] : null; }
	public String nextLine() { return hasNextLine() ? bfl : null; }
	public int nextInt() { return Integer.parseInt(next()); }
	public long nextLong() { return Long.parseLong(next()); }
	public double nextDouble() { return Double.parseDouble(next()); };
	public void println(long x) { out.append(x); out.append("\n"); }
	public void println(double x) { out.append(x); out.append("\n"); }
	public void println(String s) { out.append(s); out.append("\n"); }
	public void print(long x) { out.append(x); }
	public void print(double x) { out.append(x); }
	public void print(String s) { out.append(s); }
	public void flush() {System.out.print(out); out = new StringBuilder(); }
	public int[] arrayInt(int n) {
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i] = nextInt();
		}
		return a;
	}
	public long[] arrayLong(int n) {
		long[] a = new long[n];
		for(int i=0;i<n;i++) {
			a[i] = nextLong();
		}
		return a;
	}
	public double[] arrayDouble(int n) {
		double[] a = new double[n];
		for(int i=0;i<n;i++) {
			a[i] = nextDouble();
		}
		return a;
	}
}