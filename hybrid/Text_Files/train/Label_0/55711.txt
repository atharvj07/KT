import java.util.Scanner;

/**
 * https://abc059.contest.atcoder.jp/tasks/arc072_b
 */
public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		long x = sc.nextLong();
		long y = sc.nextLong();
		sc.close();
		
		String ans = Math.abs(x-y) <= 1 ? "Brown" : "Alice";
		System.out.println(ans);

	}

}
