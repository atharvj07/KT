import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static boolean[] isPrime = new boolean[51001];
	static{
		Arrays.fill(isPrime, true);
		isPrime[0]=isPrime[1]=false;
		for(int i = 2; i*i<=isPrime.length; i++){
			if(isPrime[i]){
				for(int j = i+i; j < isPrime.length; j+=i){
					isPrime[j]=false;
				}
			}
		}
	}
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while(cin.hasNext()){
			int n = cin.nextInt();
			for(int i = n-1 ; i >= 0; i--){
				if(isPrime[i]){
					System.out.print(i+" ");
					break;
				}

			}

			for(int i = n+1 ; i < isPrime.length; i++){
				if(isPrime[i]){
					System.out.println(i);
					break;
				}
			}
		}
	}

}