import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class A122_LuckyDivision {

	static BufferedReader in;
	static StringTokenizer st;
	static PrintWriter out;

	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens()) {
			st = new StringTokenizer(in.readLine());
		}
		return st.nextToken();
	}

	static int nextInt() throws IOException {
		return Integer.parseInt(next());
	}

	public static void main(String[] args) throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
				System.out)));
		int[] luckyNumbers = { 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744,
				747, 774, 777 };
		int n = nextInt();
		boolean isLucky = false;
		for (int i = 0; i < luckyNumbers.length; i++) {
			if (n % luckyNumbers[i] == 0) {
				isLucky = true;
			}
		}
		if (isLucky) {
			out.print("YES");
		} else {
			out.print("NO");
		}
		out.close();
	}
}
