import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long m = sc.nextLong();
		long[] a = new long[n + 1];
		long gcd = 0;
		long lcm = 1;
		for(int i = 0 ; i < n ; i++) {
			a[i] = sc.nextLong() / 2;
			gcd = gcd(lcm , a[i]);
			lcm = lcm * a[i] / gcd;
			if(lcm > m) {
				System.out.println(0);
				return;
			}
		}
		for(int i = 0 ; i < n ; i++) {
			if((lcm / a[i]) % 2 == 0) {
				System.out.println(0);
				return;
			}
		}

		sc.close();
		System.out.println((m / lcm + 1 ) / 2);

	}
	public static long gcd(long num1,long num2) {
        if(num2 == 0) return num1;
        else return gcd(num2 , num1 % num2 );
 }
}

