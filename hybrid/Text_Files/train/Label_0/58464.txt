import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;

class Main {
	public static void main(String args[]) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String buf;

		try {
			while ((buf = br.readLine())!=null) {
				StringTokenizer st = new StringTokenizer(buf);
				int V = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());
				int f[] = new int[V+1];
				int count = 1;
				f[0] = 1;
				f[1] = 2;
				for (int i=2;i<=V;i++) {
					f[i] = (f[i-1]+f[i-2])%1001;
				}
				Arrays.sort(f);
				for (int i=2;i<=V;i++) {
					if (f[i]-f[i-1]>=d) count++;
				}
				System.out.println(count);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}