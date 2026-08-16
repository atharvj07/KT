import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class submission{
	public static void main(String[] args) throws IOException
	{
		BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
		int num=Integer.parseInt(input.readLine());
		String home=input.readLine();
		String[][] string=new String[num][2];
		for(int i=0;i<num;++i)
		{
			String tmp=input.readLine();
			string[i][0]=tmp.substring(0,3);
			string[i][1]=tmp.substring(5);
		}
		int flag=1;
		for(int i=0;i<num;++i)
		{
			flag=1;
			for(int j=0;j<num;++j)
			{

				if(string[j][0].equals(string[i][1])==true && string[j][1].equals(string[i][0])==true)
				{
					string[j][0]="*";
					string[j][1]="*";
					string[i][0]="*";
					string[i][1]="*";
					flag=0;
					break;
				}
			}
			if(flag==1)
			{
				break;
			}
		}
		if(flag==1)
		{
			System.out.println("contest");
		}
		else
		{
			System.out.println("home");
		}
	}
}