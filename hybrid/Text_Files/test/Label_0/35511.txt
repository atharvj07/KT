import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		sc.close();
		
		Set<Integer> A = new HashSet<Integer>(Arrays.asList(1, 3, 5, 7, 8, 10, 12));
		Set<Integer> B = new HashSet<Integer>(Arrays.asList(4, 6, 9, 11));
		Set<Integer> C = new HashSet<Integer>(Arrays.asList(2));
		
		if(A.contains(x) && A.contains(y)
			|| B.contains(x) && B.contains(y)
			|| C.contains(x) && C.contains(y)) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}
