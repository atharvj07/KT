import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());

		int[] a = new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		long count = a[n - 1];
		int prev = a[n - 1];
		for (int i = n - 2; i >= 0; i--) {
			if (a[i] < prev) {
				count += a[i];
				prev = a[i];
			} else {
				prev = Math.max(0, prev - 1);
				count += prev;
			}
		}

		System.out.println(count);

	}
}
