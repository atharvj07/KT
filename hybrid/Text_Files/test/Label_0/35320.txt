import java.util.*;
 
public class Main {
 	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String str = sc.next();
		if(N>=3200){
			System.out.println(str);
		}else{
			System.out.println("red");
		}
	}
}