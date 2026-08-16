import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);
		// 整数の入力
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = A + B;
		if (C >= 24) {
			C = C - 24;
		}
		// 出力
		System.out.println(C);
	}
}
