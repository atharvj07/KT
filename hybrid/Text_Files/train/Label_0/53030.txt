import java.util.Scanner;

public class ez {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int[] time = new int[5];
		int[] wrong = new int[5];
		for(int i = 0; i < 5; i++){
			time[i]=in.nextInt();
		}
		for(int i = 0; i < 5; i++){
			wrong[i]=in.nextInt();
		}
		double score =0;
		for(int i = 0; i < 5; i++){
			int value = 500+500*(i);
			score+=Math.max(.3*value, (1-(time[i]/250.0))*value-50*wrong[i]);
		}
		score+=100*in.nextInt();
		score-=50*in.nextInt();
		System.out.println((long)Math.round(score));
	}
}