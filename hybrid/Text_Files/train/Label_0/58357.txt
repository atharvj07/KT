import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();

		int[] n = new int[N];

		for (int i = 0; i < K; i++){

			int d = sc.nextInt();

			for (int j = 0; j < d; j++){

				int su = sc.nextInt() - 1;

				n[su] = 1;
			}
		}

		int sum = 0;
		for (int sunu : n){
			if (!(sunu==1))
				sum ++;
		}

		System.out.println(sum);

	}

}
