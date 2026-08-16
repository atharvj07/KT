import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ProblemD {
	
	static final double EPS = 1e-11; 

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);

		String[] nlr = in.readLine().split(" ");
		int n = Integer.valueOf(nlr[0]);
		int l = Integer.valueOf(nlr[1]);
		int r = Integer.valueOf(nlr[2]);
		
		long[][] light = new long[n][2];
		double[] rad = new double[n];
		for (int i = 0 ; i < n ; i++) {
			String[] xya = in.readLine().split(" ");
			light[i][0] = Integer.valueOf(xya[0]);
			light[i][1] = Integer.valueOf(xya[1]);
			int ra = Integer.valueOf(xya[2]);
			rad[i] = Math.PI * ra / 180; 
		}
		
		
		double[] dp = new double[1<<n];
		double best = l;
		Arrays.fill(dp, -1e12);
		dp[0] = l;
		for (int i = 0 ; i < (1<<n) ; i++) {
			if (dp[i] + EPS >= l) {
				double left = dp[i];
				for (int j = 0 ; j < n ; j++) {
					if ((i & (1<<j)) >= 1) {
						continue;
					}
					int ti = i|(1<<j);
					double dx = (left - light[j][0]);
					double dy = -light[j][1];
					{
						double tdx = dx * Math.cos(rad[j]) - dy * Math.sin(rad[j]);
						double tdy = dx * Math.sin(rad[j]) + dy * Math.cos(rad[j]);
						if (tdy >= -EPS) {
							best = r;
						} else {
							double tdxOne = tdx * light[j][1] / (Math.abs(tdy) + EPS);
							double tx = light[j][0] + tdxOne;
							if (dp[ti] < tx) {
								dp[ti] = tx;
								best = Math.max(best, dp[ti]);
							}
						}
					}
				}
			}
			if (best > r) {
				break;
			}
		}
		
		out.println(Math.min(r - l, best - l));
		out.flush();
	}

	
	static double[] rotate(double dx, double dy, double rad) {
		return new double[]{ dx * Math.cos(rad) - dy * Math.sin(rad), dx * Math.sin(rad) + dy * Math.cos(rad)};
	}
	
	

	public static void debug(Object... o) {
		System.err.println(Arrays.deepToString(o));
	}

}
