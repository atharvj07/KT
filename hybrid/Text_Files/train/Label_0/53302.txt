import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String str[] = br.readLine().split(" ");

		long n = Long.parseLong(str[0]);
		long k = Long.parseLong(str[1]);

		long cnt[] = new long[100001];

		for (long i = 0; i < n; i++) {
			str = br.readLine().split(" ");

			long a = Long.parseLong(str[0]);
			long b = Long.parseLong(str[1]);

			cnt[(int) a] += b;
		}

		long count = 0;
		for (int i = 0; i < cnt.length; i++) {
			count += cnt[i];
			if (count >= k) {
				System.out.println(i);
				return;
			}
		}
	}

}
