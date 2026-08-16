import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

	public static double getDistance (double a, double b, double c, double d) {

		return Math.sqrt(Math.pow(c -a,2) + Math.pow(d - b,2));

	}

	public static void main(String[] args) throws IOException {

		BufferedReader br =
			new BufferedReader(new InputStreamReader(System.in));
		ArrayList<String> ans = new ArrayList<String>();
		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");

			double x1 = Double.parseDouble(st.nextToken());
			double y1 = Double.parseDouble(st.nextToken());
			double x2 = Double.parseDouble(st.nextToken());
			double y2 = Double.parseDouble(st.nextToken());
			double x3 = Double.parseDouble(st.nextToken());
			double y3 = Double.parseDouble(st.nextToken());

			double a1 = 2 * (x2 - x1);
			double b1 = 2 * (y2 - y1);
			double c1 = x1 * x1 - x2 * x2 + y1 * y1 - y2 * y2;
			double a2 = 2 * (x3 - x1);
			double b2 = 2 * (y3 - y1);
			double c2 = x1 * x1 - x3 * x3 + y1 * y1 - y3 * y3;

			double xp = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1);
			double yp = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1);

			double a = getDistance(x1,y1,x2,y2);
			double b = getDistance(x1,y1,x3,y3);
			double c = getDistance(x2,y2,x3,y3);

			double s = (a + b + c) / 2;
			double S = Math.sqrt(s * (s - a) * (s - b) * (s - c));
			double r = (a * b * c) / (S * 4);

			BigDecimal bd_xp = BigDecimal.valueOf(xp).setScale(3, BigDecimal.ROUND_HALF_UP);
			BigDecimal bd_yp = BigDecimal.valueOf(yp).setScale(3, BigDecimal.ROUND_HALF_UP);
			BigDecimal bd_r  = BigDecimal.valueOf(r).setScale(3, BigDecimal.ROUND_HALF_UP);

			ans.add(bd_xp.toString() + " " + bd_yp.toString() + " " + bd_r.toString());
		}
		for (String s : ans) {
			System.out.println(s);
		}
	}

}