import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();	//賞味期限+x+1日でお腹を壊す
		int a = sc.nextInt();	//賞味期限のa日前に買った
		int b = sc.nextInt();	//買ってからb日後に食べた
		
		if(b - a <= 0){
			//賞味期限内に食べた
			System.out.println("delicious");
		}else if(b - a <= x){
			//お腹は壊さない
			System.out.println("safe");
		}else{
			System.out.println("dangerous");
		}	
	}
}