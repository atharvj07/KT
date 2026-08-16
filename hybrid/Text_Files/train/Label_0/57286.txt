import java.util.*;
//import java.util.stream.Collectors;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int a = Integer.parseInt(sc.next());
		int b = Integer.parseInt(sc.next());
		int c = Integer.parseInt(sc.next());
		int k = Integer.parseInt(sc.next());
		for(int i=0; i<k; i++){
			if(b >= c){
				c *= 2;
			}else if(a >= b){
				b *= 2;
			}
		}
		System.out.println(a < b && b < c ? "Yes" : "No");
	}
}
