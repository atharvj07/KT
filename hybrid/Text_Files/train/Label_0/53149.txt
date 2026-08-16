import java.util.*;
import java.io.*;

public class B {
	public static void main(String[] args) throws IOException {
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);
		n = Integer.parseInt(rd.readLine());
		p = new double[n];
		StringTokenizer st = new StringTokenizer(rd.readLine());
		for(int i=0; i<n; i++) p[i] = Double.parseDouble(st.nextToken());
		double[] f = new double[n];
		f[n-1] = p[n-1];
		for(int i=n-2; i>=0; i--) f[i] = p[i]*(1+f[i+1]);
		double ans = 0;
		for(int i=0; i<n; i++) ans += 2*f[i]-p[i];
		pw.println(ans);
		pw.flush();
	}
	
	static int n;
	
	static double[] p;
	
}
