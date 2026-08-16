import java.util.Scanner;
public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Main me = new Main();
		while(in.hasNext()){
			long a = in.nextInt(),b = in.nextInt();
			long gcd = me.GCD(a,b);
			System.out.printf("%d %d\n",gcd,a*b/gcd);
			
		}
	}
	private long GCD(long a,long b){
		if(b == 0)
			return a;
		else
			return GCD(b,a%b);
	}
}