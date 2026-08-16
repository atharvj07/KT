import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = input.nextInt();
		int M = input.nextInt();
		int cnt = 0;
		System.out.println(N*(N-1)/2+M*(M-1)/2);
	}
}