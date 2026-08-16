import java.util.*;

public class e{
	static long gcd(long a, long b){
		return b == 0? a: gcd(b, a % b);
	}
	// okay
	// i see why i got hacked
	// i only considered the SMALLEST factor of x
	// i should really consider ALL factors of x
	
	static long f(long x, long y){
		if(y == 0) return 0;
		if(x == 1 || y == 1) return y;
		long gcd = gcd(x,y);
		if(gcd > 1){
			x /= gcd;
			y /= gcd;
		}
		
		// smallest factor of f?
		long diff = Long.MAX_VALUE;
		long fac, temp;
		for(fac = 2, temp = x; fac*fac <= temp; fac++){
			if(temp % fac == 0){
				diff = Math.min(diff, y % fac);
				while(temp % fac == 0){
					temp /= fac;
				}
			}
		}
		if(temp != 1 && fac*fac > temp){
			diff = Math.min(diff, y % temp);
		}
		
		return diff + f(x, y - diff);
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		long X = in.nextLong();
		long Y = in.nextLong();
		
		System.out.println(f(X,Y));
	}
}