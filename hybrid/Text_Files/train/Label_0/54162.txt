import java.io.*;
import java.util.*;


public class asitis
{

	
	

	static OutputStream outputStream = System.out;
	static PrintWriter out = new PrintWriter(outputStream);




	
	public static void main(String[] args)throws IOException{
		
			
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

			int n=Integer.parseInt(br.readLine());

			String[] s=br.readLine().split(" ");

			PriorityQueue<Integer> pq= new PriorityQueue<Integer>();

			for(int i=0;i<n;i++) pq.add(Integer.parseInt(s[i]));

			long check=1;

			int days=0;

			while(pq.size()>0)
			{
				while(pq.size()>0 && pq.peek()<check)
					pq.poll();

				if(pq.size()>0)
				{
					days++;
					pq.poll();
				}
				check++;
			}
			
			out.println(days);
			
			
			out.close();

	}
}