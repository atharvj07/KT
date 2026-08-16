import java.util.Scanner;

public class p9 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int k = in.nextInt();
		for(int i = k+1; i > 0; i--)
			System.out.printf("%d ", i);
		for(int i = k+2; i <= n; i++)
			System.out.printf("%d ", i);
	}

}
