import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int q = sc.nextInt();
		int array[] = new int [q];
		for(int i = 0;i < q;i++){
			array[i] = sc.nextInt() - 1;
		}
		int countarray[] = new int [n];

		for(int i = 0;i < q;i++){
				countarray[array[i]]++;
		}
		for(int i = 0;i < n;i++){
			if((k - q + countarray[i]) > 0){
				System.out.println("Yes");
			}else{
				System.out.println("No");
			}
		}
	}
}