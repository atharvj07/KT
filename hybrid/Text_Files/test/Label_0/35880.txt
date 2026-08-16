
import java.util.*;
import java.lang.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	int MAX = 10005;
	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			int n = sc.nextInt(), r = sc.nextInt();
			if ((n|r) == 0) break;
			E[] G = new E[MAX];
			for (int i = 0; i < MAX;i++) G[i] = new E();
			for (int i=0;i<n;i++) {
				int x1 = sc.nextInt()+1, y1 = sc.nextInt()+1, x2 = sc.nextInt()+1, y2 = sc.nextInt()+1;
				G[y1].add(new P(x1, x2, true));
				G[y2].add(new P(x1, x2, false));
			}
			int a = 0, l = 0, t = 1, minx = MAX, maxx = 0;
			int[][] area = new int[2][MAX];
			for (E e: G) {
				fill(area[t], 0);
				for (P p: e) {
					area[t][p.x1] += p.c ? 1: -1; area[t][p.x2] += p.c ? -1 : 1;
					minx = min(minx, p.x1); maxx = max(maxx, p.x2);
				}
				for (int i = minx; i <= maxx; i++) {
					area[t][i] += area[t][i-1] + area[1-t][i] - area[1-t][i-1];
					if (area[t][i] > 0) a++;
					if (((area[t][i] | area[1-t][i]) != 0 ) && area[t][i] * area[1-t][i] == 0) l++;
					if (((area[t][i] | area[t][i-1]) != 0 ) && area[t][i] * area[t][i-1] == 0) l++;
				}
//				debug(area[t]);
				t ^= 1;
			}
			System.out.println(a);
			if (r == 2) System.out.println(l);
		}
	}
	
	class E extends ArrayList<P>{};
	
	class P {
		int x1, x2; boolean c;
		P(int x1, int x2, boolean c) {
			this.x1 = x1;
			this.x2 = x2;
			this.c = c;
		}
	}
	
	void debug(Object... os) {
		System.out.println(deepToString(os));
	}
	
	public static void main (String[] args) throws java.lang.Exception
	{
		new Main().run();
	}
}