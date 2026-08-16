import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int d = sc.nextInt();
		int h = sc.nextInt();
		int v = sc.nextInt();
		int e = sc.nextInt();
		double res = 4 * v - e * Math.PI * d * d;
		if (res < 0) {
			System.out.println("NO");
		} else {
			System.out.println("YES");
			System.out.println(Math.PI * d * d * h / res);
		}
	}

}
