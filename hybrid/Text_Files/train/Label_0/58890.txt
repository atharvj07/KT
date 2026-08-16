import java.util.Scanner;
public class Main {

	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		
		String xi[] = new String[n];
		String bi[] = new String[n];
		String ci[] = new String[n];
		
		int x = scan.nextInt();
		for(int i = 0 ; i < x ; i++) {
			int num = scan.nextInt();
			xi[num-1] = "A";
		}
		int b = scan.nextInt();
		for(int i = 0 ; i < b ;i++) {
			int num = scan.nextInt();
			bi[num-1] = "B";
		}
		int c = scan.nextInt();
		for(int i = 0 ; i < c ;i++) {
			int num = scan.nextInt();
			ci[num-1] = "C";
		}
		
		int count = 0;
		
		for(int i = 0 ; i < n ; i++) {
			if(xi[i] == null && ci[i] == "C") {
				++count;
			}else if(bi[i] == "B" && ci[i] == "C"){
				++count;
			}
		}
		System.out.println(count);
	}
}

