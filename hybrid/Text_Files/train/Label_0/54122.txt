// practice with kaiboy
import java.io.*;
import java.util.*;

public class Main extends PrintWriter {
	Main() { super(System.out, true); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		Main o = new Main(); o.main(); o.flush();
	}

	static class V {
		int i, j;
		V(int i, int j) {
			this.i = i; this.j = j;
		}
	}
	void main() {
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		int k_ = k * 9;
		V[] vv = new V[k_];
		k_ = 0;
		while (k-- > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			for (int i = a - 2; i <= a; i++)
				for (int j = b - 2; j <= b; j++)
					if (i >= 1 && j >= 1 && i + 2 <= n && j + 2 <= m)
						vv[k_++] = new V(i, j);
		}
		Arrays.sort(vv, 0, k_, (u, v) -> u.i != v.i ? u.i - v.i : u.j - v.j);
		int[] kk = new int[10];
		for (int u = 0, v; u < k_; u = v) {
			int i = vv[u].i, j = vv[u].j;
			v = u + 1;
			while (v < k_ && vv[v].i == i && vv[v].j == j)
				v++;
			kk[v - u]++;
		}
		long z = (long) (n - 2) * (m - 2);
		for (int h = 1; h < 10; h++)
			z -= kk[h];
		println(z);
		for (int h = 1; h < 10; h++)
			println(kk[h]);
	}
}
