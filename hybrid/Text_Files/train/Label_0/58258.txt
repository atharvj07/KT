import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result = 0;
		int a = sc.nextInt(),b = sc.nextInt(),c = sc.nextInt();
		if(a != b) result++;
		if(a != c) result++;
		if(b != c) result++;
		if(a == b && b == c) result++;
		System.out.println(result);
	}
}