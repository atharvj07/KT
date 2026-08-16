import java.util.Scanner;
import java.math.BigInteger;

public class Main{
    public static void main(String[] args){
	Scanner sc= new Scanner(System.in);
	int n=sc.nextInt();

	for(int i=0; i<n; i++){
	    BigInteger a,b,c;
	    a = sc.nextBigInteger();
	    b = sc.nextBigInteger();
	    c = a.add(b);
	    if(c.toString().length()<=80){
		System.out.println(c);
	    }else{
		System.out.println("overflow");
	    }
	}
    }
}