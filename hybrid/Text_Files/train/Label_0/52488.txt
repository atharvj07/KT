import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		sc.close();
		A = A*N;
		if(A>=B) {
			System.out.println(B);
		}else {
			System.out.println(A);
		}
	}

}
