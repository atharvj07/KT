import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int sum = 0;
		int maxSub = 0;
		for (int i = 0; i < 5; i++) {
			int time = sc.nextInt();
			int sub = 10 - time % 10;
			if (sub == 10) {
				sub = 0;
			}
			sum += time + sub;
			if (sub > maxSub) {
				maxSub = sub;
			}
		}
		System.out.println(sum - maxSub);

		sc.close();
	}
}
