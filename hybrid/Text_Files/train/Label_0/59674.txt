import java.util.Scanner;

public class Main {

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = n%10;
		if(k==3)System.out.println("bon");
		else if(k==0 || k==1 || k==6 || k==8)System.out.println("pon");
		else System.out.println("hon");
	}

}
