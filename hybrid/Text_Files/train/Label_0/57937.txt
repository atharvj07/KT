
import java.util.Scanner;

public class DigitalRoot {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int digits[] = new int[9];
		long result = 0;
		for (int i = 1; i <= n; i++) {
			digits[i%9]++;
			result -= (n/i);
		}
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				result += 1L*digits[i]*digits[j]*digits[(i*j)%9];
			}
		}
		System.out.println(result);
	}

}
