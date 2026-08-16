import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int n = in.nextInt();
		long[] r = new long[n];
		for (int i = 0; i < n; i++) {
			String s = in.next();
			int p = in.nextInt();
			r[i] = toLong(s, p, i + 1);
		}
		Arrays.sort(r);
		for (int i = 0; i < n; i++)
			System.out.println(r[i] % 101);
		in.close();
	}

	private static long toLong(String s, int p, int n) {
		long r = 0;
		for (int i = 0; i < 10; i++) {
			r *= 26;
			if (i < s.length())
				r += s.charAt(i) - 'a';
		}
		r *= 101;
		r += 101 - p;
		r *= 101;
		r += n;
		return r;
	}

}