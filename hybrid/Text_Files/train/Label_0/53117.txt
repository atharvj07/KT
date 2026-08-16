import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		double ans=100000;
		for(int i=0;i<n;i++){
			ans=ans*1.05;
			if(ans%1000!=0){
				ans=ans+1000-ans%1000;
			}
		}
		int a=(int)ans;
		System.out.println(a);
	}
}