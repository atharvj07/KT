
import java.util.Scanner;

class Main {

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();

		int[] c = new int[n];
		for (int i = 0; i < n; i++) {
			c[i] = in.nextInt();

		}
		int q = in.nextInt();
		for (int i = 0; i < q; i++) {

			if(solve(c,0,in.nextInt())) {
				System.out.println("yes");
			}else{
				System.out.println("no");
			};

		}

		in.close();
	}

	private static boolean solve(int[] c,int i, int m) {
		boolean res;
	   if (m == 0) {
	     return true;
	   }
	   if (i == c.length) {
	     return false;
	   }
	   res = solve(c,i + 1, m) || solve(c,i + 1, m - c[i]);
	   return res;
	}
}

