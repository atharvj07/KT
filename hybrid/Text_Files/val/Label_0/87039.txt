import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int sum = 0;
		int max = 0;

		int pre[] = new int[N];

		for(int i = 0; i < N; i++) {
			pre[i] = sc.nextInt();

			if(max < pre[i]) {

				max = pre[i];
			}
			sum += pre[i];
		}


		sum-= (int)max/2;


		System.out.println(sum);

	}

}
