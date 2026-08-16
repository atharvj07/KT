import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		
		while(stdIn.hasNext()){
			int n = stdIn.nextInt();
			int ans = 2;
			for(int i=2;i<=n;i++){
				ans+=i;
			}
			System.out.println(ans);
		}
	}
}