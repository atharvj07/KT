// practice with rainboy
import java.io.*;
import java.util.*;

public class CF1202A extends PrintWriter {
	CF1202A() { super(System.out); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF1202A o = new CF1202A(); o.main(); o.flush();
	}

	void reverse(byte[] aa, int n) {
		for (int i = 0, j = n - 1; i < j; i++, j--) {
			byte tmp = aa[i]; aa[i] = aa[j]; aa[j] = tmp;
		}
	}
	void main() {
		int t = sc.nextInt();
		while (t-- > 0) {
			byte[] aa = sc.next().getBytes();
			byte[] bb = sc.next().getBytes();
			int n = aa.length;
			int m = bb.length;
			reverse(aa, n);
			reverse(bb, m);
			int j = 0;
			while (bb[j] == '0')
				j++;
			int i = j;
			while (aa[i] == '0')
				i++;
			println(i - j);
		}
	}
}
