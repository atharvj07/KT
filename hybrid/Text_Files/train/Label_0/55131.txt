// practice with rainboy
import java.io.*;
import java.util.*;

public class CF663E {
	static void fwht(long[] aa, int n) {
		for (int h = 0, b; (b = 1 << h) < n; h++)
			for (int i = 0; i < n; i += b * 2)
				for (int j = 0; j < b; j++) {
					int l = i + j, r = l + b;
					long u = aa[l], v = aa[r];
					aa[l] = u + v;
					aa[r] = u - v;
				}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		char[][] cc = new char[n][m];
		for (int i = 0; i < n; i++)
			br.readLine().getChars(0, m, cc[i], 0);
		int n_ = 1 << n;
		long[] aa = new long[n_];
		for (int j = 0; j < m; j++) {
			int x = 0;
			for (int i = 0; i < n; i++)
				x = x * 2 + cc[i][j] - '0';
			aa[x]++;
		}
		long[] bb = new long[n_];
		for (int h = 1; h < n_; h++)
			bb[h] = bb[h & h - 1] + 1;
		for (int h = 0; h < n_; h++)
			bb[h] = bb[n_ - 1 ^ h] = Math.min(bb[h], bb[n_ - 1 ^ h]);
		fwht(aa, n_);
		fwht(bb, n_);
		for (int h = 0; h < n_; h++)
			aa[h] *= bb[h];
		fwht(aa, n_);
		for (int h = 0; h < n_; h++)
			aa[h] /= n_;
		long ans = m * n;
		for (int h = 0; h < n_; h++)
			ans = Math.min(ans, aa[h]);
		System.out.println(ans);
	}
}
