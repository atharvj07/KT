
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		reader.readLine();
		int n = Integer.parseInt(reader.readLine());
		
		int[] y = new int[n];
		int[] x = new int[n];
		int[] sy = new int[n];
		int[] sx = new int[n];
		for (int i = 0; i < n; i++) {
			StringTokenizer to = new StringTokenizer(reader.readLine());
			sx[i] = x[i] = Integer.parseInt(to.nextToken());
			sy[i] = y[i] = Integer.parseInt(to.nextToken());
		}
		Arrays.sort(x);
		Arrays.sort(y);
		int ax = 0;
		int ay = 0;
		long ans = Long.MAX_VALUE;
		int m = (n - 1) / 2;
		int nm = n/2;
		int[] xx = {x[m],x[nm]};
		int[] yy  ={y[m],y[nm]};
		for (int i = 0; i <= 1; i++) {
			for (int j = 0; j <= 1; j++) {
				long res = 0;
				long max = 0;
				for (int k = 0; k < n; k++) {
					long dis = Math.abs(sx[k] - xx[i]) + Math.abs(sy[k] - yy[j]);
					res += dis * 2;
					max = Math.max(max, dis);
				}
				res -= max;
				if (res < ans) {
					ans = res;
					ax = xx[i];
					ay = yy[j];
				}
			}
		}
		System.out.println(ans);
		System.out.println(ax + " " + ay);
	}
}