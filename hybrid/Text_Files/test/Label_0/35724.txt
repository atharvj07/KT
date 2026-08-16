import java.util.*;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	String table[];

	void run() {
		Scanner sc = new Scanner(System.in);
		for (;;) {
			int R = sc.nextInt();
			int C = sc.nextInt();
			if (R == 0 && C == 0)
				break;
			table = new String[R];
			for (int r = 0; r < R; r++) {
				table[r] = sc.next();
			}
			System.out.println(solve(R, C));
		}
	}

	int LargestRect(int a[]) {
		int best = 0;
		Stack<Integer> pos = new Stack<Integer>();
		Stack<Integer> height = new Stack<Integer>();

		pos.add(-1);
		height.add(-1);
		for (int i = 0; i < a.length; i++) {
			if (height.peek() <= a[i]) {
				pos.add(i);
				height.add(a[i]);
			} else {
				int last_pos = -1;
				while (height.peek() > a[i]) {
					best = Math.max(best, (height.peek()) * (i - pos.peek()));
					height.pop();
					last_pos = pos.pop();
				}
				pos.add(last_pos);
				height.add(a[i]);
			}
		}
		return best;
	}

	int solve(int R, int C) {
		int temp[][] = new int[R][C];
		for (int c = 0; c < C; c++) {
			int len = 0;
			for (int r = 0; r < R; r++) {
				if (table[r].charAt(c) == '.')
					len++;
				else
					len = 0;
				temp[r][c] = len;
			}
		}
		int a[] = new int[C + 1];
		a[C] = -1;
		int res = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++)
				a[c] = temp[r][c];
			res = Math.max(res, LargestRect(a));
		}
		return res;
	}
}