import java.util.Scanner;

public class Main2 {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		long counter = 1;
		int count = 1;
		int sum = Character.digit(s.charAt(0), 10);
		for(int i = 1 ; i < s.length() ; i++){
			sum += Character.digit(s.charAt(i), 10);
			if(sum == 9){
				count++;
			}else{
				if(count % 2  == 1){
					counter *= (count+1)/2;
				}
				count = 1;
			}
			sum = Character.digit(s.charAt(i), 10);
		}
		if(count % 2  == 1){
			counter *= (count+1)/2;
		}
		System.out.println(counter);
	}
}