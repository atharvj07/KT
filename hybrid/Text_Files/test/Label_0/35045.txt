import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int ans = 0;
		if(n % 2 == 0){
			ans = (n / 2) * (n / 2);
		}else{
			ans = (n / 2 + 1) * (n / 2);
		}
		System.out.println(ans);
	}
}
