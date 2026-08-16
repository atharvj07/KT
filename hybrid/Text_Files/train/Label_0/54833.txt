import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		PrintWriter pw = new PrintWriter(System.out);
		for (int i = 0; i < t; i++) {
			String[] sa = br.readLine().split(" ");
			int n = Integer.parseInt(sa[0]);
			int m = Integer.parseInt(sa[1]);
			int a = Integer.parseInt(sa[2]);
			int b = Integer.parseInt(sa[3]);
			pw.println(floorSum(n, m, a, b));
		}
		br.close();
		pw.flush();
	}

	/**
	 * floor((a * i + b) / m) の i＝0～n-1 の総和<br>
	 * y = (a/m)x + b/m、x軸、y軸、x = nで囲まれた領域の格子点の数（x軸上とx = n上は含まない）<br>
	 * 制約：0≦n≦10^9, 1≦m≦10^9, 0≦a,b＜m<br>
	 * O(log(n + m + a + b))
	 */
	static long floorSum(long n, long m, long a, long b) {
		long ans = 0;
		if (a >= m) {
			ans += (n - 1) * n * (a / m) / 2;
			a %= m;
		}
		if (b >= m) {
			ans += n * (n / m);
			b %= m;
		}

		long ymax = (a * n + b) / m;
		long xmax = (ymax * m - b);
		if (ymax == 0) {
			return ans;
		}
		ans += (n - (xmax + a - 1) / a) * ymax;
		ans += floorSum(ymax, a, m, (a - xmax % a) % a);
		return ans;
	}
}
