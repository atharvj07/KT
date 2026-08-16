import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class E {

	static final long MIN = -200000000010L;
	static final long MAX = 200000000010L;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out), false);
		String[] parts = br.readLine().split(" ");
		long h = Long.parseLong(parts[0]);
		int n = Integer.parseInt(parts[1]);
		long[] lives = new long[n];
		long minLive = MAX;
		long sumLive = 0;
		parts = br.readLine().split(" ");
		for (int i = 0; i < n; ++i) {
			lives[i] = Long.parseLong(parts[i]);
			sumLive += lives[i];
			minLive = Math.min(minLive, sumLive);
		}
		if (sumLive >= 0 && h + minLive > 0) {
			out.println(-1);
		} else {
			long fullRounds = sumLive >= 0 || h + minLive <= 0 ? 0 : (h + minLive) / -sumLive;
			h += fullRounds * sumLive;
			long ans = fullRounds * n;
			while (h > 0) {
				for (int i = 0; i < n; ++i) {
					++ans;
					h += lives[i];
					if (h <= 0) {
						break;
					}
				}
			}
			out.println(ans);
		}
		out.close();
	}
	
}
