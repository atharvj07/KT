import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.parseInt;

/**
 * Problem B: Matsuzaki Number
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;

		boolean[] primes = primes(100_0000);

		while ((line = br.readLine()) != null && !line.isEmpty()) {

			int N, P;
			N = parseInt(line.substring(0, line.indexOf(' ')));
			P = parseInt(line.substring(line.indexOf(' ') + 1));
			if (N == -1 || P == -1) break;

			List<Integer> _primes = new ArrayList<>();
			for (int i = N + 1; ; i++) {
				if (primes[i]) {
					_primes.add(i);
					if (_primes.size() == P) {
						break;
					}
				}
			}

			List<Integer> ans = new ArrayList<>();
			for (int i = 0; i < _primes.size(); i++) {
				for (int j = 0; j < _primes.size(); j++) {
					if (i <= j) {
						ans.add(_primes.get(i) + _primes.get(j));
					}
				}
			}
			Collections.sort(ans);
			System.out.println(ans.get(P - 1));
		} //end while
	} //end main

	static boolean[] primes(int limit) {

		boolean[] ps = new boolean[limit + 1];
		int _limit = (int) Math.ceil(Math.sqrt(ps.length));

		Arrays.fill(ps, 2, ps.length, true);

		for (int i = 2; i <= _limit; i++) {
			if (ps[i]) {
				for (int j = i * 2; j < ps.length; j += i) {
					if (ps[j]) ps[j] = false;
				}
			}
		}
		return ps;
	}
}