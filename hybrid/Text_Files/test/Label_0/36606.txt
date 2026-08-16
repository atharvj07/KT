import java.io.*;
import java.util.*;

public class CF948D extends PrintWriter {
	CF948D() { super(System.out, true); }
	static class Scanner {
		Scanner(InputStream in) { this.in = in; } InputStream in;
		byte[] bb = new byte[1 << 15]; int i, n;
		byte getc() {
			if (i == n) {
				i = n = 0;
				try { n = in.read(bb); } catch (IOException e) {}
			}
			return i < n ? bb[i++] : 0;
		}
		int nextInt() {
			byte c = 0; while (c <= ' ') c = getc();
			int a = 0; while (c > ' ') { a = a * 10 + c - '0'; c = getc(); }
			return a;
		}
	}
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF948D o = new CF948D(); o.main(); o.flush();
	}

	static final int H = 30;
	void main() {
		int n = sc.nextInt();
		int[] aa = new int[n];
		for (int i = 0; i < n; i++)
			aa[i] = sc.nextInt();
		int m = 2 + H * n;
		int[] tt = new int[m * 2];
		int[] kk = new int[m * 2];
		m = 2;
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int u = 1;
			for (int h = H; h-- > 0; ) {
				int a = x >> h & 1;
				int ua = u << 1 | a;
				kk[ua]++;
				if (tt[ua] == 0)
					tt[ua] = m++;
				u = tt[ua];
			}
		}
		for (int i = 0; i < n; i++) {
			int x = aa[i];
			int u = 1;
			for (int h = H; h-- > 0; ) {
				int a = x >> h & 1;
				int ua = u << 1 | a;
				if (kk[ua] == 0) {
					a ^= 1;
					ua ^= 1;
				}
				x ^= a << h;
				kk[ua]--;
				u = tt[ua];
			}
			print(x + " ");
		}
		println();
	}
}
