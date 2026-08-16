
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

	Scanner sc = new Scanner(System.in);

	void run() {
		
		long n = sc.nextLong();
		
		System.out.println(solve(n));
		
	}
	
	long solve(long n){
		long x = n;
		int r = 0;
		
		long d1 = 1;
		boolean isNine = true;
		for(;x > 0;){
			if(x >= 10 && x % 10 != 9){
				isNine = false;
			}
			r += x % 10;
			x = x / 10;
			d1 *= 10;
		}
		d1 /= 10;
		if(d1 == 1){
			return n;
		}
		/*
		System.out.println(isNine);
		System.out.println(r);
		System.out.println(d1);
		*/
		if(isNine){
			return r;
		}
		
		return digitSum(d1-1 + (n/d1 - 1) * d1);
	}
	
	int digitSum(long n){
		int r = 0;
		for(;n > 0;){
			r += n%10;
			n /= 10;
		}
		return r;
	}
}
