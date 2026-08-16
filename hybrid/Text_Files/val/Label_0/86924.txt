/*
	submission # - User: herp_sy
	https://atcoder.jp/contests/
*/

import java.util.*;
import java.util.Collections; // sorting use
import java.io.*;
import static java.lang.System.*;

public class Main{
	public static void main(String[] args){
		int n,x;
		ArrayList<Integer> m = new ArrayList<Integer>();
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		x = sc.nextInt();
		for (int i = 0; i < n; ++i){
			m.add(sc.nextInt());
			x -= m.get(i);
		}
		out.println(n + x / Collections.min(m));
	}
}
