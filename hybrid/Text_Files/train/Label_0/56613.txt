import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Solution {
	public static void main (String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 0; i < t; i++) {
			int a = in.nextInt();
			int b = in.nextInt();
			int c = in.nextInt();
			int d = in.nextInt();
			int x = in.nextInt();
			int y = in.nextInt();
			int x1 = in.nextInt();
			int y1 = in.nextInt();
			int x2 = in.nextInt();
			int y2 = in.nextInt();
			boolean bool = true;
			int hor = b - a;
			if (hor == 0) {
				if (a != 0 && x1 == x && x2 == x) bool = false;
			} else {
				hor += x;
				if (hor < x1 || hor > x2) bool = false;
			}
			int ver = d - c;
			if (bool && ver == 0) {
				if (c != 0 && y1 == y && y2 == y) bool = false;
			} else {
				ver += y;
				if (ver < y1 || ver > y2) bool = false;
			}
			System.out.println(bool ? "YES" : "NO");
		}
		in.close();
	}
}
