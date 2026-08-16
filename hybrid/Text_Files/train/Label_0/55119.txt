

import java.util.Scanner;

public class Main {

	static int n, m, sum;// sum记录有没有找到,找到了为1,没找到为0
	static int[] xx = { 0, 0, -1, 1 };
	static int[] yy = { -1, 1, 0, 0 };
	static char[][] arr;
	static boolean[][] vis;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new char[n][m];
		vis = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.next().toCharArray();
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				//把这个起点置为true,如果以此起点找不到环,说明这一点肯定不参与形成环的一部分,那么下一次也就不用搜这个点
				vis[i][j] = true;
				dfs(i, j, i, j, 1, arr[i][j]);
				if (sum != 0) {// 只要找到了就退出循环
					break;
				}
			}
			if (sum != 0) {
				break;
			}
		}
		if (sum == 0) {// 没找到输出No
			System.out.println("No");
		}
	}

	public static void dfs(int x, int y, int i, int j, int index, char c) {
		if (sum != 0) {
			return;
		}
		for (int k = 0; k < 4; k++) {
			if (sum != 0) {
				return;
			}
			int row = x + xx[k];
			int col = y + yy[k];
			if (index >= 4 && row == i && col == j && sum == 0) {// 只有个数大于等于4,而且碰到了一开始的点才说明找到环
				sum = 1;
				System.out.println("Yes");
				return;
			}
			if (row >= 0 && row < n && col >= 0 && col < m && !vis[row][col] && arr[row][col] == c) {
				vis[row][col] = true;
				dfs(row, col, i, j, index + 1, c);
				if (sum != 0) {//只要找到了环就不用管他回溯不回溯了,只要输出Yes就完事儿
					return;
				}
				//当然没找到还是要回溯的
				vis[row][col] = false;// 回溯
				index--;// 回溯
				
			}
		}
	}
}
