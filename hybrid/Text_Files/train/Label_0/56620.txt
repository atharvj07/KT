import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	public void run() {
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		String T = sc.next();
		int[] v = Zalgo(T + S);
		int[] u = Zalgo(rev(T) + rev(S));
		int ans = 0;
		v = Arrays.copyOfRange(v, T.length(), T.length() + S.length());
		u = Arrays.copyOfRange(u, T.length(), T.length() + S.length());
		for (int i = 0; i < S.length(); ++i) {
			if (S.length() - 1 - i - (T.length() - 1) < u.length && S.length() - 1 - i - (T.length() - 1) >= 0)
				if (v[i] + u[S.length() - 1 - i - (T.length() - 1)] == T.length() - 1)
					++ans;
		}
		System.out.println(ans);

	}

	String rev(String S) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < S.length(); ++i) {
			sb.append(S.charAt(S.length() - 1 - i));
		}
		return sb.toString();
	}

	int[] Zalgo(String S) {
		char[] s = S.toCharArray();
		int n = s.length;
		int[] ret = new int[n];
		ret[0] = n;
		int i = 1, j = 0;
		while (i < n) {
			while (i + j < n && s[j] == s[i + j])
				++j;
			ret[i] = j;
			if (j == 0) {
				++i;
				continue;
			}
			int k = 1;
			while (i + k < n && k + ret[k] < j) {
				ret[i + k] = ret[k];
				++k;
			}
			i += k;
			j -= k;

		}
		return ret;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}