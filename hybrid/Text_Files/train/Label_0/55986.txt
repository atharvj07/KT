import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ

		Scanner sc = new Scanner(System.in);
		//入力表示

		double a = sc.nextInt();
		double b = sc.nextInt();
		double h = sc.nextInt();
		double m = sc.nextInt();

		double rad = Math.PI * 2 * (h / 12.0 + (m / 60.0) / 12.0 - m / 60.0);

		double rsq = Math.sqrt((a * a + b * b) - (2 * a *
				b) * Math.cos(rad));

		System.out.printf("%.20f", rsq);

	}
}