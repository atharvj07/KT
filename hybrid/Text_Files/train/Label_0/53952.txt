

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		long result = 0;
		for(int i = 1; i <= n; i++){
			int l = n / i * i;

			result += ((long)n / i) * (i + l) / 2;
		}

		System.out.println(result);
	}
}