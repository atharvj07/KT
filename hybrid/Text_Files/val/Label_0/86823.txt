import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		PrintWriter out=new PrintWriter(System.out);
		String str1=in.next(),str2=in.next();
		str1+=str1;
		if(str1.indexOf(str2)!=-1)out.println("Yes");
		else out.println("No");
		out.flush();
	}

}

