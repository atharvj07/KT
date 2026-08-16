import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int m=in.nextInt(),f=in.nextInt(),b=in.nextInt();
		int d=m-b,da=Math.abs(d);

		if(d>=0)System.out.println(0);
		else if(da>f)System.out.println("NA");
		else System.out.println(da);

		in.close();
	}

}

