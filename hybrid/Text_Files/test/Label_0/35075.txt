import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) {
		Scanner ir = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = ir.nextInt();
		long m = ir.nextLong();
		int[][] a = new int[n][];
		for (int i = 0; i < n; i++) {
			a[i] = new int[] { ir.nextInt(), ir.nextInt() };
		}
		int[][] ca = compress(a);
		int[] imos = new int[1000000];
		for (int i = 0; i < n; i++) {
			imos[ca[i][0]]++;
			imos[ca[i][1] + 1]--;
		}
		int ma = 0;
		for (int i = 0; i < 1000000 - 1; i++) {
			imos[i + 1] += imos[i];
			ma = Math.max(ma, imos[i]);
		}
		long res = (long) ma * m;
		if (ma % 2 == 0) {
			for (int i = 0; i < 1000000; i++) {
				if (imos[i] == ma) {
					res -= conv[i];
					break;
				}
			}
		} else {
			for (int i = 1000000 - 1; i >= 0; i--) {
				if (imos[i] == ma) {
					res -= (m - conv[i]);
					break;
				}
			}
		}
		out.println(res);
		out.flush();
	}

	static int[] conv = new int[1000000];

	static int[][] compress(int[][] a) {
		TreeSet<Integer> st = new TreeSet<>();
		int[][] ret = new int[a.length][2];
		for (int i = 0; i < a.length; i++) {
			for (int x : a[i])
				st.add(x);
		}
		ArrayList<Integer> l = new ArrayList<>(st);
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < 2; j++) {
				int idx = Collections.binarySearch(l, a[i][j]);
				ret[i][j] = idx;
				conv[idx] = a[i][j];
			}
		}
		return ret;
	}
}
