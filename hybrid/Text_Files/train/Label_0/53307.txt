import java.util.*;

public class spalin
{

	public static void main(String[] ar)
	{
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		
		int half;
		
		if(str.length()%2 == 0 )
			half = str.length()/2;
		else
			half = str.length()/2+1;
			
		//System.out.println(half);
		for(int i=0;i<half; i++ )
		{	char x = str.charAt(i);
			char y = str.charAt(str.length() - i -1);
			if( x == y || (x=='b' && y =='d')||(x=='d' && y =='b')||(x=='q' && y =='p') ||(x=='p' && y =='q') )
			{
				if( (x=='b' && y =='d')||(x=='d' && y =='b')||(x=='q' && y =='p') ||(x=='p' && y =='q') )
				{
					
					
				}
				else
				{
					switch(x)
					{
						case 'A' :
						case 'H' :	
						case 'I' :	
						case 'M' :	
						case 'O' :
						case 'o' :	
						case 'T' :	
						case 'U' :
						case 'V' :
						case 'v' :	
						case 'W' :
						case 'w' :
						case 'X' :	
						case 'x' :
						case 'Y' :	break;
						default:   System.out.println("NIE");
									return;
					}
				}
			}
			else
			{
				System.out.println("NIE");
				return;
			}
		}	
		
		System.out.println("TAK");
	
	}

}