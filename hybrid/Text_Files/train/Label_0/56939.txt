import java.util.*;
import java.io.*;

public class SubstringsSort {

	void solve(Scanner in, PrintWriter out) {
		int n = in.nextInt();
		String[] s = new String[n];
		for (int i = 0; i < n; i++)
			s[i] = in.next();

		Arrays.sort(s, new Comparator<String>() {

			@Override
			public int compare(String s1, String s2) {

				if (s1.indexOf(s2) != -1)
					return 1;
				else if (s2.indexOf(s1) != -1)
					return -1;
				else
					return 0;
			}
		});

		for (int i = 0; i < n; i++) {

			for (int j = i - 1; j >= 0; j--) {
				if (s[i].indexOf(s[j]) == -1) {
					out.println("NO");
					return;
				}
			}
		}
		out.println("YES");
		for (int i = 0; i < n; i++) {
			out.println(s[i]);
		}

		//out.println(Arrays.toString(s));
	}

	void run() {
		try (Scanner in = new Scanner(System.in); PrintWriter out = new PrintWriter(System.out);) {
			solve(in, out);
		}
	}

	public static void main(String args[]) {
		new SubstringsSort().run();
	}
}
