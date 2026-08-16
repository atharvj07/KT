import java.math.BigDecimal;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input[] = sc.nextLine().split(" ");
		BigDecimal A = new BigDecimal(input[0]);
		BigDecimal B = new BigDecimal(input[1]);
		System.out.println(A.multiply(B).longValue());
		sc.close();
	}
}
