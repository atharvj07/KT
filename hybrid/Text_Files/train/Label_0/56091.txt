import java.util.Scanner;

public class R425P1 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		long n = scan.nextLong(), k = scan.nextLong();
		if((n/k)%2==0) System.out.println("NO");
		else System.out.println("YES");
	}
}