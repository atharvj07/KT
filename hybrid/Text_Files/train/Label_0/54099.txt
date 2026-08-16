import java.util.Scanner ; 
public class A478_InitialBet {

	public static void main(String[] args) {
		Scanner ss =new Scanner (System.in) ; 
		int one = ss.nextInt() ; 
		int two = ss.nextInt() ; 
		int three = ss.nextInt() ; 
		int four = ss.nextInt() ; 
		int five = ss.nextInt() ; 
		int sum = one + two + three + four + five ; 
		if (sum%5 == 0 && sum!=0)
			System.out.println(sum/5);
		
		else 
			System.out.println(-1);
	}

}
