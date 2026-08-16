
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class CF {

	private static Scanner cin = new Scanner(System.in);
	static final int N = 100111;
	static final long MAX = 1350851717672992089L;
	static int tc;
	long n;
	int a[];
	long p[];
	public void init() {
		p = new long[40];
		a = new int[40];
		p[0] = 1;
		for (int i = 1; i <= 38; i++) {
			p[i] = p[i-1] * 3L;
		}
	}
	public void input() {
		n = cin.nextLong();
	}
	
	public void solve() {
		long x = n;
		for (int i = 38; i >= 0; i--) {
			a[i] = (int)(x / p[i]);
			x %= p[i];
		}
		for (int i = 38; i >= 0; i--) {
			if (a[i] == 2) {
				for (int j = i + 1; j <= 38; j++) {
					if (a[j] == 0) {
						a[j] = 1;
						break;
					} else {
						a[j] = 0;
					}
				}
				for (int j = i; j >= 0; j--) {
					a[j] = 0;
				}
				break;
			}
		}
		x = 0;
		for (int i = 0; i <= 38; i++) {
			if (a[i] == 1) {
				x += p[i];
			}
		}
		System.out.println(x);
	}
	public static void main(String[] args) {
		int tc = cin.nextInt();
		CF cf = new CF();
		cf.init();
		while (tc-- > 0) {
			cf.input();
			cf.solve();
//			System.out.println(Arrays.toString(cf.b));
		}
	}
}
