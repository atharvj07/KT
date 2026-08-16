import java.util.Scanner;

public class Main {
	Scanner sc = new Scanner(System.in);

	void run() {
		for (;;) {
			int q1 = sc.nextInt();
			if (q1 == 0) return;
			int b = sc.nextInt();
			int c1 = sc.nextInt();
			int c2 = sc.nextInt();
			int q2 = sc.nextInt();

			int aizCnt = 0;
			int norCnt = 0;

			aizCnt = Math.min(b / c1, q2);
			b -= aizCnt * c1;
			norCnt += b / c2;
			b -= norCnt * c2;
			while (aizCnt + norCnt < q1 && 1 < aizCnt--) {
				b += c1;
				norCnt += b / c2;
				b -= (b / c2) * c2;
			}
			System.out.println((aizCnt == 0 || aizCnt + norCnt < q1) ? "NA" : (aizCnt + " " + norCnt));
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}