import java.util.Scanner;
public class Main
{
	public static void main(String[] args) 
	{
		Scanner in=new Scanner(System.in);
		while(in.hasNext())
		{
			char ch[]=in.nextLine().toCharArray();
			String st="";
			String ans="";
			for(int i=0;i<ch.length;i++)
			{
				if(ch[i]=='A')
					st+="00000";
				else if(ch[i]=='B')
					st+="00001";
				else if(ch[i]=='C')
					st+="00010";
				else if(ch[i]=='D')
					st+="00011";
				else if(ch[i]=='E')
					st+="00100";
				else if(ch[i]=='F')
					st+="00101";
				else if(ch[i]=='G')
					st+="00110";
				else if(ch[i]=='H')
					st+="00111";
				else if(ch[i]=='I')
					st+="01000";
				else if(ch[i]=='J')
					st+="01001";
				else if(ch[i]=='K')
					st+="01010";
				else if(ch[i]=='L')
					st+="01011";
				else if(ch[i]=='M')
					st+="01100";
				else if(ch[i]=='N')
					st+="01101";
				else if(ch[i]=='O')
					st+="01110";
				else if(ch[i]=='P')
					st+="01111";
				else if(ch[i]=='Q')
					st+="10000";
				else if(ch[i]=='R')
					st+="10001";
				else if(ch[i]=='S')
					st+="10010";
				else if(ch[i]=='T')
					st+="10011";
				else if(ch[i]=='U')
					st+="10100";
				else if(ch[i]=='V')
					st+="10101";
				else if(ch[i]=='W')
					st+="10110";
				else if(ch[i]=='X')
					st+="10111";
				else if(ch[i]=='Y')
					st+="11000";
				else if(ch[i]=='Z')
					st+="11001";
				else if(ch[i]==' ')
					st+="11010";
				else if(ch[i]=='.')
					st+="11011";
				else if(ch[i]==',')
					st+="11100";
				else if(ch[i]=='-')
					st+="11101";
				else if(ch[i]=='\'')
					st+="11110";
				else if(ch[i]=='?')
					st+="11111";
			}
			char ch2[]=st.toCharArray();
			String tmp="";
			for(int i=0;i<ch2.length;i++)
			{
				tmp+=ch2[i];
				if(tmp.equals("101"))
				{
					ans+=" ";
					tmp="";
				}
				else if(tmp.equals("000000"))
				{
					ans+="'";
					tmp="";
				}	
				else if(tmp.equals("000011"))
				{
					ans+=",";
					tmp="";
				}
				else if(tmp.equals("10010001"))
				{
					ans+="-";
					tmp="";
				}
				else if(tmp.equals("010001"))
				{
					ans+=".";
					tmp="";
				}
				else if(tmp.equals("000001"))
				{
					ans+="?";
					tmp="";
				}
				else if(tmp.equals("100101"))
				{
					ans+="A";
					tmp="";
				}
				else if(tmp.equals("10011010"))
				{
					ans+="B";
					tmp="";
				}
				else if(tmp.equals("0101"))
				{
					ans+="C";
					tmp="";
				}
				else if(tmp.equals("0001"))
				{
					ans+="D";
					tmp="";
				}
				else if(tmp.equals("110"))
				{
					ans+="E";
					tmp="";
				}
				else if(tmp.equals("01001"))
				{
					ans+="F";
					tmp="";
				}
				else if(tmp.equals("10011011"))
				{
					ans+="G";
					tmp="";
				}
				else if(tmp.equals("010000"))
				{
					ans+="H";
					tmp="";
				}
				else if(tmp.equals("0111"))
				{
					ans+="I";
					tmp="";
				}
				else if(tmp.equals("10011000"))
				{
					ans+="J";
					tmp="";
				}
				else if(tmp.equals("0110"))
				{
					ans+="K";
					tmp="";
				}
				else if(tmp.equals("00100"))
				{
					ans+="L";
					tmp="";
				}
				else if(tmp.equals("10011001"))
				{
					ans+="M";
					tmp="";
				}
				else if(tmp.equals("10011110"))
				{
					ans+="N";
					tmp="";
				}
				else if(tmp.equals("00101"))
				{
					ans+="O";
					tmp="";
				}
				else if(tmp.equals("111"))
				{
					ans+="P";
					tmp="";
				}
				else if(tmp.equals("10011111"))
				{
					ans+="Q";
					tmp="";
				}
				else if(tmp.equals("1000"))
				{
					ans+="R";
					tmp="";
				}
				else if(tmp.equals("00110"))
				{
					ans+="S";
					tmp="";
				}
				else if(tmp.equals("00111"))
				{
					ans+="T";
					tmp="";
				}
				else if(tmp.equals("10011100"))
				{
					ans+="U";
					tmp="";
				}
				else if(tmp.equals("10011101"))
				{
					ans+="V";
					tmp="";
				}
				else if(tmp.equals("000010"))
				{
					ans+="W";
					tmp="";
				}
				else if(tmp.equals("10010010"))
				{
					ans+="X";
					tmp="";
				}
				else if(tmp.equals("10010011"))
				{
					ans+="Y";
					tmp="";
				}
				else if(tmp.equals("10010000"))
				{
					ans+="Z";
					tmp="";
				}
			}
			System.out.println(ans);
		}
	}
}