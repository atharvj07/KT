import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] ant = new int[5];
		int dis = 0;

		for(int i = 0; i < 5; i++) {
			ant[i] = sc.nextInt();
		}
		dis = sc.nextInt();

		for(int i = 0; i < 4; i++) {
			for(int j = i + 1; j < 5; j++) {
				if(ant[j] - ant[i] > dis) {
					System.out.println(":(");
					System.exit(0);
				}
			}
		}
		System.out.println("Yay!");
	}
}