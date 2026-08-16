import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int l=sc.nextInt(),r=sc.nextInt();
		sc.close();
		if(r-l>=2018) System.out.println(0);
		else {
			long min=2018;
			for(int i=l;i<r;i++) {
				for(int j=i+1;j<=r;j++) {
					long temp =(long)i*j;
					long mod = temp%2019;
					if(mod<min) min=mod;
				}
			}
			System.out.println(min);
		}
	}
}