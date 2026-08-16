import java.util.HashSet;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static char[] str = new char[1100];
	static int N;
	static HashSet<String> outer = new HashSet<String>();
	static HashSet<String> inner = new HashSet<String>();

	public static void main(String[] args) {
		while (sc.hasNextLine()) {
			N = 0;
			outer.clear();
			inner.clear();
			for (char c : sc.nextLine().toUpperCase().toCharArray()) {
				if ('A' <= c && c <= 'Z') {
					str[N++] = c;
				}
			}
			for (int i = 0; i + 2 < N; i++) {
				if (str[i] == str[i + 2]) {
					solve(i, i + 2);
				}
			}
			for (int i = 0; i + 3 < N; i++) {
				if (str[i] == str[i + 3] && str[i + 1] == str[i + 2]) {
					solve(i, i + 3);
				}
			}
			outer.removeAll(inner);
			String[] ans = outer.toArray(new String[0]);
			if (ans.length > 0) {
				System.out.print(ans[0]);
			}
			for (int i = 1; i < ans.length; ++i) {
				System.out.print(" " + ans[i]);
			}
			System.out.println();
		}
	}

	static void solve(int l, int r) {
		while (l > 0 && r < N - 1 && str[l - 1] == str[r + 1]) {
			inner.add(String.valueOf(str, l, r - l + 1));
			--l;
			++r;
		}
		outer.add(String.valueOf(str, l, r - l + 1));
	}

}