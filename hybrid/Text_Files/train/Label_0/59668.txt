import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			//例 12=2*2*3=2^2 * 3^1
			//a=2^p * 3^q
			//b=2^t * 3^s
			//p, tが少なくとも一つ2である必要
			//p,tの並びは(2+1)*(2+1)
			//全部2でない並びは 2*2
			//よって少なくとも一つ2であるのは(2+1)*(2+1)-2*2
			//q,sも同様
			while (sc.hasNext()) {
				long L = sc.nextLong();
				if (L == 0) break;
				long ans = 1;
				for(long i=2; i*i<=L; i++) {
					if(L%i != 0) continue;
					L/=i;
					int count=1;
					while(L%i == 0) {
						L/=i;
						count++;
					}
					ans*=(count+1)*(count+1)-count*count;
				}
				if(L!=1) {
					ans*=2*2-1*1;
				}
				System.out.println((ans+1)/2);
			}
			
		}
	}
}
