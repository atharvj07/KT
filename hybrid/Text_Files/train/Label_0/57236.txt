import java.util.Scanner;
public class Main {
	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		long sum = 0;



		for(int i = 1; i <= N; i++){
			for (int k = 1; k <= N; k++){
				for (int l = 1; l <= N; l++){

					int x = i;
					int y = k;
					int z = l;
					int tmp;

					while (x % y != 0){
						tmp = (x % y);
						x = y;
						y = tmp;
					}

					while (y % z != 0){
						tmp = (y % z);
						y = z;
						z = tmp;
					}

					sum += z;

				}
			}
		}

		System.out.print(sum);

	return;

	}
}
