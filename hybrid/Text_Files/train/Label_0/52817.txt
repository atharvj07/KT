import java.util.*;
import java.io.*;
public class A
{
	public static void main (String[] args) 
	{
		Scanner s=new Scanner(System.in);
		int N=s.nextInt();
		int K=s.nextInt();
		s.nextLine();
		char C1[]=s.nextLine().toCharArray();
		
		Arrays.sort(C1);
		int L1=C1.length;
		
		String S=""+C1[0];
		for(int i=1;i<L1;i++)
		{
		    if(C1[i]!=C1[i-1])
		    S=S+C1[i];
		}
		
	//	System.out.println(S);
		
		char C2[]=S.toCharArray();
		int L2=C2.length;
		
		if(K>L2)
		{
			System.out.println(-1);
		}
		else
		{
		List<Integer> L=new ArrayList<Integer>();
		
		for(int j=0;j<=L2-K;j++)
		{
		int a=C2[j]-'a'+1;
		int c=1,k=j;
		
		for(int i=j;i<L2;i++)
		{
		   if(C2[i]-C2[k]>1)
		   {
			   k=i;
		       a+=C2[i]-'a'+1;
		       c++;
		   }
		   if(c==K)
		   {
			   L.add(a);
			   break;
		   }
		}
		}
		
	//	System.out.println(L);
		if(L.size()!=0)
		{
			Collections.sort(L);
			System.out.println(L.get(0));
		}
		else
		System.out.println(-1);
		}
		
	}}