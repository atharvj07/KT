import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int d = sc.nextInt();
		int n = sc.nextInt();
		int b = (int) Math.pow(100, d);
		int result = b * n;
		if(n % 100 == 0) result += b;
		System.out.println(result);
	}
}