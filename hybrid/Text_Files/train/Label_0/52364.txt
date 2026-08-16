import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.parseInt;

/**
 * Decimal Sequences - Time Limit Exceeded
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		int n = parseInt(br.readLine());
		char[] seq = new char[n];

		int _i = 0;
		while ((line = br.readLine()) != null && !line.isEmpty()) {
			for (int i = 0; i < line.length(); i += 2, _i++) {
				seq[_i] = line.charAt(i);
			}
		}

		//solve
		boolean[] nums = new boolean[1_000_000];
		outer:
		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				int len = j - i + 1;
				if ((seq[i] == '0' && len > 1) || len > 6) continue outer;
				nums[parseInt(String.valueOf(seq, i, len))] = true;
			}
		}

		for (int i = 0; i < nums.length; i++) {
			if (!nums[i]) {
				System.out.println(i);
				break;
			}
		}

	} //end main
}