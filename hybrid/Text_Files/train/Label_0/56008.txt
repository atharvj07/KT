import java.util.Scanner;

public class good_string {

	public static void main(String[] args) {
		// TODO Auto-generated method stub                                                                                                                                

		Scanner s = new Scanner(System.in);
		int t=s.nextInt();
		for(int j=0;j<t;j++)
		{
			int n=s.nextInt();
		String str = s.next();
		int c1=-1;
		int c2=-1;
		for(int k=0;k<str.length();k++)
		{
			if(str.charAt(k)=='<')
				c1=k;
		}
		for(int k=0;k<str.length();k++)
		{
			if(str.charAt(k)=='>')
			{
				c2=k;
               break;
           }
		}
		
		int k1 = str.length()-c1;
		int k2 = c2+1;
		
		
		if(c1==-1)
			System.out.println(k2-1);
		else if(c2==-1)
			System.out.println(k1-1);
		else
			System.out.println(Integer.min(k1, k2)-1);
		}}}