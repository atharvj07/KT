// https://codeforces.com/contest/1168/submission/54696824 (neal)
// upsolve with rainboy
import java.io.*;
import java.util.*;

public class CF1168E {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = 1 << k;
		int[] aa = new int[n];
		int a = 0;
		for (int i = 0; i < n; i++)
			a ^= aa[i] = Integer.parseInt(st.nextToken());
		if (a != 0) {
			System.out.println("Fou");
			return;
		}
		int[] pp = new int[n];
		int[] qq = new int[n];
		int[] ii = new int[n];
		for (int i = 0; i < n; i++)
			pp[i] = qq[i] = ii[i] = i;
		for (int i = 0; i < n - 1; i++)
			for (int u = i, v; u <= i && (aa[u] ^ pp[u] ^ qq[u]) != 0; u = v) {
				v = ii[aa[u] ^ pp[u]];
				int tmp;
				tmp = qq[u]; qq[u] = qq[v]; qq[v] = tmp;
				tmp = ii[qq[u]]; ii[qq[u]] = ii[qq[v]]; ii[qq[v]] = tmp;
				tmp = pp[v]; pp[v] = pp[n - 1]; pp[n - 1] = tmp;
			}
		PrintWriter pw = new PrintWriter(System.out);
		pw.println("Shi");
		for (int i = 0; i < n; i++)
			pw.print(pp[i] + " ");
		pw.println();
		for (int i = 0; i < n; i++)
			pw.print(qq[i] + " ");
		pw.println();
		pw.close();
	}
}
