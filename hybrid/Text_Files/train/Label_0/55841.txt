import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
	
	static int INF = 1000000000;
	static int MAXN = 31;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int[][] point = new int[n][2];
		for (int i = 0; i < n; ++i) {
			point[i][0] = input.nextInt();
			point[i][1] = input.nextInt();
		}
		int q = input.nextInt();
		for (int i = 0; i < q; ++i) {
			int x, y;
			x = input.nextInt();
			y = input.nextInt();
			System.out.println(checkWithPolygon(x, y, point));
		}
	}
	
	static int checkWithPolygon(int x, int y, int[][] pol) {
		boolean check = false;
		for (int i = 0; i < pol.length; ++i) {
			int ax = pol[i][0] - x, ay = pol[i][1] - y;
			int bx = pol[(i + 1) % pol.length][0] - x, by = pol[(i + 1) % pol.length][1] - y;
			if (ay > by) {
				int temp = ax; ax = bx; bx = temp;
				temp = ay; ay = by; by = temp;
			}
			if (ay <= 0 && by > 0 && cross(ax, ay, bx, by) < 0) check = !check;
			if (cross(ax, ay, bx, by) == 0 && dot(ax, ay, bx, by) <= 0) return 1;
		}
		return check ? 2 : 0;
	}
	
	static int cross(int ax, int ay, int bx, int by) {
		return ax * by - ay * bx;
	}
	
	static int dot(int ax, int ay, int bx, int by) {
		return ax * bx + ay * by;
	}
}