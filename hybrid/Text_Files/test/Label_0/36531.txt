
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		int B = sc.nextInt();

		int sum = 0;
		for(int i = 0; i < 2; i++) {
			if(A < B) {
				sum += B;
				B--;
			}
			else {
				sum += A;
				A--;
			}

		}

		System.out.println(sum);
	}

}
