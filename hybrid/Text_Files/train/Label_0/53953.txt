import java.io.*;
import java.util.*;

public class CF337B {
	static int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a % b);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int p, q;
		if (a * d >= b * c) {
			p = a * d - b * c;
			q = a * d;
		} else {
			p = b * c - a * d;
			q = b * c;
		}
		int g = gcd(p, q);
		p /= g;
		q /= g;
		System.out.println(p + "/" + q);
	}
}
