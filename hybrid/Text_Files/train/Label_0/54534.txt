import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		long x = sc.nextLong();
		long y = sc.nextLong();
		sc.close();
		long abs = Math.abs(Math.abs(x) - Math.abs(y));
		if(x * y < 0 || (x == 0 && y < 0) || (y == 0 && x > 0)){
            System.out.println(abs + 1);
        }else if((x > 0 && y > 0 && x > y) || (x < 0 && y < 0 && x > y)){
        	System.out.println(abs + 2);
        }else{
        	System.out.println(abs);
        }
	}
}
