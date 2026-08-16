import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
    
		// 整数の入力
        int sum = sc.nextInt() + sc.nextInt();
        System.out.println(sum >= 10 ? "error" : sum);
	}
}
