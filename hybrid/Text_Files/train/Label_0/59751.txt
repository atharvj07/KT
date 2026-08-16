import java.util.*;
import java.io.*;

public class codeforces {
	public static void main(String[] args) throws Exception {

		
		int t=sc.nextInt();
		while(t-->0) {
			int n=sc.nextInt();
			char[][]a=new char[3][];
			a[0]=sc.next().toCharArray();
			a[1]=sc.next().toCharArray();
			a[2]=sc.next().toCharArray();
			
			int[]A0=new int[3];
			int[]A1=new int[3];
			
			for(int i=0;i<2*n;i++) {
				if(a[0][i]=='0') {
					A0[0]++;
				}else {
					A1[0]++;
				}
				if(a[1][i]=='0') {
					A0[1]++;
				}else {
					A1[1]++;
				}
				if(a[2][i]=='0') {
					A0[2]++;
				}else {
					A1[2]++;
				}
			}
			out:for(int i=0;i<2;i++) {
				for(int j=0;j<3;j++) {
					for(int k=j+1;k<3;k++) {
						if(i==0) {
							
							if(A0[j]>=n&&A0[k]>=n) {
								if(A0[j]>A0[k]) {
									int ind=0;
									while(ind<2*n&&a[k][ind]=='1') {
										pw.print('1');
										ind++;
									}
									for(int z=0;z<2*n;z++) {
										pw.print(a[j][z]);
										if(ind<2*n&&a[j][z]=='0') {
											ind++;
											while(ind<2*n&&a[k][ind]=='1') {
												pw.print('1');
												ind++;
											}
										}
									}
								}else {
									int ind=0;
									while(ind<2*n&&a[j][ind]=='1') {
										pw.print('1');
										ind++;
									}
									for(int z=0;z<2*n;z++) {
										pw.print(a[k][z]);
										if(ind<2*n&&a[k][z]=='0') {
											ind++;
											while(ind<2*n&&a[j][ind]=='1') {
												pw.print('1');
												ind++;
											}
										}
									}
								}
//								pw.print("*"+i+" "+j+" "+k);
								break out;
							}
							
						}else {
							if(A1[j]>=n&&A1[k]>=n) {
								if(A1[j]>A1[k]) {
									int ind=0;
									while(ind<2*n&&a[k][ind]=='0') {
										pw.print('0');
										ind++;
									}
									for(int z=0;z<2*n;z++) {
										pw.print(a[j][z]);
										if(ind<2*n&&a[j][z]=='1') {
											ind++;
											while(ind<2*n&&a[k][ind]=='0') {
												pw.print('0');
												ind++;
											}
										}
									}
								}else {
									int ind=0;
									while(ind<2*n&&a[j][ind]=='0') {
										pw.print('0');
										ind++;
									}
									for(int z=0;z<2*n;z++) {
										pw.print(a[k][z]);
										if(ind<2*n&&a[k][z]=='1') {
											ind++;
											while(ind<2*n&&a[j][ind]=='0') {
												pw.print('0');
												ind++;
											}
										}
									}
								}
								break out;
							}
							
						}
							
					}
				}
			}
			pw.println();
		}
		
		
		
		
		
		
		
		pw.close();
	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public Scanner(FileReader r) {
			br = new BufferedReader(r);
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public double nextDouble() throws IOException {
			String x = next();
			StringBuilder sb = new StringBuilder("0");
			double res = 0, f = 1;
			boolean dec = false, neg = false;
			int start = 0;
			if (x.charAt(0) == '-') {
				neg = true;
				start++;
			}
			for (int i = start; i < x.length(); i++)
				if (x.charAt(i) == '.') {
					res = Long.parseLong(sb.toString());
					sb = new StringBuilder("0");
					dec = true;
				} else {
					sb.append(x.charAt(i));
					if (dec)
						f *= 10;
				}
			res += Long.parseLong(sb.toString()) / f;
			return res * (neg ? -1 : 1);
		}

		public long[] nextlongArray(int n) throws IOException {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public Long[] nextLongArray(int n) throws IOException {
			Long[] a = new Long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}

		public int[] nextIntArray(int n) throws IOException {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public Integer[] nextIntegerArray(int n) throws IOException {
			Integer[] a = new Integer[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

	}

	static class pair implements Comparable<pair> {
		long x;
		long y;

		public pair(long x, long y) {
			this.x = x;
			this.y = y;
		}

		public String toString() {
			return x + " " + y;
		}

		public boolean equals(Object o) {
			if (o instanceof pair) {
				pair p = (pair) o;
				return p.x == x && p.y == y;
			}
			return false;
		}

		public int hashCode() {
			return new Long(x).hashCode() * 31 + new Long(y).hashCode();
		}

		public int compareTo(pair other) {
			if (this.x == other.x) {
				return Long.compare(this.y, other.y);
			}
			return Long.compare(this.x, other.x);
		}
	}

	static class tuble implements Comparable<tuble> {
		int x;
		int y;
		int z;

		public tuble(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}

		public String toString() {
			return x + " " + y + " " + z;
		}

		public int compareTo(tuble other) {
			if (this.x == other.x) {
				if (this.y == other.y) {
					return this.z - other.z;
				}
				return this.y - other.y;
			} else {
				return this.x - other.x;
			}
		}
	}

	static long mod = 1000000007;
	static Random rn = new Random();
	static Scanner sc = new Scanner(System.in);
	static PrintWriter pw = new PrintWriter(System.out);
}