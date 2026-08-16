import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int[] key = new int[256];

	public static void main(String[] args) {
		while (true) {
			StringBuilder sb = new StringBuilder();
			while (true) {
				String line = sc.nextLine();
				if (line.isEmpty()) break;
				sb.append(line);
			}
			char[] input = sb.toString().toCharArray();
			int N = input.length;
			Arrays.fill(key, -1);
			String keys = sc.nextLine();
			for (int i = 0; i < keys.length(); ++i) {
				key[keys.charAt(i)] = i;
			}
			int[] count = new int[keys.length()];
			int l = 0;
			int r = 0;
			int ans = Integer.MAX_VALUE;
			int ansC = 0;
			String repr = "";
			int found = 0;
			while (r < N) {
				while (r < N) {
					if (key[input[r]] >= 0) {
						if (count[key[input[r]]] == 0) ++found;
						count[key[input[r]]]++;
						if (found == keys.length()) break;
					}
					++r;
				}
				if (r == N) break;
				while (true) {
					if (key[input[l]] >= 0) {
						--count[key[input[l]]];
						if (count[key[input[l]]] == 0) {
							--found;
							if (r - l + 1 < ans) {
								ans = r - l + 1;
								ansC = 1;
								repr = String.valueOf(input, l, r - l + 1);
							} else if (r - l + 1 == ans) {
								++ansC;
							}
							++l;
							break;
						}
					}
					++l;
				}
				++r;
			}

			if (ansC == 0) {
				System.out.println(0);
			} else {
				System.out.println(ansC);
				StringBuilder result = new StringBuilder();
				for (int i = 0; i < repr.length(); ++i) {
					if (i % 72 == 0) {
						result.append('\n');
					}
					result.append(repr.charAt(i));
				}
				System.out.println(result);
			}
			System.out.println();
			if (!sc.hasNext()) break;
			sc.nextLine();
		}
	}

}