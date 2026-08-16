

import java.util.Scanner;
import java.util.TreeSet;

public class ProblemA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		TreeSet<Integer> set = new TreeSet<>();
		for(int i = 1; i <= m; i++) {
			set.add(i);
		}
		
		for(int i = 0; i < n; i++) {
			int l = sc.nextInt();
			int r = sc.nextInt();
			for(int j = l; j <= r; j++) {
				if(set.contains(j)) set.remove(j);
			}
		}
		
		System.out.println(set.size());
		for(int x: set) {
			System.out.print(x + " ");
		}

	}

}
