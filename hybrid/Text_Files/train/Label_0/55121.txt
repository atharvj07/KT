import java.util.*;
import java.util.stream.*;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(IntStream.range(1, 10).anyMatch(i -> n % i == 0 && n / i <= 9) ? "Yes" : "No");
	}
}
