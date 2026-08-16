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
		boolean ok = true;
		for (int i = 1; i < n - 2; ++i) {
			int ccw1 = ccw(point[i - 1], point[i], point[i + 1]);
			int ccw2 = ccw(point[i], point[i + 1], point[i + 2]);
			if (ccw1 * ccw2 < 0) {
				ok = false;
				break;
			}
		}
		int ccw1 = ccw(point[n - 2], point[n - 1], point[0]);
		int ccw2 = ccw(point[n - 1], point[0], point[1]);
		if (ccw1 * ccw2 < 0) {
			ok = false;
		}
		if (ok) System.out.println(1);
		else System.out.println(0);
	}
	
	static int ccw(int[] p1, int[] p2, int[] p3) {
		int a1, b1;
		int a2, b2;
		a1 = p2[0] - p1[0];
		b1 = p2[1] - p1[1];
		a2 = p3[0] - p2[0];
		b2 = p3[1] - p2[1];
		return a1 * b2 - a2 * b1;
	}
}