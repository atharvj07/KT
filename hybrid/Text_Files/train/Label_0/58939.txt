import java.util.*;
import java.lang.*;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int w = sc.nextInt();
		String[] s = new String[h];
		for (int i = 0; i < h; i++) {
			s[i] = sc.next();
		}
		int[][] u = new int[h][w];
		int[][] r = new int[h][w];
		int[][] d = new int[h][w];
		int[][] l = new int[h][w];
		for (int i = 0; i < h; i++) {
			int tmp = 0;
			for (int j = 0; j < w; j++) {
				if (s[i].charAt(j) == '.') {
					tmp++;
				} else {
					tmp = 0;
				}
				l[i][j] = tmp;
			}
		}
		for (int i = 0; i < h; i++) {
			int tmp = 0;
			for (int j = w - 1; j >= 0; j--) {
				if (s[i].charAt(j) == '.') {
					tmp++;
				} else {
					tmp = 0;
				}
				r[i][j] = tmp;
			}
		}
		for (int i = 0; i < w; i++) {
			int tmp = 0;
			for (int j = 0; j < h; j++) {
				if (s[j].charAt(i) == '.') {
					tmp++;
				} else {
					tmp = 0;
				}
				u[j][i] = tmp;
			}
		}
		for (int i = 0; i < w; i++) {
			int tmp = 0;
			for (int j = h - 1; j >= 0; j--) {
				if (s[j].charAt(i) == '.') {
					tmp++;
				} else {
					tmp = 0;
				}
				d[j][i] = tmp;
			}
		}
		int ans = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				ans = Math.max(ans, u[i][j] + r[i][j] + d[i][j] + l[i][j] - 3);
			}
		}
		System.out.println(ans);
	}
}
