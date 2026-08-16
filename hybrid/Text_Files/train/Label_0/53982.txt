//Referred professors code
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Fenwick{		
	static int[] fenwick;
	static final int Z = 1000000000;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		List<V> list = new ArrayList<>();

		for (int i=0; i<n; i++) {
			int k = Integer.parseInt(br.readLine());
			int[] xx = new int[k];
			int[] yy = new int[k];

			StringTokenizer st;

			for (int j = 0; j < k; j++) {
				st=new StringTokenizer(br.readLine());
				xx[j] = Integer.parseInt(st.nextToken());
				yy[j] = Integer.parseInt(st.nextToken());
			}

			for (int j=0; j<k; j++) {
				int j1 = (j + 1) % k;
				int x = xx[j1] - xx[j], y = yy[j1] - yy[j];
				int d = GCD(Math.abs(x), Math.abs(y)); x /= d; y /= d;
				list.add(new V(x, y, i));
			}
		}
		Collections.sort(list, (i, j) -> i.z == j.z ? j.i - i.i : i.z < j.z ? -1 : 1);

		int m = list.size();
		V[] vv = list.toArray(new V[m]);
		for (int i = 0; i < m; i++)
			vv[i].i1 = i == 0 || vv[i].z != vv[i - 1].z ? -1 : vv[i - 1].i;

		Arrays.sort(vv, (i,j) -> j.i - i.i);

		int q = Integer.parseInt(br.readLine());

		int[] ll = new int[q];
		int[] rr = new int[q];
		int[] res = new int[q];

		Integer[] ii = new Integer[q];

		StringTokenizer st;
		for (int h = 0; h < q; h++) {
			st=new StringTokenizer(br.readLine());
			ll[h] = Integer.parseInt(st.nextToken())-1;
			rr[h] = Integer.parseInt(st.nextToken())-1;
			ii[h] = h;
		}

		Arrays.sort(ii, (i,j) -> ll[j] - ll[i]);

		fenwick = new int[n];

		for (int j=0, h=0; h<q; ) {
			int l = ll[ii[h]];
			while (j < m && vv[j].i >= l) {
				if (vv[j].i1 != -1)
					update(vv[j].i1, n, -1);
				update(vv[j].i, n, 1);
				j++;
			}
			while (h<q && ll[ii[h]] == l) {
				int r = rr[ii[h]];
				res[ii[h]] = query(r);
				h++;
			}
		}
		for (int j=0; j<q; j++)
			System.out.println(res[j]);
	}
	static int GCD(int a, int b) {
		return b == 0 ? a : GCD(b, a % b);
	}
	//Fenwick implementation
	static void update(int i, int n, int x) {
		while (i < n) {
			fenwick[i] += x;
			i|=i+1;
		}
	}
	static class V {
		long z;
		int i, i1;
		V(int x, int y, int i) {
			z = 2L * Z * (x + Z) + (y + Z);
			this.i = i;
		}
	}
	static int query(int i) {
		int s = 0;
		while (i >= 0) {
			s += fenwick[i];
			i &= i + 1;
			i--;
		}
		return s;
	}
}
