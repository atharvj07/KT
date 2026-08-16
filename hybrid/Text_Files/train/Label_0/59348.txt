import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();

		long min = (long)A*(N-1)+B;
		long max = A+(N-1)*(long)B;
		System.out.println(Math.max(0, max-min+1));
		
		sc.close();
	}
}
