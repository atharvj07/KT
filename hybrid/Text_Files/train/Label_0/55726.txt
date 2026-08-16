import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		long N = in.nextInt();
		long A = in.nextInt();
		
		long buy = N % 500;
		if(buy<=A) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}
 
}