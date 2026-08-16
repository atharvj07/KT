import java.io.*;
import java.util.*;

public class A {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		
		int[] a = new int[n];
		for(int i=0; i<n; i++) {
			a[i] = in.nextInt();
		}
		
		Solver A = new Solver(a, n);
		A.solve();
		//System.out.println(A.solve());
	}

}

class Solver {
	int[] a;
	int n;
	int t;
	public Solver(int[] a, int n) {
		this.a = a;
		this.n = n;
		for(int i=0; i<n; i++) {
			if(a[i] == 0) t++;
		}
	}
	
	public void solve() {
		if(n == 1) {
			if(a[0] == 0) {
				System.out.println("YES\n0");
				return;
			}
			else {
				System.out.println("NO");
				return;
			}
		}
		
		if(a[n-1] == 1 || a[n-2] == 0 && t == 2) {
			System.out.println("NO");
			return;
		}
		
		System.out.println("YES");
		fi(0, n - 2, "");
		//res += "" + fi(0, n - 2, "");
		System.out.println("->0");
	}
	
	private void fi(int cur, int nn, String aa) {
		if(nn == 0) {
			System.out.print("" + a[cur]);
			//String aaa = "" + a[cur];
			//return aaa;
		}
		else {
			System.out.print("(" + a[cur] + "->");
			fi(cur + 1, nn - 1, aa);
			System.out.print(")");
			//aa += "(";
			//aa += a[cur];
			//aa += "->";
			//aa += fi(cur + 1, nn - 1, aa);
			//aa += ")";
			//return aa;
		}
	}
}
