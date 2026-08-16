
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args){
		int i, n, m, a, b;
		TreeSet<Integer> setA = new TreeSet<Integer>();
		TreeSet<Integer> setB = new TreeSet<Integer>();
		try (Scanner sc = new Scanner(System.in)) {
			n = sc.nextInt();
			for(i = 0; i < n; i++) {
				a = sc.nextInt();
				setA.add(a);
			}
			m = sc.nextInt();
			for(i = 0; i < m; i++) {
				b = sc.nextInt();
				setB.add(b);
			}
			setA.removeAll(setB);
			for(int output : setA) {
				System.out.println(output);
			}
		}
	}
}

