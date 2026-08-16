import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long a = sc.nextLong();
		long b = sc.nextLong();
		long ans ;
		if((b-a)%2==0) {
			ans = (b-a)/2;
		}
		else {
			ans = Math.min(a-1, n-b)+(b-a)/2+1;
		}
		System.out.println(ans);
	}
}