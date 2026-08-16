import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int progA[] = new int[n];
		int progB[] = new int[n];
		for(int i = 0; i < n; i++) {
			progA[i] = sc.nextInt();
		}
		int q = sc.nextInt();

		for(int i = 0; i < q; i++) {
			int b = sc.nextInt();
			int e = sc.nextInt();
			int t = sc.nextInt();
			for(int k = 0; k < e - b; k++) {
				progB[b + k] = progA[b + k];
				progA[b + k] = progA[t + k];
				progA[t + k] = progB[b + k];
			}
		}
		for(int j = 0; j < progA.length; j++) {
			if(j != 0) System.out.print(" ");
			System.out.print(progA[j]);
		}
		System.out.println();
	}

}

