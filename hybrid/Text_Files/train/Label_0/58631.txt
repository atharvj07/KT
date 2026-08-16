import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), k = sc.nextInt();
		for(int i=a; i<=b; i++){
			if(Math.abs(i-a)<k || Math.abs(i-b)<k){
				System.out.println(i);
			}else{
				i = b-k;
			}
		}
	}
}