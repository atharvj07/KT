import java.util.Scanner;
class Main{
	public static void main(String[]$){

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		String S = sc.next();

		S = S.substring(0,K-1) + S.substring(K-1,K).toLowerCase() + S.substring(K,S.length());

		System.out.println(S);
	}
}
