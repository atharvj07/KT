import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		sc.close();
		
		int num = a * (int)Math.pow(10, (int)Math.log10(b)+1) + b;
		int sqrt = (int)Math.sqrt(num);
		if(num == sqrt * sqrt)
			System.out.println("Yes");
		else
			System.out.println("No");
	}
}
