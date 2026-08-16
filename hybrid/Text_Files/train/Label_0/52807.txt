import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int[] d = {Math.abs(a - b), Math.abs(b - c), Math.abs(c - a)};
		Arrays.sort(d);

		System.out.println(d[0] + d[1]);
	}
}