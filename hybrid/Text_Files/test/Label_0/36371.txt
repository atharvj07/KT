import java.util.Scanner;

public class Main4 {
	
	public static void main(String args[]){
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int total = sc.nextInt();
		int cnt = Math.min(n-1, total);
		int fuel = Math.min(n-1, total) - 1;
		//System.out.println("g " + cnt + "  " + fuel);
		for(int i=2;i<n;i++){
			if(n-i > fuel){
				cnt += Math.min(n-i-fuel, total-fuel)*i;
				fuel += Math.min(n-i-fuel, total-fuel);
				
				//System.out.println("g " + cnt + "  " + fuel + "  " + Math.min(n-i-fuel, total-fuel));
			}
			fuel--;
		}
		System.out.println(cnt);
		
	}
}
