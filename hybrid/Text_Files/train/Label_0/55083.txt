import java.util.Scanner;
class Main{
	public static void main(String[] a){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			int n = scan.nextInt();
			int sum = 0;
			if(n > 36) System.out.println(0);
			else{
				for(int i = 0; i <= 9; i++){
					for(int j = 0; j <= 9; j++){
						for(int k = 0; k <= 9; k++){
							for(int l = 0; l <= 9; l++){
								if(i+j+k+l == n) sum++;
							}
						}
					}
				}
				System.out.println(sum);
			}
		}
	}
}