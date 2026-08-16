import java.util.Arrays;
import java.util.Scanner;


public class Main {

	static Scanner sc = new Scanner(System.in);
	static int m,n;
	static int[] p;
	public static void main(String[] args) {
		while(read())	solve();
	}

	private static void solve() {
		Arrays.sort(p);
		p = reverse(p);
		int i = 0;
		int sum = 0;
		while (m >= i + n) {
			for (int j = 0; j < n-1; j++) {
				sum += p[i + j];
			}
			i += n;
		}
		for (int j = i; j < m; j++) {
			sum += p[j];
		}
		System.out.println(sum);
	}

	private static int[] reverse(int[] in) {
		int[] out = new int[in.length];
		for (int i = 0; i < in.length; i++) {
			out[i] = in[in.length - 1 - i];
		}
		return out;
	}

	private static boolean read() {
		m = sc.nextInt();
		n = sc.nextInt();
		if(m==0 && n==0) return false;

		p = new int[m];
		for(int i=0; i<m; i++) {
			p[i] = sc.nextInt();
		}
		return true;
	}


}