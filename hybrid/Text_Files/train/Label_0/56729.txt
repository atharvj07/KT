import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int f[] = new int[N +1];
		for(int x = 1 ; x <= 100 ; ++x){
			for(int y = 1 ; y <= 100 ; ++y){
				for(int z = 1 ; z <= 100 ; ++z){
					int n = x * x + y * y + z * z + x * y + y * z + z * x;
					if(n < f.length){
						f[n]++;
					}
				}	
			}			
		}
		for(int i = 1 ; i <= N ; ++i){
			System.out.println(f[i]);
		}
	}
}