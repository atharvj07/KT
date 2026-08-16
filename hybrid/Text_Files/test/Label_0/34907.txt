import java.util.*;
import java.io.*;
import static java.lang.Math.*;
import java.math.*;

public class Main implements Runnable {
	BufferedReader in;
	PrintStream out;  
	StringTokenizer st = new StringTokenizer("");
	static boolean local = false;
	
	public static void main(String [] args) throws Exception {
		if (args.length > 0) local = true;
		new Thread(new Main()).start();
	}

	class V implements Comparable <V> {
		int x, y;

		V(int x, int y) { this.x = x; this.y = y; }

		public int compareTo(V r) {
			if (y >= 0 && r.y < 0) return 1;
			if (y < 0 && r.y >= 0) return -1;
			return x * r.y - y * r.x > 0 ? -1 : 1;	
		}
	}

	void balance(int [] x) {
		int n = x.length;
		int S = 500;
		int [][] dx = new int [n][S];
		int mid = S / 2;
		dx[0][mid + x[0]] = 1;
		dx[0][mid - x[0]] = -1;
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < S; j++) {
				if (dx[i - 1][j] == 0) continue;
				int sa = j + x[i], ss = j - x[i];
				if (sa >= 0 && sa < S) dx[i][sa] = 1;
				if (ss >= 0 && ss < S) dx[i][ss] = -1;
			} 	
		}

		if (dx[n - 1][mid] == 0) System.out.println("bad");
		int cur = mid;
		for (int i = n - 1; i >= 0; i--) {
			//System.out.println(dx[i][cur]);
			if (dx[i][cur] == -1) x[i] = -x[i];
			cur -= x[i];
		}
	}

	public void run() {
		try {
			Locale.setDefault(Locale.US);
			in = local ? new BufferedReader(new FileReader("input.txt")) : new BufferedReader(new InputStreamReader(System.in));
			out = local ? new PrintStream(new File("output.txt")) : new PrintStream(System.out);

			int M = 1000000, cnt = 0;
			int [] x = new int[M], y = new int [M];
			Arrays.fill(x, -1);
			for (int i = 0; i < 500; i++)
				for (int j = i + 1; j < 500; j++) {
					int s = i * i + j * j;
					if (x[s] == -1) {
						cnt++;
						x[s] = i;
						y[s] = j;
					}	
				}

			int n = nextInt();
			cnt = 0;
			

			//int [] tmp = new int[] {1, 1, 1, 1};
			//balance(tmp);
			//System.out.println(tmp[0] + " " + tmp[1] + " " + tmp[2] + " " + tmp[3]);

			int [] gx = new int[n], gy = new int[n];

			int k = 0, Sum = 0;
			while (cnt < n) {
				if (x[k] != -1) {
					gx[cnt] = x[k];
					gy[cnt] = y[k];
					Sum += x[k] + y[k];
					cnt++;
					//System.out.println(k + " " + x[k] + " " + y[k]);
				}
				k++;
			}

			if (Sum % 2 != 0) {
				while (x[k] == -1) k++;
				int cs = x[k] + y[k];
				for (int i = n - 1; i >= 0; i--) {
					if ((cs - gx[i] - gy[i]) % 2 != 0) {
						gx[i] = x[k];
						gy[i] = y[k];
						break;
					}
				}
			}

			
			Sum = 0;
			for (int i = 0; i < n; i++) {
				Sum += gx[i];	
			}

			if (Sum % 2 != 0) {
				for (int i = 0; i < n; i++) {
					if ((gx[i] + gy[i]) % 2 != 0) {
						int tmp = gx[i];
						gx[i] = gy[i];
						gy[i] = tmp;
						break;
					}
				}
			}

			balance(gx);
			balance(gy);



			V [] arr = new V[n];
			for (int i = 0; i < n; i++) {
				arr[i] = new V(gx[i], gy[i]);
				//System.out.println("vector: " + gx[i] + " " + gy[i]);
			}


			Arrays.sort(arr);
			
			out.println("YES");

			int cx = 0, cy = 0;
			for (int i = 0; i < n; i++) {
				cx += arr[i].x;
				cy += arr[i].y;
				out.println(cx + " " + cy);
			}
			
			//System.out.println(cnt);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}

	boolean seekForToken() {
 		try {
			while (!st.hasMoreTokens()) {
				String s = in.readLine();
				if (s == null) {
				 	return false;
				}
			 	st = new StringTokenizer(s);
			}
			return true;
		}
		catch (IOException e) {
		 	e.printStackTrace();
		 	return false;
		}
 	}

 	int nextInt() {
		return Integer.parseInt(nextToken());
 	}

 	long nextLong() {
		return Long.parseLong(nextToken());
 	}

 	double nextDouble() {
		return Double.parseDouble(nextToken());
 	}

 	BigInteger nextBigInteger() {
 	 	return new BigInteger(nextToken());
 	}

 	String nextToken() {
 	 	seekForToken();
 	 	return st.nextToken();
 	}

}
