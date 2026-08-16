import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	// 保存行、列的“*”数目
	private static int row[] = new int[50500];
	private static int col[] = new int[50500];
	// 二维数组
	private static ArrayList<int[]> aa = new ArrayList<>();

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		int n, m, ans;
		String s;
		char cs[];
		while (t-- > 0) {
			aa.clear();
			n = in.nextInt();
			m = in.nextInt();
			for (int i = 0; i < n; i++) {
				row[i] = 0;
			}
			for (int i = 0; i < m; i++) {
				col[i] = 0;
			}
			for (int i = 0; i < n; i++) {
				s = in.next();
				cs = s.toCharArray();
				int a[] = new int[m];
				for (int j = 0; j < m; j++) {
					if (cs[j] == '*') {
						row[i]++;
						col[j]++;
						a[j] = 1;
					} // 否则a[j]=0
				}
				aa.add(a);
			}
			ans = n + m - 1;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					int cur = row[i] + col[j] - aa.get(i)[j];
					ans = Math.min(ans, n + m - 1 - cur);
				}
			}
			System.out.println(ans);
		}
		in.close();
	}
}