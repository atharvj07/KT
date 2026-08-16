import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = Integer.parseInt(sc.next());
		int B = Integer.parseInt(sc.next());
		int C = Integer.parseInt(sc.next());
		int K = Integer.parseInt(sc.next());
		sc.close();

		for(int i = 1; i <= K; i++) {
			int tmp = Math.max(Math.max(A, B), C);
			if(tmp == A) {
				A *= 2;
			}else if(tmp == B) {
				B *= 2;
			}else {
				C *= 2;
			}
		}
		int sum = A + B + C;
		System.out.println(sum);
	}

}