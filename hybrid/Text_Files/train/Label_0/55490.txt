import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt(),b=sc.nextInt(),c=sc.nextInt();
		if((a==b&&b!=c)||(a==c&&b!=c)||(b==c&&a!=b)){
			System.out.println("Yes");
		}
		else System.out.println("No");
	}
}