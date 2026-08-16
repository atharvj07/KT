import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A[] = new int[N];
		String out = "";
		for(int i = 0; i < N; i++) {
			A[sc.nextInt()-1] = i + 1;
		}
		for(int i = 0; i < N; i++) {
			System.out.println(A[i]);
		}
		System.out.println(out);
		sc.close();
	}

}
