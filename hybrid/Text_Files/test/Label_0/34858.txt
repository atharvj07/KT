import java.util.Scanner;

public class Main {
	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			int sum = 0;
			int bottom = 1;
			int count = 0;
			int i=1;
			while(i < n){
				if(sum <= n){
					sum += i++;
					if(sum == n){
						count++;
					}
				}
				else if(n < sum){
					for(int j=bottom;;j++){
						if(sum == n){
							count++;
							bottom = j;
							break;
						}
						else if(sum < n){
							bottom = j;
							break;
						}
						else sum -= j;
					}
				}
			}//end for
			System.out.println(count);
		}
	}
	public static void main(String[] args) {
		//new AOJ2197().run();
		new Main().run();
	}
}