import java.util.Scanner;

class Main{

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int[] data = new int[N];
		int sum= 0;
		for(int i =0;i < N;i++){
			data[i] = scan.nextInt();
		}
		for(int i=0;i<N;i++){
			while(data[i]%2 ==0){
				sum++;
				data[i] /= 2;
			}
		}

		System.out.println(sum);

	}





}