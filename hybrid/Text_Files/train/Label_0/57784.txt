import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), d = sc.nextInt();
		sc.close();
		String ans[] = {"Left", "Balanced", "Right"};
		int an = 0;
		a += b;
		c += d;
		if(a == c)an = 1;
		else if(a < c)an = 2;
		System.out.println(ans[an]);
	}

}
