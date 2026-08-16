import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a=scan.nextInt();
		int ans=0;
		for(int i=0;i!=4;i++){
			int b=a%10;
			a/=10;
			if(b==2) {ans++;}
		}
		System.out.println(ans);
    }
}